from django.db.models import *

# Create your models here.

class Room(Model):

    ST_OPTIONS = [
        (0,'使用中'),
        (1,'開放使用')
    ]

    name = CharField('教室名稱', max_length=48)
    detail = TextField('詳細資訊', blank=True)
    status = IntegerField('狀態', default=0 , choices=ST_OPTIONS)