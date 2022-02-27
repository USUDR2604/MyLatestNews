from django import forms
from django.forms.widgets import NumberInput
# import GeeksModel from models.py
from .models import *

class SearchDetailsForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = SearchDetails
		fields = "__all__"

class FeedbackForm(forms.ModelForm):
	class Meta:
		model=FeedBackDetailsModel
		fields="__all__"