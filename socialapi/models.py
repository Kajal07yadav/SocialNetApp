from authapi.models import MyUser
from django.db import models

class FriendRequest(models.Model):
    """Friend request object"""

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    sender = models.ForeignKey(MyUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(MyUser, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'receiver')

    def __str__(self):
        return f"From {self.sender} to {self.receiver} - Status: {self.status}"
