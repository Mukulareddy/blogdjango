from django import forms
from django.forms import ModelForm
from entry.models import Entry

class EntryForm(ModelForm):
	class Meta:
		model = Entry
		exclude = ()
