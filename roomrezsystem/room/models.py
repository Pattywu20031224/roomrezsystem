from django.db.models import *

# Create your models here.

class Room(Model):

    ST_OPTIONS = [
        (0,'使用中'),
        (1,'開放使用')
    ]

    name = CharField('教室名稱', max_length=48)
    preface = ImageField('教室圖片', blank=True)
    detail = TextField('詳細資訊', blank=True)
    status = IntegerField('狀態', default=0 , choices=ST_OPTIONS)
    #status的選項可能要改一下