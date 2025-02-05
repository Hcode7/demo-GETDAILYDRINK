from django.shortcuts import render
from .models import UserWaterUntake
from .forms import WaterIntakeForm
from .utils import calculte_daily_water_intake

# Create your views here.


def log_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            activity_level = form.cleaned_data['activity_level']
            weight = form.cleaned_data['weight']
            climate = form.cleaned_data['climate']
            health_conditions = form.cleaned_data['health_conditions']
            
            total_water = calculte_daily_water_intake(gender, age, weight, climate, health_conditions, activity_level)

            total_water = round(total_water, 2)

            # UserWaterUntake.objects.create(
            #     water_amount=total_water,
            # )
            return render(request, 'pages/log_water.html', {'form' : form, 'total_water' : total_water})
        else:
            print(form.errors)
    else:
        form = WaterIntakeForm()
    
    return render(request, 'pages/log_water.html', {'form' : form})