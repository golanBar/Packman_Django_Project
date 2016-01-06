from braces.views import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

from .forms import SubscriberForm
from .models import Subscriber


def subscriber_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # Create the User record
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            # Create Subscriber Record
            nickname = form.cleaned_data['nickname']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            sub = Subscriber(user=new_user, nickname=nickname, gender=gender, age=age)
            sub.save()
            # Auto login the user
            # return redirect('team_list')
            # Auto login the user
            authuser = authenticate(username=username, password=password)
            if authuser is not None:
                if authuser.is_active:
                    login(request, authuser)
                    return HttpResponseRedirect(reverse('team_list'))
                else:
                    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
            else:
                return HttpResponseRedirect(reverse('sub_new'))
        else:
            print("form is not valid")
            return render(request, template, {'form': form})
    else:
        form = SubscriberForm()

    return render(request, template, {'form': form})


@login_required()  # Decorating a FBV to ensures that only authenticated users can access this page.
def subscriber_details(request):
    sub = Subscriber.objects.get(user=request.user)
    variables = {
        'sub': sub,
    }
    return render(request, 'subscribers/subscriber_details.html', variables)



