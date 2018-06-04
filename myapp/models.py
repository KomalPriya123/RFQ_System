from django.db import models

# Create your models here.
class Employee(models.Model):
	EmpID = models.AutoField(primary_key=True) 
	Name = models.CharField(max_length=255)
	Password = models.CharField(max_length=255)
	Street = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	ZipCode = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Phone = models.IntegerField()
	
	class Meta:
		db_table ="employee"


class Customer(models.Model):
	CustID = models.AutoField(primary_key=True) 
	CompanyName = models.CharField(max_length=255)
	Password = models.CharField(max_length=255)
	Name = models.CharField(max_length=255)
	Street = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	ZipCode = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Phone = models.IntegerField()
	Type = models.IntegerField()
	EmpID = models.ForeignKey(Employee, db_column='EmpID',on_delete=models.CASCADE)

	class Meta:
		db_table ="customer"


class Part(models.Model):
	PartID = models.AutoField(primary_key=True) 
	Name = models.CharField(max_length=255)
	Barcode = models.CharField(max_length=12)
	Description = models.CharField(max_length=255)
	QuantityAvail = models.CharField(max_length=255)
	Price = models.CharField(max_length=255)
	Manufacturer = models.CharField(max_length=255)
	Image = models.CharField(max_length=255)
	Comments = models.CharField(max_length=255)

	class Meta:
		db_table ="part"