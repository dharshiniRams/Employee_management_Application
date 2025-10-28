from django.shortcuts import render, redirect, get_object_or_404
from EmployeeApp.models import Employee
from EmployeeApp.forms import EmployeeForm

def empDetails(request):
    emp_data = Employee.objects.all()
    if not emp_data:
        message = "No employees found."
    else:
        message = ""
    return render(request, 'EmployeeApp/employees.html', {
        'emp_list': emp_data,
        'message': message
    })

def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm()

    return render(request, 'EmployeeApp/add_employee.html', {'form': form})

def editEmployee(request, empId):
    emp = get_object_or_404(Employee, empId=empId) 

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=emp)

    return render(request, 'EmployeeApp/edit_employee.html', {'form': form, 'edit': True})

def deleteEmployee(request, empId):
    emp = get_object_or_404(Employee, empId=empId)
    emp.delete()
    return redirect('employee_list')
