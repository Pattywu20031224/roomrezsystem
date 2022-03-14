from operator import mod
from django.db import models
from classes.models import *
from student.models import *

# Create your models here.

class Teacher(Model):
    realname = CharField('姓名', max_length=32)
    #tea_classes = ManyToManyField(Classes,through='Teacher_Classes')
    #classes=models.ManyToManyField(Classes)
    test=models.ManyToManyField(Classes)
    tel = CharField('連絡電話', max_length=10)
    role= CharField('職稱', max_length=20)  #ex:訓育組長、教務主任、高中部數學老師
    cardid= CharField('卡號', max_length=30)
    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.tel, 
            self.role
        )

'''class  Teacher_Classes(Model):
    classes=ForeignKey(Classes,CASCADE)
    teacher=ForeignKey(Teacher,CASCADE)'''