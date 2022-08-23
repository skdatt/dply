from django.shortcuts import render

# Create your views here.
from mvcapp.models import Student
def welcome(req):
    return render(req,template_name='index.html')

def Add_update(req):
    message = ''
    if req.method == 'POST':
        formdata = req.POST  # req.forms
        # elif req.method == 'GET':
        #     formdata = req.GET          #req.args

        sid = formdata.get('id')
        stud = Student.objects.filter(id=sid).first()

        if formdata:
            if not stud:
                stud = Student(First_Name=formdata.get('fname'),
                               Last_Name=formdata.get('lname'),
                               Age=formdata.get('Age'),
                               Email=formdata.get('Email'),
                               Dept=formdata.get('Department'))

                if int(sid):
                    stud.id = sid

                stud.save()
                message = 'Student Record Saved..'
            else:
                stud.First_Name = formdata.get('fname')
                stud.Last_Name = formdata.get('lname')
                stud.Age = formdata.get('Age')
                stud.Email= formdata.get('Email')
                stud.Dept = formdata.get('Department')
                stud.save()
                message = 'Student Record Updated..'
        # Student(**formdata)
        return render(req, template_name='add.html',
             context={"result": message, 'student': Student( id=0,First_Name='', Last_Name='', Age=0, Email='',Dept='')})

    # massage=""
    # if request.method=='POST':
    #     formdata=request.POST
    # # else:
    # #     data=request.GET
    # sid=formdata.get('id')
    # s=Student.objects.filter_all(id=sid).first()
    #     if formdata:
    #        if not s:
    #           s=Student(FIRST_Name= formdata.get('fname'),
    #              Last_Name=formdata.get('lname'),
    #               Age=formdata.get('Age'),
    #              Email=formdata.get('Email'),
    #              Dept=formdata.get('Department'))
    #           s.save()
    #           massage='Student Record saved..... !!!!!!!'
    #        else:
    #         s.First_Name=formdata.get('fname')
    #         s.Last_Name=formdata.get('lname')
    #         s.Age=formdata.get('Age'),
    #         s.Email=formdata.get('Email')
    #         s.Dept=formdata.get('Department')
    #         s.save()
    #         massage = 'Student Record updated..... !!!!!!!'
    #
    #     return render(request,template_name='add.html', context={"Result":massage})

def edit(request,sid):
    return render(request,template_name='index.html')

def delete(request,sid):
    return render(request,template_name='index.html')

def showlist(request):
    return render(request,template_name='index.html')
