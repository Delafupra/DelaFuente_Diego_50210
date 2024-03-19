from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


#Login

def InicioSesion(request):
    
    if request.method == "POST":
        
        form =AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})
        
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
    
    else:
        
        form = AuthenticationForm()
        
    return render(request, "AppCoder/login.html", {"formulario":form})

#Registro

def registro(request):
    
    if request.method == "POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado"})
        
    else:
            
        form =UsuarioRegistro()
            
    return render(request, "AppCoder/registro.html", {"formulario":form})

#editar usuario

@login_required
def editarUsuario(request):
    
    usuario = request.user
    
    if request.method ==  "POST":
        
        form = FormularioEditar(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
        
    return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})
            

@login_required
def agregarAvatar(request):
    
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            usuarioActual = User.objects.get(username=request.user)
            
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            
            avatar.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        form = AvatarFormulario()
        
    return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})
                       
def inicio(request):
    
    return render(request, "AppCoder/inicio.html")
def viaje(request):
    
    return render(request, "AppCoder/viajes.html")

def libro(request):
    
    return render(request, "AppCoder/libros.html")

def actividad(request):
    
    return render(request, "AppCoder/actividades.html")
def curso(request):
    
    return render(request, "AppCoder/cursos.html")

def acerca_de_mi(request):
    
    return render(request, "AppCoder/about.html")

def busquedaNombreV(request):
    
    return render(request, "AppCoder/inicio.html")    
    
def resultados(request):
    
    if request.GET["nombre"]:
        
        nombre=request.GET["nombre"]
        viajes = Viaje.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppCoder/inicio.html", {"viajes":viajes, "nombre":nombre})
    
    else:
        
        respuesta= "No enviaste datos."
        
    
    return HttpResponse(respuesta)

def busquedaNombreL(request):
    
    return render(request, "AppCoder/inicio.html")    
    
def resultadosL(request):
    
    if request.GET["nombre"]:
        
        nombre=request.GET["nombre"]
        libros = Libro.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppCoder/inicio.html", {"libros":libros, "nombre":nombre})
    
    else:
        
        respuesta= "No enviaste datos."

    return HttpResponse(respuesta)

def busquedaNombreC(request):
    
    return render(request, "AppCoder/inicio.html")    
    
def resultadosC(request):
    
    if request.GET["nombre"]:
        
        nombre=request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "nombre":nombre})
    
    else:
        
        respuesta= "No enviaste datos."
        
    
    return HttpResponse(respuesta)

def busquedaNombreAF(request):
    
    return render(request, "AppCoder/inicio.html")    
    
def resultadosAF(request):
    
    if request.GET["nombre"]:
        
        nombre=request.GET["nombre"]
        actividades = Actividad.objects.filter(nombre__iexact=nombre)
        
        return render(request, "AppCoder/inicio.html", {"actividades":actividades, "nombre":nombre})
    
    else:
        
        respuesta= "No enviaste datos."
        
    
    return HttpResponse(respuesta)

#CRUD de viajes

class ListaViaje(LoginRequiredMixin, ListView):
    
    model = Viaje

class DetalleViaje(LoginRequiredMixin, DetailView):
    
    model = Viaje
    
class CrearViaje(LoginRequiredMixin, CreateView):

    model = Viaje
    success_url = "/AppCoder/viaje/list"
    fields = ["nombre", "duracion"]
    
class ActualizarViaje(LoginRequiredMixin, UpdateView):
    
    model = Viaje
    success_url = "/AppCoder/viaje/list"
    fields = ["nombre", "duracion"]
    
class BorrarViaje(LoginRequiredMixin, DeleteView):
    
    model = Viaje
    success_url = "/AppCoder/viaje/list"
    
#CRUD de libros
class ListaLibro(LoginRequiredMixin, ListView):
    
    model = Libro

class DetalleLibro(LoginRequiredMixin, DetailView):
    
    model = Libro
    
class CrearLibro(LoginRequiredMixin, CreateView):

    model = Libro
    success_url = "/AppCoder/libro/list"
    fields = ["nombre", "autor"]
    
class ActualizarLibro(LoginRequiredMixin, UpdateView):
    
    model = Libro
    success_url = "/AppCoder/libro/list"
    fields = ["nombre", "autor"]
    
class BorrarLibro(LoginRequiredMixin, DeleteView):
    
    model = Libro
    success_url = "/AppCoder/libro/list"
    
#CRUD de actividades fisicas
class ListaActividad(LoginRequiredMixin, ListView):
    
    model = Actividad

class DetalleActividad(LoginRequiredMixin, DetailView):
    
    model = Actividad
    
class CrearActividad(LoginRequiredMixin, CreateView):

    model = Actividad
    success_url = "/AppCoder/actividad/list"
    fields = ["nombre", "frecuencia"]
    
class ActualizarActividad(LoginRequiredMixin, UpdateView):
    
    model = Actividad
    success_url = "/AppCoder/actividad/list"
    fields = ["nombre", "frecuencia"]
    
class BorrarActividad(LoginRequiredMixin, DeleteView):
    
    model = Actividad
    success_url = "/AppCoder/actividad/list"
    
#CRUD de cursos
class ListaCurso(LoginRequiredMixin, ListView):
    
    model = Curso

class DetalleCurso(LoginRequiredMixin, DetailView):
    
    model = Curso
    
class CrearCurso(LoginRequiredMixin, CreateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "docente"]
    
class ActualizarCurso(LoginRequiredMixin, UpdateView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "docente"]
    
class BorrarCurso(LoginRequiredMixin, DeleteView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    
    