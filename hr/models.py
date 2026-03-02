from django.db import models
from datetime import date
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    def __str__(self):
        return self.full_name
    
    def save(self, *args,**kwargs):
        if self.full_name:
            self.full_name = self.full_name.title()  # isimleri baş harfleri büyük olsun dedim 
        if self.salary and self.salary<28000:
            self.salary = 28000  # minimum maaş sınırını 
        if not self.email and self.full_name:
            isim_temiz = self.full_name.lower()\
                .replace(' ', '.')\
                .replace('ı', 'i')\
                .replace('ö', 'o')\
                .replace('ğ', 'g')\
                .replace('ü', 'u')\
                .replace('ş', 's')\
                .replace('ç', 'c')
            self.email = isim_temiz + '@company.com'  #mail boş bırajılırsa isim soyisime göre oluştursun
        super().save(*args, **kwargs)
    @property
    def annual_salary(self):
        if self.salary:
            return self.salary * 12
        return None
    @property
    def tenure_in_years(self):
        if self.hire_date:
            today = date.today()
            years = today.year - self.hire_date.year - ((today.month, today.day) < (self.hire_date.month, self.hire_date.day))
            return years
        return None

