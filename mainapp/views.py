from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from mainapp.forms import RegisterForm


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Article, Category
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='login')
def list(request):
    
    articles = Article.objects.all()
    # Establecer el número de artículos por página
    paginator = Paginator(articles, 2)
    # Obtener la página actual por url
    page = request.GET.get('page')
    # Guardar todos los articulos que hay en la página
    page_articles = paginator.get_page(page)
    return render(request, 'mainapp/index.html', {
        'title': 'Articulos',
        # mostrar page_articles
        'articles': page_articles,
    })






def about(request):
    return render(request, 'mainapp/about.html', {
        "title": "About",
    })
    
def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()
        
        # Recibe el método en mediante el form
        if request.method == "POST":
            # envia la rq mediante POST
            register_form = RegisterForm(request.POST)
            # si el formulario es válido
            if register_form.is_valid():
                # guarda el registro
                register_form.save()
                # mensaje flash
                messages.success(request, "Tu registro fue existoso!")
                # redirecciona a la página de inicio
                return redirect('index')
            
    
        return render(request, "users/register.html", {
            "title": "Registro",
            "register_form": register_form,
        })
# login  
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        # Si el método es POST recibir mediante el form el usuario y contraseña
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            # autenticar usuario
            user = authenticate(request, username=username, password=password)
        
            # si el usuario es válido, enviamos a la rq el user y redirect
            if user is not None:
                login(request, user)
                return redirect('index')
            # si no mostramos un flash message
            else:
                messages.warning(request, "Error, usuario o contraseña incorrectos")
    
        # renderiza la página de login
        return render(request, "users/login.html", {
            "title": 'Login'
        })
    
def logout_user(request):
    logout(request)
    return redirect('index')