from django.shortcuts import render, redirect
import pickle
import pandas as pd
from .models import Selll

# Load your model (ensure the model file path is correct)
model = pickle.load(open('./Model/resale.pkl', 'rb'))

def selll(request):
    return render(request, 'sell/sell.html')

def predict(request):
    return render(request, 'sell/predict.html')

def brand_switch(brand):
    car_name_map = {
        'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5, 'Ford': 6, 'Renault': 7,
        'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10, 'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13,
        'Mitsubishi': 14, 'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'Lexus': 19,
        'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23, 'Daewoo': 24, 'Kia': 25, 'Fiat': 26,
        'Force': 27, 'Ambassador': 28, 'Ashok': 29, 'Isuzu': 30, 'Opel': 31
    }
    return car_name_map.get(brand, 0)  # Default value of 0 if brand not found

def fuel_switch(fuel):
    fuel_type_map = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}
    return fuel_type_map.get(fuel, 0)  # Default value of 0 if fuel not found

def transmission_switch(transmission):
    transmission_map = {'Manual': 1, 'Automatic': 2}
    return transmission_map.get(transmission, 0)  # Default value of 0 if transmission not found

def owner_type_switch(owner_type):
    owner_type_map = {
        'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3,
        'Fourth & Above Owner': 4, 'Test Drive Car': 5
    }
    return owner_type_map.get(owner_type, 0)  # Default value of 0 if owner_type not found

def result(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        year = int(request.POST.get('year'))
        km_driven = int(request.POST.get('Km_driven'))
        fuel = request.POST.get('fuel')
        transmission = request.POST.get('transmission')
        owner_type = request.POST.get('owner_type')
        mileage = float(request.POST.get('mileage'))
        engine_cc = float(request.POST.get('engine_cc'))
        max_power_bhp = float(request.POST.get('max_power_bhp'))
        seats = float(request.POST.get('seats'))
        image = request.FILES.get('image')

        # Encode categorical variables using switch functions for prediction
        brand_encoded = brand_switch(brand)
        fuel_encoded = fuel_switch(fuel)
        transmission_encoded = transmission_switch(transmission)
        owner_type_encoded = owner_type_switch(owner_type)

        # Create dictionary for DataFrame
        temp = {
            'name': brand_encoded,
            'year': year,
            'km_driven': km_driven,
            'fuel': fuel_encoded,
            'transmission': transmission_encoded,
            'owner': owner_type_encoded,
            'mileage': mileage,
            'engine': engine_cc,
            'max_power': max_power_bhp,
            'seats': seats
        }

        # Create DataFrame
        columns = ['name', 'year', 'km_driven', 'fuel', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
        testData = pd.DataFrame([temp], columns=columns)

        # Make prediction using the model
        output = model.predict(testData)[0]

        # Save the original values to the database
        sell_instance = Selll(
            brand=brand,
            year=year,
            Km_driven=km_driven,
            fuel=fuel,
            transmission=transmission,
            owner_type=owner_type,
            mileage=mileage,
            engine_cc=engine_cc,
            max_power_bhp=max_power_bhp,
            seats=seats,
            image=image,
            price=output,
            
        )
        sell_instance.save()

        context = {'output': output}
        return render(request, 'sell/predict.html', context)

    return redirect('sell:sell')  # Redirect to the sell page if not a POST request
