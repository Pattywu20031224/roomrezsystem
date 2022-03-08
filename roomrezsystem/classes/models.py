from django.db.models import *

# Create your models here.
class Classes(Model):
    name = CharField('班級名稱', max_length=30)

    def __str__(self):
        return "{}".format(
            self.name
        )
