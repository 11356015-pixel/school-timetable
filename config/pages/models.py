from django.db import models

class Course(models.Model):
    name= models.CharField(max_length=100,verbose_name="課程名稱")
    credits= models.IntegerField(verbose_name="學分數")
    is_required=models.BooleanField(default=True, verbose_name="是否必修")
    time_slot=models.CharField(max_length=50,verbose_name="上課時間",null=True,blank=True)

    def __str__(self):
        return f"{self.name} ({self.credits}學分)"
