from django.db import models


# Create your models here.
class AppFeedBack(models.Model):
    description = models.CharField(max_length=200,null=True,blank=True)
    rating = models.CharField(max_length=5,blank=True,null=True)
    submit_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.rating
