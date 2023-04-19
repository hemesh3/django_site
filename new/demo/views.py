from django.shortcuts import render
from .models import Project
from django.http import HttpResponse

capitals = [
    {'id': '1', 'name': 'Hemesh', 'position': 'Python Developer'},
    {'id': '2', 'name': 'Ajay', 'position': 'Project Manager'},
    {'id': '3', 'name': 'Krishna', 'position': 'Web Developer'},
    {'id': '4', 'name': 'Nitin', 'position': 'Web Developer'},
    {'id': '5', 'name': 'Neha', 'position': 'Database Developer'},
]


def home(request):
    # return HttpResponse("")
    capitals = Project.objects.all()
    print(capitals)
    capitals1 = {'capitals': capitals}

    return render(request, 'demo/index.html', capitals1)


def pos(request,id):
<<<<<<< HEAD
    position12 = Project.objects.get(id=id)
    # position12 = None
    # for i in capitals:
    #     print(i)
    #     if i['id'] == id:
    #         position12 = i
=======
    position12 = None
    for i in capitals:
        if i['id'] == id:
            position12 = i
>>>>>>> 1416e723362dbdef2d18d4b1e1695e306ef516c2
    position1 = {'position12':position12}
    return render(request, 'demo/index2.html', position1)
