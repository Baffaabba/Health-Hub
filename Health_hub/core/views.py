from django.shortcuts import render
from .models import Meal
# Create your views here.


def home(request):
    return render(request, 'base.html')

def dashboard(request):
    from random import shuffle
    user = request.user.details
    meals = Meal.objects.filter(is_diabetic=user.is_diabetic, gain_weight=user.gain_weight)
    
    morning = [x for x in meals if x.time=='breakfast']
    afternoon = [x for x in meals if x.time=='lunch']
    night = [x for x in meals if x.time=='dinner']
    context = {
        'breakfast' : morning,
        'lunch' : afternoon,
        'dinner' : night,
    }
    print(user.region, user.is_diabetic, user.gain_weight, meals, context)
    return render(request, 'store/dashboard.html', context=context)