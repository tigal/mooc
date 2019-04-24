from datetime import datetime
from peewee import *
from sqlalchemy.orm.attributes import History

from application import APP
from models.specialization import Specialization
from models.provider import Provider
from models.student_answers import StudentFinishedTheme
from models.student import Student
from models.static import STATUSES

cert_get_value= 0.3


class CertificateCourse(APP.db.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False, backref='certs')
    course_id = IntegerField(default=0, null=False)
    ud_course_id = IntegerField(default=0, null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)
    cert_status = CharField(choices=STATUSES.items_raw(), null=False, default=STATUSES.REQUESTED)

    class Meta:
        table_name = 'certificate_course'

    def __str__(self):
        return f'{self.cert_id}: in status "{self.cert_status}"'

    @staticmethod
    def get_statuses():
       return STATUSES

    @classmethod
    def set_status_by_id(cls, cert_id, status_name):
        cert = cls.select().where(cls.cert_id == cert_id)
        if cert.exists():
            cert.set_status(status_name)

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
                    message = f'Сертификат №{self.cert_id} студента "{self.student_id}" изменил статус с "{self.cert_status}" на "{status_name}"\n'
                    self.cert_status = status_name  # выставляем статус заказу
                    self.save()  # сохраняем в БД
                else:
                    message = f'Сертификат №{self.cert_id} студента "{self.student}" не смог сменить статус на "{status_name}"'
                History.create(student=self.student, data=message)  # Сохраняем событие в историю
            except Exception as ex:
                transaction.rollback()  # Если произошла ошибка, то откатыаем транзацкцию
            else:
                pass
                self.student.send_message(message)  # отправляем уведомление пользователю по почте
        return result

    def set_requested_status(self):
        return {}

    def set_user_verified_status(self):
        if Student.user_verified(self.student_id):
           return {}
        return None

    def set_validated_status(self):
        course = Course.return_course(self.course_id)
        if course and course.can_get_certificate(self.student_id):
            return {}
        return None

    def set_generated_status(self):
        return {}

    def set_expired_status(self):
        if self.end_date == datetime.now().timestamp():
            return {}
        return None

    def set_updated_status(self):
        return {}


class CertificateSpec(APP.db.Model):
    cert_id = PrimaryKeyField()
    student_id = ForeignKeyField(Student, to_field='student_id', null=False)
    spec_id = ForeignKeyField(Specialization, to_field='spec_id',null=False)
    text = CharField(10000)
    issued = DateTimeField(default=datetime.now, null=False)
    end_date = DateTimeField(default=None)

    class Meta:
        table_name = 'certificate_spec'

class Course(APP.db.Model):
    course_id = PrimaryKeyField()
    name = CharField(100, null=False)
    provider = ForeignKeyField(Provider, to_field='provider_id')
    spec = ForeignKeyField(Specialization, to_field= 'spec_id')
    creation_date = DateTimeField(default=datetime.now, null=False)
    points = IntegerField(default=0, null=False)
    certificate_get = cert_get_value

    class Meta:
        table_name = 'courses'

    def __str__(self):
        return self.name

    @classmethod
    def get_themes(cls):
        return CourseTheme.select(CourseTheme.name).where(CourseTheme.course_id==cls.course_id)

    @classmethod
    def can_get_certificate(cls, student_id):
        student_themes_cnt = StudentFinishedTheme.select().where(StudentFinishedTheme.student_id == student_id &
                                                           StudentFinishedTheme.course_id == cls.course_id).count()
        courses_themes_cnt = cls.get_themes().count()
        if round(student_themes_cnt/courses_themes_cnt) >= cls.certificate_get:
            return True
        return False

    @classmethod
    def get_finished_themes(cls,student_id):
        return CourseTheme.select(CourseTheme.name).join(StudentFinishedTheme,
                                                         on=(CourseTheme.theme_id == StudentFinishedTheme.course_id)).where(
            StudentFinishedTheme.student_id == student_id & StudentFinishedTheme.course_id == cls.course_id)

    @classmethod
    def get_certificate(cls, student_id):
        if cls.can_get_certificate(student_id):
            str = "Course name: " + cls.course_name
            courses_themes = cls.get_finished_themes(student_id)
            str += "Themes: \n"
            for row in courses_themes:
                str += row["name"] + '\n'
            # create new certificate
            CertificateCourse.insert(student_id=student_id, course_id=cls.course_id, text = str)
            print(str)
        else:
            print ('Too less themes passed. Certificate cannot be issued')


class CourseTheme(APP.db.Model):
    theme_id = PrimaryKeyField()
    course_id = ForeignKeyField(Course, to_field= 'course_id', backref='themes')
    name = CharField(100, null=False)
    points = IntegerField(default=0, null=False)


    class Meta:
        table_name = 'themes'

    def __str__(self):
        return self.name


class Question(APP.db.Model):
    question_id = PrimaryKeyField()
    theme_id = ForeignKeyField(CourseTheme, to_field= 'theme_id')
    description = CharField(300, null=False)
    max_points = IntegerField(default=0, null=False)

    class Meta:
        table_name = 'questions'

    def __str__(self):
        return self.name
