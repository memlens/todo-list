from django.db import models
from django.contrib.auth.models import User



#The tasks model
class Task(models.Model):
    
    title=models.CharField(max_length=50)
    
    description=models.CharField(max_length=1000, null=True, blank=True)
    
    completed=models.BooleanField(default=False)
    
    created_at=models.DateTimeField(auto_now_add=True)
    
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering=['completed']
