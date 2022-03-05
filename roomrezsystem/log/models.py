from django.db.models import *
from teacher.models import *
from room.models import *
from room.models import Room
from teacher.models import Teacher

# Create your models here.
class Log(Model):
    teacher = ForeignKey(Teacher, CASCADE)
    room = ForeignKey(Room, CASCADE)
    reserve = DateTimeField('登記時間', auto_now_add=True)
    end = DateTimeField('結束使用時間', null=True)    

    def __str__(self):
        return "{} | {} | {}".format(
            self.reserve, 
            self.teacher.realname, 
            self.room.name
        )