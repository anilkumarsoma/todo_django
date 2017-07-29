from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from .models import Users, Task
# Create your views here.

def index(request):
    all_users = Users.objects.all()
    # template = loader.get_template('todo/index.html')
    # request.session['username'] = 'Sowmya'
    context = {'all_users' : all_users, 'session_set':request.session['username']}
    # html = ''
    # for user in all_users:
    #     url ='/manage/'+str(user.id)+'/'
    #     html += '<a href="'+url+'">'+user.username+'</a><br>'
    # return HttpResponse(template.render(context,request))
    return render(request, 'todo/index.html', context)

def details_user(request, user_id):
    # return HttpResponse("<h2>"+str(user_id)+"</h2>")
    # try:
    #     all_users = Users.objects.get(pk=user_id)
    # except Users.DoesNotExist:
    #     raise Http404('User not in database')
    all_users = get_object_or_404(Users, pk=user_id)
    return render(request,'todo/detailuser.html', {'user' : all_users} )

def addTask(request):
    userid = request.session['id']
    task = Task()
    user = Users.objects.get(pk=userid)
    task.user = user
    task.date = request.POST['date_task']
    task.status = request.POST['title_task']
    task.task = request.POST['details_task']
    task.save()
    return render(request, 'todo/index.html', {'user': user, 'session_set': request.session['username']})

