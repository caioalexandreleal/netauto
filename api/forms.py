from django import forms
from django.contrib.postgres.forms import SimpleArrayField

class Host(forms.Form):
  device_type = forms.CharField(label="device_type", max_length=100, required=True)
  host = forms.CharField(label="host", max_length=100, required=True)
  username = forms.CharField(label="username", max_length=100, required=True)
  password = forms.CharField(label="password", max_length=100, required=True)
  secret = forms.CharField(label="secret", max_length=100, required=False)
  command = SimpleArrayField(forms.CharField(max_length=100, required=False), required=False)
  commit = forms.BooleanField(label="commit", required=False)
  enable = forms.BooleanField(label="enable", required=False)