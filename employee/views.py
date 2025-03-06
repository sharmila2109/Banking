
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

def login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
            

def logout(request):
    return redirect(request,'login.html')

def register(request):
    return render(request,'register.html')

def registeration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registration successful')
        return redirect('login')    

def customer_support(request):
    return render(request, 'customer_Support.html')

def Contact(request):
    return render(request, 'contact.html')

# About
def about(request):
    return render(request, 'about.html')

# Services
def services(request):
    return render(request, 'services.html')

# Withdrawal
def withdrawl(request):
    return render(request, 'withdrawl.html')

# Balance
def balance(request):
    return render(request, 'balance.html')

# Deposit
def deposit(request):
    return render(request, 'deposit.html')

def dashboard(request):
    return render(request, 'dashboard.html')
