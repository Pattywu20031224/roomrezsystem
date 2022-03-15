from django.db.models import *
from teacher.models import *
from room.models import *
from teacher.models import Teacher
from classes.models import *
from student.models import *

# Create your models here.
class Log(Model):
    ST_OPTIONS = [
        (0,'即將使用'),
        (1,'使用中'),
        (2,'使用完畢')
    ]
    teacher = ForeignKey(Teacher, CASCADE)
    room = ForeignKey(Room, CASCADE)
    #classes = ForeignKey(Classes, CASCADE)
    reserve = DateTimeField('登記時間', null=True)
    end = DateTimeField('結束使用時間', null=True)    
    workstatus = IntegerField('資料狀態', default=0 , choices=ST_OPTIONS)

    
    def __str__(self):
        return "{} | {} | {}".format(
            self.reserve, 
            self.teacher.realname, 
            self.room.name,
            self.classes.name
        )