from django.db import models

from django.utils import timezone


class ChatRoom(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    chatroom = models.ForeignKey(
        'ChatRoom',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'member.User',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        blank=True
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.pk} - {self.comment}'
