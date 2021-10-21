from django.db import models


# Create your models here.


class OpenVpn(models.Model):
    user_name_send = models.TextField(db_column="Имя отправителя")
    user_name_get = models.TextField(db_column="Имя получателя")
    message = models.TextField(db_column="Сообщение")

    def __str__(self):  # Для отображение в админ панели
        return str((self.user_name_send, self.user_name_get))
