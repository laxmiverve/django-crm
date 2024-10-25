from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            userInfos = Record.objects.all()
        else:
            userInfos = Record.objects.filter(user=request.user)
    else:
        userInfos = None

    if request.method == "POST":
        login_credential = request.POST['username']
        password = request.POST['password']

        # authenticate with the username
        user = authenticate(request, username=login_credential, password=password)

        # If username not exist, try to authenticate with the email
        if user is None:
            user_with_email = User.objects.filter(email=login_credential).first()
            if user_with_email:
                user = authenticate(request, username=user_with_email.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username/email or password")
            return redirect('home')
    else:
        return render(request, 'home.html', {'userInfos': userInfos})




@login_required
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, "Record Added...")
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})






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
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})





def user_record(request, pk):
    if request.user.is_authenticated:
        user_record = Record.objects.get(id=pk, user=request.user)
        return render(request, 'record.html', {'user_record': user_record})
    else:
        messages.success(request, "You are not logged in")
        return redirect('home')





def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk, user=request.user)
        if request.method == "POST":
            delete_it.delete()
            messages.success(request, "User record deleted successfully")
            return redirect('home')
        return render(request, 'record.html', {'user_record': delete_it})
    else:
        messages.success(request, "You must be logged in to perform it")
        return redirect('home')




def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk, user=request.user)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
