from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=False,  # Make the email field optional
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Re-Enter Password</small></span>'




    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise forms.ValidationError("Your password must contain at least 8 characters.")

        if password1.isdigit():
            raise forms.ValidationError("Your password can't be entirely numeric.")

        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data
    


class AddRecordForm(forms.ModelForm):
    name = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")

    email = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")

    password = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Password", "class":"form-control"}), label="")

    phone = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")

    city = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")

    state = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")

    country = forms.CharField(required=True, widget = forms.widgets.TextInput(attrs={"placeholder":"Country", "class":"form-control"}), label="")


    class Meta:
        model = Record
        exclude = ("user",)

    