from django.db import models


# Create your models here.
class VendorServices(models.Model):
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    description = models.TextField(max_length=200,default='')
    service_is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Vendor Services"

    def __str__(self):
        return self.title
    
class VendorVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,default='')
    video_url = models.URLField(default='')

    class Meta:
        verbose_name_plural = "Vendor videos"

    def __str__(self):
        return self.video_url
