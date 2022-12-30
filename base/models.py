from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    chat_id = models.PositiveIntegerField(
        verbose_name='Chat id',
        primary_key=True,
    )
    user = models.ForeignKey(User, null=True, on_delete= models.PROTECT)
    username = models.TextField(
        verbose_name= 'Username',
    )

    def __str__(self):
        return f'#{self.chat_id} {self.username}'
    
    class Meta:
        verbose_name = 'Profile'

class Message(models.Model):
    profile = models.ForeignKey(
        to= 'Profile', 
        verbose_name= 'Profile', 
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Text',
    )
    created_at = models.DateTimeField(
        verbose_name= 'Received At',
        auto_now_add=True,
    )
    def __str__(self):
        return f'Message {self.pk} from {self.profile}'
    class Meta:
        verbose_name = 'Message'