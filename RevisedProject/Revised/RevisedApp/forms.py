from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from RevisedApp.models import User,Jobinfo,Coordinator

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=["username"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
		}

class Cordform(forms.ModelForm):
	class Meta:
		model= Coordinator
		fields= ["cord_name","dept","phone_no"]
		widgets={
		 "cord_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your name"}),
		"dept":forms.Select(attrs = {"class": "form-control",}),
		"phone_no":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Enter your Phone number","required":True}),
		}

class Usperm(forms.ModelForm):
	class Meta:
		model = User
		fields=["username","role"]
		widgets={
		 "username":forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
		 "role":forms.Select(attrs={"class":"form-control"}),
		}


class Jobform(forms.ModelForm):
	class Meta:
		model= Jobinfo
		fields = ["title","location","salary","job_role","skills","descrip"]
		widgets={
		"title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter company name"}),
		"location":forms.TextInput(attrs={"class":"form-control","placeholder":"Job Location"}),
		"salary":forms.NumberInput(attrs={"class":"form-control","placeholder":"Salary"}),
		"job_role":forms.TextInput(attrs={"class":"form-control","placeholder":"Job Role"}),
		"skills":forms.TextInput(attrs={"class":"form-control","placeholder":"Skills requried"}),
		"descrip":forms.TextInput(attrs={"class":"form-control","placeholder":"Description"})
		}

class UpJobform(forms.ModelForm):
	class Meta:
		model= Jobinfo
		fields= ["job_role","eligible_percent","eligible_dept","year_of_pass","last_date","com_image"]
		widgets={
		"job_role":forms.TextInput(attrs={"class":"form-control","placeholder":"Job role"}),
		"eligible_percent":forms.TextInput(attrs={"class":"form-control","placeholder":"eligible percent"}),
		"eligible_dept":forms.TextInput(attrs={"class":"form-control","placeholder":"eligible_dept"}),
		"year_of_pass":forms.NumberInput(attrs={"class":"form-control","placeholder":"year_of_pass"}),
		"last_date":forms.DateInput(attrs = {"class": "form-control","placeholder":"Last date to apply"},),
		}

class UtupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","email","rollno","dob","year","dept","phone_no","percentage","backlogs","pass_year","address"]
		widgets= {
		"username":forms.TextInput(attrs = {"class": "form-control","placeholder":"Enter your name","required":True}),
		"email":forms.EmailInput(attrs = {"class": "form-control","placeholder":"Enter your Email","required":True}),
		"rollno":forms.TextInput(attrs = {"class": "form-control","placeholder":"Enter your Roll no","required":True}),
		"dob":forms.DateInput(attrs = {"class": "form-control",}),
		"year":forms.Select(attrs = {"class": "form-control",}),
		"dept":forms.Select(attrs = {"class": "form-control",}),
		"phone_no":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Enter your Phone number","required":True}),
		"percentage":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Enter your Percentage","required":True}),
		"backlogs":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Enter your Backlogs","required":True}),
		"pass_year":forms.NumberInput(attrs = {"class": "form-control","placeholder":"Enter your year of pass","required":True}),
		"address":forms.TextInput(attrs = {"class": "form-control","placeholder":"Enter your address","required":True}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your new password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your new confirmation password"}))
	class Meta:
		model=User
		fields="__all__"
