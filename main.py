import os
import Funciones.funciones_estudiante
import Funciones.funciones_curso


msg_principal_menu = "Programa de control de estuidantes y cursos de la Universidad"
msg_secun_estudiantes = "Has selecionado la opcion de Estudiantes, ahora seleciona que deseas hacer, marcando el número correspondiente"
msg_secun_cursos = "Has selecionado la opcion de Cursos, ahora seleciona que deseas hacer, marcando el número correspondiente"
msg_selecion_opcion = "Seleciona una de las opciones marcando el número correspondiente en tu teclado: "

opciones_list_principal = ["Estudiantes -->> 1",
                           "Cursos -->> 2",
                           "Salir -->> 3",]

opciones_list_estudiantes = ["Agregar estudiante; -->> 1",
                             "Matricular estudiante en un curso; --> 2",
                             "Mostrar todos los estudiantes registrados; -->> 3",
                             "Consultar promedio de estudiante; -->> 4",
                             "Consultar materias matriculadas por un estudiante; -->> 5",
                             "Retroceder; -->> 6", ]

opciones_list_cursos = ["Crear nuevo curso; -->> 1", 
                        "Mostrar todos los cursos registrados; -->> 2", 
                        "Consultar estudiantes matriculados en un curso; -->> 3",
                        "Porcentaje de estudiantes que ganaron y perdieron un curso; -->> 4",
                        "Retroceder; -->> 5", ]

Iniciar = True
Menu_Inicial = True
Menu_secund_students = False #Estudantes
Menu_secund_cursos = False #Cursos

Verificacion = 0

def Menu_Principal():
    os.system("clear")
    
    global opciones_list_1, msg_selecion_opcion
    
    print(msg_principal_menu, end="\n")
    print("Menu principal")
    for objeto_list in opciones_list_principal:
        print (objeto_list)
    selection_user = input(msg_selecion_opcion)
    return selection_user

def Menu_Estudiantes():
    os.system("clear")

    global opciones_list_estudiantes, msg_secun_estudiantes, msg_selecion_opcion

    print(msg_secun_estudiantes, end="\n")
    for objeto_list in opciones_list_estudiantes:
        print(objeto_list)
    selection_user_2 = input(msg_selecion_opcion)
    return selection_user_2

def Menu_Cursos():
    os.system("clear")
    
    global opciones_list_cursos, msg_secun_cursos, msg_selecion_opcion
    
    print(msg_secun_cursos, end="\n")
    for objeto_list in opciones_list_cursos:
        print (objeto_list)
    selection_user_2 = input(msg_selecion_opcion)
    return selection_user_2

def Opcion_user(selection_user, range): #Verifica la opcion selecionada por el usuario, determinando si es un string o int, y que no supere len, 1.
    """
    #Esta funcion nos permitira establecer que la opcion seleccionada por el usuario sea correcta, verificando si el dato ingresado por el usuario es un numero o string, debe cumplir la condicion, donde su logitud == 1.
    #Ademas definimos un limite de intentos, finalizando con la ejecución del programa.
    #Evaluamos si se cumple las condiciones, establecidas; El valor ingresado es igual a una logitud de 1, que su valor sea un numero, que este dentro del rango o que el valor ingresado sea menor o igual a la longitud del rango menos 1.
    #De lo contrario vuelva y pidale otra vez el mismo dato al usuario, si excede el limite se termina la ejeucion del programa.
    """
    
    ciclo = 0
    condicional = True
    option_user_rst = 0
        
    
    while condicional == True:
        aux_1 = selection_user.isdigit() # Si es un numero retorna True de lo contrario False.
        if aux_1 == True:  # Si es un numero lo convierte a un int
            aux_1 = int(selection_user)
        
        if aux_1 > 0 and aux_1 < 9 and selection_user.isdigit() == True and aux_1 <= len(range):
            option_user_rst = int(selection_user)
            condicional = True
            return(option_user_rst)
        else:
            ciclo += 1
            selection_user = input("Te haz equivocado, haz ingresado una opcion incorrecta, vuelve a intentarlo ") #Verificar si hay error por asignar un nuevo valor a la variable de entrada de la funcion.
            if ciclo > 3:
                print("Intentalo en otra ocasión")
                condicional = False
                option_user_rst = False
                #break
    return option_user_rst

def Establecer_Opcion_Principal (opcion):
    global Menu_secund_cursos, Menu_Inicial, Menu_secund_students, Iniciar
    
    x1 = Menu_Inicial
    x2 = Menu_secund_students
    x3 = Menu_secund_cursos
    x4 = Iniciar
    
    if opcion == 1: #Menu_secund_students
        x1 = False
        x2 = True
        x3 = False
        x4 = True
    elif opcion == 2: #Menu_secud_cursos
        x1 = False
        x2 = False
        x3 = True
        x4 = True
    elif opcion == 3: #Salir
        x1 = False
        x2 = False
        x3 = False
        x4 = False
    else:
        print("Hay error detro de la funcion")

    return x1, x2, x3, x4

#Esta funcion verifica si el número esta en la base de datos.
def Numero_Verificacion_BBD(nombre_user):
    return()

#Esta funcion nos retorna el nombre del curso y número de creditos, una vez realizada la comprobacion de los datos ingresados.
def Add_Curso(Nom_curso, Num_creditos):
    
    return(Nom_curso, Num_creditos)

#Esta funcion añade estudiantes, retorna dos valores, cedula y nombre, una vez ralizada la comprobacion de los datos ingresados.
def Add_students (Cedula, Nombre):

    return()

while Iniciar == True:
    
    if Menu_Inicial == True: #Menu principal del programa.
        selection_user = Menu_Principal()
        selection_user = Opcion_user(selection_user, opciones_list_principal)
        if selection_user == False:
            Iniciar = False
            break
        else:
            Menu_Inicial, Menu_secund_students, Menu_secund_cursos, Iniciar = Establecer_Opcion_Principal(selection_user)            
        
    elif Menu_secund_students == True:
        while Menu_secund_students == True:
            #Inicialmente imprimimos el menu que corresponde a esta opcion.
            selection_user = Menu_Estudiantes()
            selection_user = Opcion_user(selection_user, opciones_list_estudiantes)
            if selection_user == False:
                Iniciar = False
                break
            else:
                Verificacion = selection_user

            #Comprobación e invocación de las funciones externas al archivo.
            if Verificacion == 1: #Agregar estudiante.
                #Le pedimos los datos.
                Identificacion_student = Num_Identificacion()
                Nombre_student = Name_student()
                #Verificar si cumplen con los criterio.
                
                #Invocar la funcion que añade al archivo de texto dichos datos.
                Add_students(Identificacion_student, Nombre_student)
                
            elif Verificacion == 2: #Matricular un estudiante en un curso.
                #Le pedimos los datos.
                
                #Verificamos si cumplen con los criterios.
                
                #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                Add_students()
                
            elif Verificacion == 3:  # Mostrar todos los estudiantes registrados.
                #Invocamos la fucion que muestra los estudiantes registrados en la base de datos.
                Add_students()
                
            elif Verificacion == 4:  # Consultar promedio de estudiantes.
                #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                Add_students()
            elif Verificacion == 5:  # Matricular un estudiante en un curso.
                #Le pedimos los datos.
                #Verificamos si cumplen con los criterios.
                #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                Add_students()
                
            elif Verificacion == 6: #Regresa al menu principal, cambiando los valores pertinentes, "Retroceder"
                Menu_Inicial = True
                Menu_secund_students = False
                Menu_secund_cursos = False
            else:
                Menu_Inicial = False
                Menu_secund_students = False
                Menu_secund_cursos = False
        
    elif Menu_secund_cursos == True:
        while Menu_secund_cursos == True:
            selection_user = Menu_Cursos()
            selection_user = Opcion_user(selection_user, opciones_list_cursos)
            if selection_user == False:
                Iniciar = False
                break
            else:
                Verificacion = selection_user

            #Comprobación e invocación de las funciones externas al archivo.
            if Verificacion == 1:  # Crear nuevo curso
            #if Verificacion == opciones_list_estudiantes[Verificacion -1], podriamos utilizar este codigo, ambos cumplen con su funcion.
               
                Add_students()

            elif Verificacion == 2:  # Mostrar todos los cursos registrados.
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                Add_students()

            elif Verificacion == 3:  # Consultar estudiantes matriculados en un curso.
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                Add_students()

            elif Verificacion == 4:  #Porcentaje de estudiantes que gano y perdio un curso.
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                Add_students()

            elif Verificacion == 5:  # Regresa al menu principal, cambiando los valores pertinentes, "Retroceder"
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                Menu_Inicial = True
                Menu_secund_students = False
                Menu_secund_cursos = False
            else:
                Menu_Inicial = False
                Menu_secund_students = False
                Menu_secund_cursos = False
        
    else:
        Iniciar = False