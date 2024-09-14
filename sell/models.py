# from django.db import models

# # Create your models here.
# from django.db import models

# # Create your models here.
# class sell(models.Model):
	
  
# 	)
# 	MARRIED_CHOICES = (
# 		('Yes', 'Yes'),
# 		('No', 'No')
# 	)
# 	GRADUATED_CHOICES = (
# 		('Graduate', 'Graduated'),
# 		('Not_Graduate', 'Not_Graduate')
# 	)
# 	SELFEMPLOYED_CHOICES = (
# 		('Yes', 'Yes'),
# 		('No', 'No')
# 	)
# 	PROPERTY_CHOICES = (
# 		('Rural', 'Rural'),
# 		('Semiurban', 'Semiurban'),
# 		('Urban', 'Urban')
# 	)
# 	firstname=models.CharField(max_length=15)
# 	lastname=models.CharField(max_length=15)
# 	dependants=models.IntegerField(default=0)
# 	applicantincome=models.IntegerField(default=0)
# 	coapplicatincome=models.IntegerField(default=0)
# 	loanamt=models.IntegerField(default=0)
# 	loanterm=models.IntegerField(default=0)
# 	credithistory=models.IntegerField(default=0)
# 	gender=models.CharField(max_length=15, choices=name)
# 	married=models.CharField(max_length=15, choices=MARRIED_CHOICES)
# 	graduatededucation=models.CharField(max_length=15, choices=GRADUATED_CHOICES)
# 	selfemployed=models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
# 	area=models.CharField(max_length=15, choices=PROPERTY_CHOICES)

# 	def __str__(self):
# 		return '{}, {}'.format(self.lastname, self.firstname)



from django.db import models

# Create your models here.
class Selll(models.Model):
    car_name = [
		('Maruti', 'Maruti'),
		('Skoda', 'Skoda'),
        ('Honda', 'Honda'),
        ('Hyundai','Hyundai'),
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('Renault', 'Renault'),
        ('Mahindra', 'Mahindra'),
        ('Tata', 'Tata'),
        ('Chevrolet', 'Chevrolet'),
        ('Datsun', 'Datsun'),
        ('Jeep', 'Jeep'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Audi', 'Audi'),
        ('Volkswagen', 'Volkswagen'),
        ('BMW', 'BMW'),
        ('Nissan', 'Nissan'),
        ('Lexus', 'Lexus'),
        ('Jaguar', 'Jaguar'),
        ('Land', 'Land'),
        ('MG', 'MG'),
        ('Volvo', 'Volvo'),
        ('Daewoo', 'Daewoo'),
        ('Kia', 'Kia'),
        ('Fiat', 'Fiat'),
        ('Force', 'Force'),
        ('Ambassador', 'Ambassador'),
        ('Ashok', 'Ashok'),
        ('Isuzu', 'Isuzu'),
        ('Opel', 'Opel') ]
    
    fuel_type=(('Diesel', 'Diesel'),
                ('Petrol', 'Petrol'),
                ('LPG', 'LPG'),
                ('CNG', 'CNG')
                )
    
    transmission=(
         ('Manual', 'Manual'),
        ('Automatic', 'Automatic')
    )
    OWNER_CHOICES = [
        ('First Owner', 'First Owner'),
        ('Second Owner', 'Second Owner'),
        ('Third Owner', 'Third Owner'),
        ('Fourth & Above Owner', 'Fourth & Above Owner'),
        ('Test Drive Car', 'Test Drive Car')
    ]
    
    
    
    car_id=models.AutoField(primary_key=True)
    brand=models.CharField(choices= car_name,null=False,blank=False,max_length=50)
    year=models.IntegerField(null=False,blank=False)
    Km_driven=models.IntegerField(null=False,blank=False)
    fuel=models.CharField(choices= fuel_type,null=False,blank=False,max_length=50)
    transmission=models.CharField(choices=transmission,null=False,blank=False,max_length=50)
    owner_type = models.CharField(null=False,blank=False, choices=OWNER_CHOICES,max_length=50)
    mileage = models.FloatField(null=False,blank=False)  # assuming mileage is in km/l or similar units
    engine_cc = models.FloatField(null=False,blank=False) 
    max_power_bhp = models.FloatField(null=False,blank=False)
    seats = models.FloatField(null=False,blank=False) 
    image=models.ImageField(upload_to="static/images", default="static/images/default.jpeg")
    price=models.FloatField(null=False,blank=False, default=0.0)



    def __str__(self):
       return f"{self.car_id}: {self.brand} {self.year}{self.Km_driven}{self.fuel}{self.transmission}{self.owner_type}{self.mileage}{self.engine_cc}{self.max_power_bhp}{self.seats}"
