


def calculte_daily_water_intake(gender, age, weight, climate, health_conditions, activity_level):

    water_amount = weight * 0.033


    if gender == 'male':
        water_amount *= 1.2

    climate_factor = {
        'cold' : 1,
        'temperate' : 1.05,
        'hot' : 1.1, 
    }

    water_amount *= climate_factor.get(climate, 1)

    activity_factor = {
        'sedentary': 1.0,
        'lightly-active': 1.1,
        'moderately-active': 1.2,
        'very-active': 1.3,
    }

    water_amount *= activity_factor.get(activity_level, 1)

    if age > 60:
        water_amount *= 0.9

    health_conditions_factor = {
        'pregnancy': 1.2,    
        'diabetes': 1.3,   
        'kidney disease': 0.8,
        'heart disease': 0.9, 
        'none' : 1.0,
    }

    if isinstance(health_conditions, str):
        health_conditions = [hc.strip().lower() for hc in health_conditions.split(',')]

    elif not isinstance(health_conditions, list):
        health_conditions = []
    
    for condition in health_conditions:
        water_amount *= health_conditions_factor.get(condition, 1.0)

    return round(water_amount, 2)