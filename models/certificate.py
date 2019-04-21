from datetime import datetime

import STATUSES as STATUSES
from peewee import *
from sqlalchemy.orm.attributes import History

from application import DB, APP
from models.course import Course
from models.student import Student
from models.specialization import Specialization


class CertificateCourse(DB.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False, backref='certs')
    course_id = IntegerField(default=0, null=False)
    ud_course_id = IntegerField(default=0, null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'certificate_course'

    def __str__(self):
        return f'{self.cert_id}: in status "{self.cert_status}"'

    @staticmethod
    def get_statuses():
        #statuses = ['requested', 'validated', 'refused', 'user verified', 'userdata demand', 'generated', 'expired']
        return STATUSES

    @classmethod
    def set_status_by_id(cls, cert_id, status_name):
        cert = cls.select().where(cls.cert_id == cert_id)  # actually это может быть нашим первым методом if_first_generation
        if cert.exists():
            cert.set_status('updated')
        else:
            cls.cert_request() #no certificate in DB, что положить в качестве аргумента?

    def set_status(self, status_name):
        result = None

        with APP.db.Model.database.atomic() as transaction:  # Работаем в транзацкции
            try:
                method_status_name = f'set_{status_name}_status'  # формируем название метода, который хотим вызвать
                if hasattr(self, method_status_name):
                    result = getattr(self, method_status_name)()  # вызываем метод для установки статуса, если есть
                else:
                    result = True
                print(result)
                if result is not None:  # Если всё прошла хорошо, со сохраняем новый статус
                    message = f'Сертификат №{self.cert_id} студента "{self.student}" изменил статус с "{self.cert_status}" на "{status_name}"\n'
                    self.cert_status = status_name  # выставляем статус заказу
                    self.save()  # сохраняем в БД
                else:
                    message = f'Сертификат №{self.cert_id} студента "{self.student}" не смог сменить статус на "{status_name}"'
#это скорее случай с обрывом подкючения?
                History.create(student=self.student, data=message)  # Сохраняем событие в историю
            except Exception as ex:
                transaction.rollback()  # Если произошла ошибка, то откатыаем транзацкцию
            else:
                self.student.send_message(message)  # отправляем уведомление пользователю по почте
        return result

    def cert_request(self):
        if self.user_is_verified():
            if self.is_validated:
                self.set_status('generated')
                return {}
            return True

    def user_is_verified(self):
        if True:# query to the base где лежит зачекан студент или нет
            self.set_status('user verified')
            return True
        else:
            message = 'user not verified' #будет выделено как ошибка пока сверхну не поменяем Тру
            self.set_status('refused')
            return False

    def is_validated(self):
        if Course.can_get_certificate(): #положить аргументы
            self.set_status('validated')
            return True
        else:
            message = 'not validated'
            self.set_status('refused')
            return False

    def cert_expired(self):
        if self.end_date == datetime.now().timestamp():
            self.set_status('expired')
            return {}

class CertificateSpec(DB.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False)
    spec_id = ForeignKeyField(Specialization, to_field='spec_id',null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'certificate_spec'