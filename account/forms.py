from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        # We don't need to add Bootstrap classes explicitly anymore
        # Crispy Forms will handle the styling
        
        # Mark email field as required
        self.fields['email'].required = True
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is invalid')
        
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long')
            
        return email 