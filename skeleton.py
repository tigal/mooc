class Certificate(APP.db.Model):
    cert_id = PrimaryKeyField()
   # customer = ForeignKeyField(Customer, to_field='customer_id', null=False, backref='orders')
    cert_status = CharField(choices=STATUSES.items_raw(), null=False, default=STATUSES.PRE_ORDER)
    #create_time = DateTimeField(default=datetime.now, null=False)

    class Meta:
        table_name = 'certificates'

    def __str__(self):
        return f'{self.cert_id}: in status "{self.cert_status}"'

    # @staticmethod
    # def get_statuses():
    #     # костыль для доступа к возможным статусам
    #     return STATUSES

    # @classmethod
    # def set_status_by_id(cls, order_id, status_name):
    #     order = cls.select().where(cls.order_id == order_id)  # выбираем конкретный заказ
    #     if order.exists():
    #         order.set_status(status_name)

    # def set_status(self, status_name):
    #
    #     result = None
    #
    #     with APP.db.Model.database.atomic() as transaction:  # Работаем в транзацкции
    #         try:
    #             method_status_name = f'set_{status_name}_status'  # формируем название метода, который хотим вызвать
    #             if hasattr(self, method_status_name):
    #                 result = getattr(self, method_status_name)()  # вызываем метод для установки статуса, если есть
    #             else:
    #                 result = True
    #             print(result)
    #             if result is not None:  # Если всё прошла хорошо, со сохраняем новый статус
    #                 message = f'Сертификат №{self.order_id} студента "{self.student}" изменил статус с "{self.cert_status}" на "{status_name}"\n'
    #                 message += make_message_by_items(result)
    #                 self.cert_status = status_name  # выставляем статус заказу
    #                 self.save()  # сохраняем в БД
    #             else:
    #                 message = f'Сертификат №{self.order_id} студента "{self.student}" не смог сменить статус на "{status_name}"'
    #
    #             History.create(student=self.student, data=message)  # Сохраняем событие в историю
    #         except Exception as ex:
    #             transaction.rollback()  # Если произошла ошибка, то откатыаем транзацкцию
    #         else:
    #             self.student.send_message(message)  # отправляем уведомление пользователю по почте
    #     return result

    def requested(self):
        if is_first_generated:
            if user_is_verified:
                if is_validated:
                    set_status('generated')
                    return {}


    def is_first_generated(self):
        if sertificate is not in DB:
            return True
        else:
            set_status('updated')
            return False

    def user_is_verified(self):
        if user is verified:
            set_status('user verified')
            return True
        else:
            message = 'user not verified'
            return False

    def is_validated(self):
        if sertificate is correct:
            set_status('validated')
            return True
        else:
            message = 'not validated'
            return False

    def expired(self):
        set_status('expired')
        return {}