from django import forms
from .models import Students

class std(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('std_name', 'std_name2', 'std_roll', 'std_contact', 'std_address', 'project')
        labels = {
            'std_name': 'First Member Name',
            'std_name2': 'Second Member Name',
            'std_roll': 'Student Roll',
            'std_contact': 'Contact',
            'std_address': 'Address'
        }
    def __init__(self, *args, **kwargs):
        super(std, self).__init__(*args, **kwargs)
        self.fields['project'].empty_label = "Select"
