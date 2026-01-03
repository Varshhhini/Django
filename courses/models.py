from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


