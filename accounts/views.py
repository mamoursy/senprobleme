from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.



def register(request):
    if request.method == 'POST':
        # Get forms value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Cet Utilisateur est déjà pris')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Cet Email est déjà pris')
                    return redirect('register')
                else:
                    #  Looks good
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    # Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'Tu es maintenant connecter')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'Tu es maintenant inscrit à notre plateforme Senproblème')
                    return redirect('login')



        else:
            messages.error(request, 'Mot de passe not identique')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Vous etes maintenant connecter')
            return redirect('statistique')
        else:
            messages.error(request, 'Invalid utilisateur ou mot de passe')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous etes maintenant déconnecter')
        return redirect('index')

    return redirect('index')



def dashboard(request):
    return render(request, 'accounts/dashboard.html')
