from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Meal
import random
# Create your views here.


def home(request):
    return render(request, 'store/index.html')

def dashboard(request):
    if request.user.is_superuser:
        return redirect(reverse('admin:index'))
    user = request.user.details
    meals = Meal.objects.filter(is_diabetic=user.is_diabetic, gain_weight=user.gain_weight)
        
    morning = [x for x in meals if x.time=='breakfast']
    afternoon = [x for x in meals if x.time=='lunch']
    night = [x for x in meals if x.time=='dinner']
    context = {
        'breakfast' : random.choice(morning),
        'lunch' : random.choice(afternoon),
        'dinner' : random.choice(night),
    }

    print(user.region, user.is_diabetic, user.gain_weight, meals, context)
    return render(request, 'store/dashboard.html', context=context)