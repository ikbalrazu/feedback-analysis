from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.is_active=True
           user.save()
           messages.success(request,'Your Account Created Successfully! Login Now')
           return redirect('login')    
        
    else:
        form = UserRegisterForm()

    #email = EmailMessage('Subject', 'Bodyyugugugygyugugukhjghghgv lulo', to=['mohidulhoque216@gmail.com'])
    #email.send()
    return render(request, 'register.html', {'form': form})