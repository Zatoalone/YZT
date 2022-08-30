from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def profile(request):
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
    template = "accounts/profile.html"
    print(get_profile.user)
    return render(request, template, context)