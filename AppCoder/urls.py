"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="Inicio"), #path, vista, nombre
    path("about/", acerca_de_mi, name="About"),
    path('login/', InicioSesion, name="Login"),
    path('register/', registro, name="SignUp"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar_avatar/", agregarAvatar, name="Avatar"),
    

    
    #viajes
    path('viajes/', viaje, name="Viaje"),
    path('buscarNombreV/', busquedaNombreV, name="BuscarNombreV"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
    
    #libros
    path('libros/', libro, name="Libro"),
    path('buscarNombreL/', busquedaNombreL, name="BuscarNombreL"),
    path('resultadosL/', resultadosL, name="ResultadosLibros"),
    
    #actividades fisicas
    path('actividades/', actividad, name="Actividad"),
    path('buscarNombreAF/', busquedaNombreAF, name="BuscarNombreAF"),
    path('resultadosAF/', resultadosAF, name="ResultadosActividades"),


    
    #cursos
    path('cursos/', curso, name="Curso"),
    path('buscarNombreC/', busquedaNombreC, name="BuscarNombreC"),
    path('resultadosC/', resultadosC, name="ResultadosCursos"),
    
    
    #CRUD de viajes usando clases
    path('viaje/list/', ListaViaje.as_view(), name="ViajesLeer"),
    path('viaje/<int:pk>/', DetalleViaje.as_view(), name="ViajesDetalle"),
    path('viaje/crear/', CrearViaje.as_view(), name="ViajesCrear"),
    path('viaje/borrar/<int:pk>/', BorrarViaje.as_view(), name="ViajesBorrar"),
    path('viaje/editar/<int:pk>/', ActualizarViaje.as_view(), name="ViajesEditar"),
    
        
    #CRUD de libros usando clases
    path('libro/list/', ListaLibro.as_view(), name="LibrosLeer"),
    path('libro/<int:pk>/', DetalleLibro.as_view(), name="LibrosDetalle"),
    path('libro/crear/', CrearLibro.as_view(), name="LibrosCrear"),
    path('libro/borrar/<int:pk>/', BorrarLibro.as_view(), name="LibrosBorrar"),
    path('libro/editar/<int:pk>/', ActualizarLibro.as_view(), name="LibrosEditar"),
    
    #CRUD de actividades fisicas usando clases
    path('actividad/list/', ListaActividad.as_view(), name="ActividadesLeer"),
    path('actividad/<int:pk>/', DetalleActividad.as_view(), name="ActividadesDetalle"),
    path('actividad/crear/', CrearActividad.as_view(), name="ActividadesCrear"),
    path('actividad/borrar/<int:pk>/', BorrarActividad.as_view(), name="ActividadesBorrar"),
    path('actividad/editar/<int:pk>/', ActualizarActividad.as_view(), name="ActividadesEditar"),
    
    #CRUD de actividades fisicas usando clases
    path('curso/list/', ListaCurso.as_view(), name="CursosLeer"),
    path('curso/<int:pk>/', DetalleCurso.as_view(), name="CursosDetalle"),
    path('curso/crear/', CrearCurso.as_view(), name="CursosCrear"),
    path('curso/borrar/<int:pk>/', BorrarCurso.as_view(), name="CursosBorrar"),
    path('curso/editar/<int:pk>/', ActualizarCurso.as_view(), name="CursosEditar"),

]
