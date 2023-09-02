from django.db import models
from django.utils.timezone import now

# Create your models here.

blood_choices = (
    ("A+","A+"),
    ("A-","A-"),
    ("A1-","A1-"),
    ("A1+","A1+"),
    ("A1B+","A1B+"),
    ("A1B-","A1B-"),
    ("A2+","A2"),
    ("A2B+","A2B+"),
    ("A2B-","A2B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("B+","B+"),
    ("B-","B-"),
    ("Bombay blood group","Bombay blood group"),
    ("INRA","INRA"),
    ("O+","O+"),
    ("O-","O-"),
)
state_choices = (
("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")
)


class Doner(models.Model):
    user_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    blood_group = models.CharField(choices=blood_choices,null=False,max_length=100)
    state = models.CharField(choices=state_choices,null=False,max_length=100)
    city = models.CharField(max_length=100)
    timestamp = models.DateField(default=now)
    
    def __str__(self):
        return self.user_name
    