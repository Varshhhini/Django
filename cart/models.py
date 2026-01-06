from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def total_price(self):
        return self.course.price * self.quantity
