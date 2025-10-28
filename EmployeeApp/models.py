from django.db import models


class Employee(models.Model):
    empId = models.CharField(primary_key=True, max_length=10, editable=True)
    empName = models.CharField(max_length=50)
    empDesignation = models.CharField(max_length=50)
    empSalary = models.DecimalField(max_digits=10, decimal_places=2)
    empSkills = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.empId:
            last_emp = Employee.objects.order_by('-empId').first()
            if last_emp and last_emp.empId.startswith('E'):
                try:
                    last_num = int(last_emp.empId[1:])
                except ValueError:
                    last_num = 0
            else:
                last_num = 0
            new_id = f"E{last_num + 1:03d}"
            self.empId = new_id
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.empId} - {self.empName}"
