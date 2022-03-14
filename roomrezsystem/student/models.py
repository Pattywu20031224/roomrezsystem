from re import M
from statistics import mode
from django.db.models import *
from classes.models import *
from django.db import models

from classes.models import *

# Create your models here.
class Student(Model):
    realname = CharField('姓名', max_length=32)
    stu_classes = models.ManyToManyField(Classes,through='Student_Classes')
    cardid= CharField('卡號', max_length=30)
    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.classes, 
            self.cardid
        )

class Student_Classes(Model):
    classes=models.ForeignKey(Classes,CASCADE)
    student=models.ForeignKey(Student,CASCADE)