from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserDetails
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, get_user_model, password_validation


class SignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.CharField(max_length=30)
    region = forms.ChoiceField(choices=[
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
    ])
    diabetic = forms.ChoiceField(choices=[
        ('True', 'Yes'),
        ('False', 'No'),
    ])
    gain_weight = forms.ChoiceField(choices=[
        ('True', 'Yes'),
        ('False', 'No'),
    ])
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    
    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        if self.cleaned_data.get('confirm_password') != password:
            raise forms.ValidationError("Password didn't match")

        return cleaned_data

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            UserDetails.objects.create(
                user=user,
                age=self.cleaned_data["age"],
                region=self.cleaned_data["region"],
                is_diabetic=self.cleaned_data["diabetic"],
                gain_weight=self.cleaned_data["gain_weight"],
            )
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user