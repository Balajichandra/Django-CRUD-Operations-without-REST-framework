from django import forms
from SinglePointApp.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        input_sal = self.cleaned_data['esal']
        if input_sal < 8000:
            raise forms.ValidationError("Minimum salary should be greater than 8000...")
        return input_sal

class Meta:
    model = Employee
    fields = '__all__'