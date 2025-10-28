from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empId', 'empName', 'empDesignation', 'empSalary', 'empSkills']
        widgets = {
            "empId": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "empName": forms.TextInput(attrs={"class": "form-control"}),
            "empDesignation": forms.TextInput(attrs={"class": "form-control"}),
            "empSalary": forms.NumberInput(attrs={"class": "form-control"}),
            "empSkills": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            last_emp = Employee.objects.order_by('-empId').first()
            if last_emp and last_emp.empId.startswith('E'):
                try:
                    last_num = int(last_emp.empId[1:])
                except ValueError:
                    last_num = 0
            else:
                last_num = 0

            new_id = f"E{last_num + 1:03d}"
            self.fields['empId'].initial = new_id

        self.fields['empId'].disabled = True
