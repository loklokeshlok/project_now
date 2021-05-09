from django.shortcuts import render,redirect
from django.core.mail import send_mail
from own import settings
from datetime import date
from django.core.mail import send_mail

# Create your views here.
def home(self):
	return render(self,'html/home.html')

def achievment(self):
	todays_date = date.today()
	y = {'1':todays_date.year-1,'2':todays_date.year-2,'3':todays_date.year-3,'4':todays_date.year-4,'5':todays_date.year-5}
	return render(self,'html/achievments.html',{'y':y})

def loginpage(self):
	if self.method == 'POST':
		email = self.POST["mail"]
		subject = "welcome user"
		message = "thank you for registering."
		# email_from = settings.EMAIL_HOST_USER
		# recipient_list = [email,]
		send_mail(subject,message,'loklokesh9988@gmail.com',['loklokesh9876@gmail.com'],fail_silently=False,)
		return render(self,'html/test.html')
	return render(self,'html/login_page.html')
