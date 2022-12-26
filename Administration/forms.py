from django import forms
from product.models import *

class add(forms.ModelForm):
	class Meta:
		model = product
		fields = '__all__'