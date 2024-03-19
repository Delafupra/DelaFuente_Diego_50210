La página se creo usando python y django

#contraseña de admin
Usuario: diego
Contraseña: Python12345

email:diego@diego.com

#URLS principales

    http://127.0.0.1:8000/admin
    http://127.0.0.1:8000/AppCoder
    http://127.0.0.1:8000/AppCoder/inicio
    
#URLS CRUD (En estos urls puedes navergar en todo el CRUD de los 4 modelos mediante links)
    http://127.0.0.1:8000/AppCoder/viaje/list/
    http://127.0.0.1:8000/AppCoder/actividad/list/
    http://127.0.0.1:8000/AppCoder/libro/list/
    http://127.0.0.1:8000/AppCoder/curso/list/
    
    Dentro del path AppCoder/inicio debes poder navegar a los siguientes urls:
   
    path("about/", acerca_de_mi, name="About"),
    path('login/', InicioSesion, name="Login"),
    path('register/', registro, name="SignUp"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar_avatar/", agregarAvatar, name="Avatar"),

    path('viajes/', viaje, name="Viaje"),
    path('libros/', libro, name="Libro"),
    path('actividades/', actividad, name="Actividad"),
    path('cursos/', curso, name="Curso"),

    Igualmente dentro de inicio podrás buscar en los 4 modelos y los resultados te llevarán al inicio

    #viajes
    path('buscarNombreV/', busquedaNombreV, name="BuscarNombreV"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
    #libros
    path('buscarNombreL/', busquedaNombreL, name="BuscarNombreL"),
    path('resultadosL/', resultadosL, name="ResultadosLibros"),
    #actividades fisicas
    path('buscarNombreAF/', busquedaNombreAF, name="BuscarNombreAF"),
    path('resultadosAF/', resultadosAF, name="ResultadosActividades"),
    #cursos
    path('buscarNombreC/', busquedaNombreC, name="BuscarNombreC"),
    path('resultadosC/', resultadosC, name="ResultadosCursos"),
  
  
