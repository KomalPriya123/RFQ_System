from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Customer, Employee
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def view(request):
	customers = Customer.objects.all()
	return render(request, 'customer/viewallcustomer.html', {'customers': customers})

def add(request):
	if request.method == 'POST':
		companyName = request.POST['companyName']
		Name = request.POST['name']
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

def edit(request, id):
	customer = Customer.objects.get(CustID=id)
	if request.method == 'POST':
		customer.CompanyName = request.POST['companyName']
		customer.Name = request.POST['name']
		customer.Email = request.POST['email']
		customer.Phone = request.POST['phone']
		customer.Street = request.POST['street']
		customer.City = request.POST['city']
		customer.State = request.POST['state']
		customer.ZipCode = request.POST['zipcode']
		customer.Type = request.POST['quoteType']
		print(customer.Phone)
		customer.save()
		print(customer.Phone)
	return render(request, 'customer/updatecustomer.html', {'customer': customer})
