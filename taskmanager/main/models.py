from django.db import models


class Message(models.Model):
    name = models.CharField('name', max_length=100)
    email = models.CharField('Description', max_length=100)
    subject = models.CharField('Subject', max_length=100)
    msg = models.TextField('Message')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
