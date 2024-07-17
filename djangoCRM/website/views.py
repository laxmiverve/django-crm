from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    userInfos = Record.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')
    else:
        return render(request, 'home.html', {'userInfos': userInfos})
    


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are registered and logged in")  
            return redirect('home')
        else:
            messages.error(request, "Invalid form")
            return redirect('register')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    # return render(request, 'register.html', {})
    
    

def user_record(request, pk):
	if request.user.is_authenticated: 
		user_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'user_record':user_record})
	else:
		messages.success(request, "You are not logged in")
		return redirect('home')
     

def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



def delete_record(request, pk):
     if request.user.is_authenticated: 
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, "User record deleted successfully")
        return redirect('home')
     else:
        messages.success(request, "You must be logged in to perform it")
        return redirect('home')
     


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

    