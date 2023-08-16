from django.db import models

from users.models import UserProfile


class Chat(models.Model):
    participants = models.ManyToManyField(UserProfile, related_name='chats')
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_chats')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_file = models.BooleanField(default=False)
    file = models.FileField(upload_to='chat_files/', null=True, blank=True)
