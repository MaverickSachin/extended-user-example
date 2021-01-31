from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User


class HomePageView(TemplateView):
    template_name = 'profiles/home.html'


class UserProfileView(View):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        context = {
            'viewed_user': user
        }

        return render(request, 'profiles/profile.html', context=context)
