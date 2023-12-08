from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
def hosters_main(request):
    return render(request, 'main_page/main.html')

def login(request):
    return render(request, 'main_page/login.html')


def join(request):
    return render(request, 'main_page/join.html')
def mypage(request):
    return render(request, 'main_page/my_page.html')


from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm

from django.shortcuts import render, redirect
from surveys_app.forms import RoommatePreferencesForm

def survey_view(request):
    if request.method == 'POST':
        form = RoommatePreferencesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = RoommatePreferencesForm()
    return render(request, 'main_page/survey.html', {'form': form})

