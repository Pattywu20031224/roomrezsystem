from django.shortcuts import render
from log.models import *
from datetime import *
from classes.models import *

def CheckForm(request):
    return render(request, 'check/checkform.html')
def Check(request):
    id=request.GET.get('id','no_id')
    room=request.GET.get('room','no_room')
    logs=Log.objects.filter(room_id=room)
    for log in logs:
        if log.end < datetime.now(timezone.utc):
            log.workstatus=0
            log.save()
        elif log.reserve > datetime.now(timezone.utc):
            log.workstatus=2
            log.save()
        elif log.reserve <= datetime.now(timezone.utc) and log.end >= datetime.now(timezone.utc) :
            log.workstatus=1
            log.save()
    checks=Log.objects.filter(room_id=room,workstatus=1)
    for check in checks:
        classes=Classes.objects.get(id=check.classes_id)
        classes_students=classes.student_set.all()
        for student in classes_students:
            if student.cardid == id:
                return render(request, 'check/check_true.html')

    return render(request, 'check/check_false.html')
# Create your views here.
