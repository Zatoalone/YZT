from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile


@login_required
def index(request):
    #return render(request, "dashboard/index.html")

    get_profile = Profile.objects.get(user_id=request.user.id)
    get_user = request.user
    print(get_user)
    #get_group = StudentsGroup.objects.all()
    #get_lessons = Lesson.objects.all()
    context = {
        #'get_lesson': get_lessons,
        #'get_group': get_group,
        'get_profile': get_profile,
        'get_user': get_user
    }
    template = "dashboard/index.html"
    print(get_profile.user)
    return render(request, template, context)
