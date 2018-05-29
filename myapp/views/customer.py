from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Customer, Employee
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def view(request):
	customers = Customer.objects.all()
	return render(request, 'customer/viewallcustomer.html', {'customers': customers})


def addCustomer(request):
	return render(request, 'customer/addcustomer.html')


def insert(request):
	companyName = request.POST['companyName']
	Name = request.POST['Name']
	email = request.POST['email']
	phone = request.POST['phone']
	street = request.POST['street']
	city = request.POST['city']
	state = request.POST['state']
	zipcode = request.POST['zipcode']
	quoteType = request.POST['quoteType']
	employee = Employee.objects.get(EmpID=1)

	addcustomerdetails = Customer(CompanyName=companyName, Password=1001, Name=Name, Street=street, City=city,
						 State=state, ZipCode=zipcode, Email=email, Phone=phone, Type=quoteType, EmpID=employee)
	addcustomerdetails.save()
	return render(request, 'customer/addcustomer.html')

def index(request):
	return render(request, 'home.html')