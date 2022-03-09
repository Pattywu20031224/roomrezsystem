from django.db.models import *
from classes.models import *

# Create your models here.
class Student(Model):
    realname = CharField('姓名', max_length=32)
    classes = ForeignKey(Classes, CASCADE)
    cardid= CharField('卡號', max_length=30)
    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.classes, 
            self.cardid
        )