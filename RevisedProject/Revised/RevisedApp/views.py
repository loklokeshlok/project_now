from django.shortcuts import render,redirect
from RevisedApp.forms import UsForm,Usperm,Jobform,UpJobform,UtupForm,ChpwdForm
from django.core.mail import EmailMessage
from Revised import settings
from RevisedApp.models import User,Jobinfo

# Create your views here.

def homepage(request):
	return render(request,'html/home.html')

def abtpage(self):
	return render(self,'html/abtpage.html')

def  ach(self):
	
	return render(self,'html/ach.html')

def register(request):
	if request.method=="POST":
		t=UsForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lg')
	y=UsForm()
	return render(request,'html/register.html',{'t':y})

def role(request):
	# mnp = Jobinfo.objects.all()
	return render(request,'html/mp.html')

def requestform(request):
	if request.method == "POST":
		u=request.POST.get('username')
		r=request.POST.get('rollno')
		d=request.POST.get('dept')
		e=request.POST.get('email')
		at=request.FILES['fe']
		y="Regarding approve request of "+u
		# t= mail_admins("Usesr Role",y)
		t=EmailMessage("Usesr approval",y,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1],e])
		t.content_subtype= 'html'
		t.attach(at.name,at.read(),at.content_type)
		t.send()
		if t == 1:
			return redirect('/req')
	return render(request,'html/request.html')

def permissions(request):
	ty=User.objects.all()
	return render(request,'html/permissions.html',{'q':ty})

def gvper(request,k):
	r=User.objects.get(id=k)
	if request.method == "POST":
		k=Usperm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/per')
	k2= Usperm(instance=r)
	return render(request,'html/gvp.html',{'y':k2})

def dashboard(request):
	return render(request,'html/dashboard.html')

def jobposts(request):
	w = Jobinfo.objects.all()
	if request.method== "POST":
		e = Jobform(request.POST)
		if e.is_valid():
			e.save()
			return redirect('/jobs')	
	e=Jobform()
	return render(request,'html/jobs.html',{'z':e,'y':w})


def editjobs(request,a):
	t= Jobinfo.objects.get(id=a)
	if request.method== "POST":
		k= UpJobform(request.POST,instance=t)
		if k.is_valid():
			k.save()
			return redirect('/jobs')
	k2 = UpJobform(instance=t)
	return render(request,'html/editjobs.html',{'b':k2})



def profile(req):
	return render(req,'html/profile.html')


def updf(request):
	if request.method == "POST":
		v=UtupForm(request.POST,instance=request.user)
		if v.is_valid():
			v.save()
			return redirect('/pro')
	z=UtupForm(instance=request.user)
	return render(request,'html/updateprofile.html',{'p':z})
	

def cgf(request):
	if request.method == "POST":
		c=ChpwdForm(request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepassword.html',{'p':c})

def viewjob(request):
	return render(request,'html/viewjob.html')

# def deledata(req,id):
# 	data=Jobinfo.objects.get(id=id)
# 	if req.method=="POST":
# 		data.delete()
# 		return redirect('/jobs')
# 	return render(req,'html/deletejob.html',{'sd':data})


def jobinfo(request):
	a = Jobinfo.objects.all()
	return render(request,'html/jobinfo.html',{'t':a})

# def studentinfo(request):
# 	if request.method == "POST":
# 		sid= request.POST['student_id']
# 		c = User(request.POST,instance=request.rollno)
# 		if c.is_valid():
# 			c.save()
# 			return redirect('/studinfo')
# 	b = User.objects.filter(role=2)
# 	return render(request,'html/studentinfo.html',{'u':b})


def studentinfo(request):
	b = User.objects.filter(role=2)
	return render(request,'html/studentinfo.html',{'u':b})