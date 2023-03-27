import os

from django.db import models

from core.models import User


class TgUser(models.Model):
    class Meta:
        verbose_name = "Бот"

    chat_id = models.PositiveIntegerField(unique=True)
    user_id = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT, null=True)
    verification_code = models.CharField(max_length=32, null=True, blank=True, default=None)

    def set_verification_code(self):
        code = os.urandom(12).hex()
        self.verification_code = code