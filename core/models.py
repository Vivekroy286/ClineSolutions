from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    
    def __str__(self):
        return self.text[:50]
    
    def total_likes(self):
        return self.likes.count()
    
    
    


