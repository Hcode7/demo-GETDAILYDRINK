from django import forms
from .models import UserWaterUntake


class WaterIntakeForm(forms.Form):
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female' , 'Female')], required=False)
    age = forms.IntegerField(min_value=1,max_value=120, required=True)
    weight = forms.IntegerField(min_value=1, max_value=300 , required=True)
    activity_level = forms.ChoiceField(choices=
        [            
            ('sedentary', 'Sedentary'),
            ('lightly-active', 'Lightly Active'),
            ('moderately-active', 'Moderately Active'),
            ('very-active', 'Very Active')
        ]
        ,required=True)
    climate = forms.ChoiceField(choices=[('cold', 'Cold'), ('temperate' , 'Temperate'), ('hot', 'Hot')], required=True)
    health_conditions = forms.ChoiceField(required=False, choices=[ ('none', 'None'), ('diabetes' , 'Diabetes'), ('kidney disease', 'Kidney Disease'), ('heart disease' , 'Heart Disease'),('pregnancy' , 'Pregnancy')])
