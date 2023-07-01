from .models import User
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['nombre']
        
    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user