# from django import forms
# from .models import Selll

# from django import forms

# class SellForm(forms.Form):
#     brand = forms.ChoiceField(choices=[
#         ('Maruti', 'Maruti'),
#         ('Skoda', 'Skoda'),
#         ('Honda', 'Honda'),
#         ('Hyundai', 'Hyundai'),
#         ('Toyota', 'Toyota'),
#         ('Ford', 'Ford'),
#         ('Renault', 'Renault'),
#         ('Mahindra', 'Mahindra'),
#         ('Tata', 'Tata'),
#         ('Chevrolet', 'Chevrolet'),
#         ('Datsun', 'Datsun'),
#         ('Jeep', 'Jeep'),
#         ('Mercedes-Benz', 'Mercedes-Benz'),
#         ('Mitsubishi', 'Mitsubishi'),
#         ('Audi', 'Audi'),
#         ('Volkswagen', 'Volkswagen'),
#         ('BMW', 'BMW'),
#         ('Nissan', 'Nissan'),
#         ('Lexus', 'Lexus'),
#         ('Jaguar', 'Jaguar'),
#         ('Land', 'Land'),
#         ('MG', 'MG'),
#         ('Volvo', 'Volvo'),
#         ('Daewoo', 'Daewoo'),
#         ('Kia', 'Kia'),
#         ('Fiat', 'Fiat'),
#         ('Force', 'Force'),
#         ('Ambassador', 'Ambassador'),
#         ('Ashok', 'Ashok'),
#         ('Isuzu', 'Isuzu'),
#         ('Opel', 'Opel')
#     ])
    
#     year = forms.IntegerField()
#     Km_driven = forms.IntegerField()
#     fuel = forms.ChoiceField(choices=[
#         ('Diesel', 'Diesel'),
#         ('Petrol', 'Petrol'),
#         ('LPG', 'LPG'),
#         ('CNG', 'CNG')
#     ])
#     transmission = forms.ChoiceField(choices=[
#         ('Manual', 'Manual'),
#         ('Automatic', 'Automatic')
#     ])
#     owner_type = forms.ChoiceField(choices=[
#         ('First Owner', 'First Owner'),
#         ('Second Owner', 'Second Owner'),
#         ('Third Owner', 'Third Owner'),
#         ('Fourth & Above Owner', 'Fourth & Above Owner'),
#         ('Test Drive Car', 'Test Drive Car')
#     ])
#     mileage = forms.FloatField()
#     engine_cc = forms.FloatField()
#     max_power_bhp = forms.FloatField()
#     seats = forms.FloatField()
#     image = forms.ImageField(required=False)
