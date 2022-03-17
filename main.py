import os
import sys
import Funciones.funciones_estudiante as funciones_student
import Funciones.funciones_curso as funciones_cursos

datos_archivo_students = open("BBD_student/students.txt", mode="r+", encoding="UTF-8")
student_data = datos_archivo_students.read()
student_data = [student_data] #Los almacenamos en una lista
datos_archivo_students.close()

datos_archivo_subjects = open("BBD_student/subjects.txt", mode="r+", encoding="UTF-8")
subjects_data = datos_archivo_subjects.read()
subjects_data = [subjects_data]
datos_archivo_subjects.close()

msg_principal_menu = "\nPrograma de control de estuidantes y cursos de la Universidad"
msg_secun_estudiantes = "\nHas selecionado la opcion de Estudiantes, ahora seleciona que deseas hacer, marcando el número correspondiente"
msg_secun_cursos = "\nHas selecionado la opcion de Cursos, ahora seleciona que deseas hacer, marcando el número correspondiente"
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

list_cursos_record = ["Fisica mecanica", "Informatica",
                      "Calculo diferencial", "Algebra y trigonometria",
                      "Teoria de la información", "Circuitos"]

Iniciar = True
Menu_Inicial = True
Menu_secund_students = False #Estudantes
Menu_secund_cursos = False #Cursos
Modificado = False # Archivo modificado.

Verificacion = 0

def Menu_Principal():
    "Me imprime el menu principal del programa, ademas le pide una opción para verificarla en la respectiva función"
    os.system("clear")
    
    global opciones_list_1, msg_selecion_opcion
    
    print(msg_principal_menu, end="\n")
    print("Menu principal")
    for objeto_list in opciones_list_principal:
        print (objeto_list)
    selection_user = input(msg_selecion_opcion)
    return selection_user

def Menu_Estudiantes():
    "Muestra las opciones de estudiantes, ademas le pide un dato para realizar la respectiva verificación"
    
    print("\n")
    global opciones_list_estudiantes, msg_secun_estudiantes, msg_selecion_opcion

    print(msg_secun_estudiantes, end="\n")
    for objeto_list in opciones_list_estudiantes:
        print(objeto_list)
    selection_user_2 = input(msg_selecion_opcion)
    return selection_user_2

def Menu_Cursos():
    "Imprime las opciones de curso, ademas le pide que selecciones una opción, para realizar la respectiva verficación."
    
    global opciones_list_cursos, msg_secun_cursos, msg_selecion_opcion
    
    print(msg_secun_cursos, end="\n")
    for objeto_list in opciones_list_cursos:
        print (objeto_list)
    selection_user_2 = input(msg_selecion_opcion)
    return selection_user_2

def Cerrar_Programa_Guardar(new_data_student):
    "Ivocamos esta funcion una vez se finalice la ejecución del programa para guardar los cambios realizados en los archivos"
    
    datos_archivo_students = open("BBD_student/students.txt", mode="w", encoding="UTF-8")
    new_data_student_string = new_data_student[0]
    datos_archivo_students.write(new_data_student_string)
    datos_archivo_students.close()

def Crear_new_data_subjects (data_subjects_concatenada):
    datos_archivo_subjects = open("BBD_student/subjects.txt", mode="a", encoding="UTF-8")
    datos_archivo_subjects.write(data_subjects_concatenada)
    datos_archivo_subjects.close()

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
        if ciclo > 5:
            print("Intentalo en otra ocasión")
            condicional = False
            option_user_rst = False
            #break
        
        #El ultimo if se movio una indexación a la izquierda, ya que al presionar una opción correcta en el ultimo intento me sacaba del programa, estamos obligando a esta verificación la haga si el # ciclo sea mayor a 5.      
    return option_user_rst

def Establecer_Opcion_Principal (opcion):
    ""
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


#Esta funcion añade estudiantes, retorna dos valores, cedula y nombre, una vez ralizada la comprobacion de los datos ingresados.
def Verificacion_Identificacion (Identificacion):
    os.system("clear")
    
    Iniciar = True
    ciclo = 0
    New_Identificacion = Identificacion
    
    while Iniciar == True:
        ciclo += 1
        Condicional = New_Identificacion.isdigit()
        aux_len = len(Identificacion)
        
        if aux_len == 8 or aux_len == 10: #Estamos verificando dentro de los criterios de identificación colombiana.
            if Condicional == True:
                New_Identificacion = int(Identificacion)
                Iniciar = False
        else:
            os.system("clear")
            Instruciones = "Debes ingresar solamente números, los cuales pueden ser igual a una logitud de 8 o 10, tienes hasta 5 intentos."
            print(Instruciones)
            New_Identificacion = input("Te haz equivocado porfavor ingresa el número de cedula correcto ")
            if ciclo >= 5:
                Iniciar = False
                break

    return Condicional, (New_Identificacion) #la identificación la retornamos en string, para concatenar.

def Verificacion_Nombre (Nombre):
    os.system("clear")
    Iniciar = True
    ciclo = 0
    Condicional = False
    
    while Iniciar == True:
        New_Nombre = Nombre.title() #Convertimos a nombre propio.
        aux_len = len(Nombre) #Determinamos la cantidad de caracteres.
        
        for caracter in New_Nombre: #Verifica si el string tiene números.
            aux_verificacion_num = caracter.isdigit()
            if aux_verificacion_num == True:
                aux_len = 121 #Modificamos esta variable para que salte al else.
                break
        
        if aux_len < 120: #Estamos verificando que name sea menor a 120.
            while Iniciar == True: #Estamos verificando que un caracter no este más de 7 veces en el string.
                for caracter in New_Nombre:
                    aux_contador = New_Nombre.count(caracter)
                    if aux_contador >= 7:
                        Condicional = False
                        Iniciar = False
                        break
                Condicional = True
                Iniciar = False
        else:
            os.system("clear")

            Instruciones = "Debes ingresar solamente letras, tienes una logitud de 120 caracteres incluyendo espacios, tienes hasta 5 intentos."
            print(Instruciones)
            New_Nombre = input("Ingresa otra vez el nombre de tu estudiante, te haz equivocado de acuerdo a las intruciones dadas.")
            if ciclo  >= 5:
                Condicional = False
                Iniciar = False

    return Condicional, New_Nombre

#Apartir de aqui inicia la ejecución principal del programa.
while Iniciar == True:
    
    if Menu_Inicial == True: #Menu principal del programa.
        selection_user = Menu_Principal()
        selection_user = Opcion_user(selection_user, opciones_list_principal)
        if selection_user == False:
            Iniciar = False
            break
        else:
            Menu_Inicial, Menu_secund_students, Menu_secund_cursos, Iniciar = Establecer_Opcion_Principal(selection_user)
            #Estamos definiendo que opcion eligio el usuario, y de acuerdo a eso, asignar los valores pertinentes.
    #Menu Estudiantes.
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
                name_student = input ("Ingresa el nombre del estudiante: ")
                num_identificacion = input ("Ingresa el número de identificación: ")
                
                #Verificar si cumplen con los criterio.
                V_1, Identificacion = Verificacion_Identificacion(num_identificacion) #Verificamos si el número es correcto.
                V_2, Nombre = Verificacion_Nombre(name_student) #Verificamos si el nombre es correcto y lo retornamos con valores de Nom_propio.
                
                if V_1 == True and V_2 == True:
                    #Invocar la funcion que añade al archivo de texto dichos datos.
                    new_data_student = funciones_student.add_student(Identificacion, Nombre, student_data) #Retorna una lista con el nuevo dato a ingresar.
                    Modificado = True

                    if Modificado == True:
                        Cerrar_Programa_Guardar(new_data_student)
                    
                elif V_1 == True and V_2 == False:
                    print ("Te equivocates al momento de ingresar el nombre del usuario, vuelve y selecciona otra vez opción")
                    
                elif V_1 == False and V_2 == True:
                    print ("Te equivocaste al momento de ingresar el número de identificación, vuelve y selecciona otra vez la opción")
                else:
                    Menu_Inicial = False
                    Menu_secund_students = False
                    Menu_secund_cursos = False

            elif Verificacion == 2: #Matricular un estudiante en un curso.                
                #Llamamos a la funcion que imprime el menu de cursos.
                selection_user = Menu_Curso_Record(list_cursos)
                
                #Imprimimos list_cursos, y pedimos una opcion.
                selection_user = Opcion_user(selection_user, list_cursos) #Verificamos.
                
                if selection_user == False:
                    print ("Te haz equivocado al selecionar una opción, porfavor vuelvelo a intentar en otro momento")
                else:
                    opcion_select_curso = list_cursos_record[selection_user-1] #Estamos segmentado y seleccionando la opcion del usuario.                    
                #Le pedimos el número de identificación para buscarlos en la base de datos student.txt, si esta se añade el estudiante a dicho curso invocando la funcion pertinente.
                #Si no esta le preguntamos si desea añadir dicha identificación a la base de datos, forzando el valor de Verificación = 1, para que así proceda otra vez a realizar este paso.
                
                #Le pedimos al usuario el numero de identificación.
                num_identificacion = input("Vamos a buscar al estudiante, por favor, ingresa el número de identificación del estudiante ")
                
                Condicional = Verificacion_Identificacion(num_identificacion)
                
                #Verificamos si el número de identificación esta en la base de datos.
                if Condicional == True:
                    Verificacion_SI_NO = funciones_student.Verificacion_Identificacion_BBD(num_identificacion)
                    if Verificacion_SI_NO == True: #Indica que si se encontro el número ingresado
                        funciones_student.Matricular_student_curso(opcion_select_curso, num_identificacion)
                else:
                    aux_elecion_user = Si_No()
                    aux_elecion_user = Opcion_user(aux_elecion_user, ["Si", "No"])
                    if aux_elecion_user == False:
                        print("Te haz equivocado, por favor sigue las intruciones la proxima vez, vuelvelo a intentar más tarde")
                    elif aux_elecion_user == 1:
                        Verificacion = 1
                    elif aux_elecion_user == 2:
                        print("Ok, vuelvelo a intentar en otra ocasión")
                    
                
            elif Verificacion == 3:  # Mostrar todos los estudiantes registrados.
                #Invocamos la fucion que muestra los estudiantes registrados en la base de datos.
                Lista_Estudiantes = funciones_student.Obtener_Name_Student(student_data)
                ciclo = 1
                print ("\n")
                print ("Estos son todos los estudiantes que se tienen registrados en la base de Datos.")
                for name_student in Lista_Estudiantes:
                    print(ciclo, name_student, end="")
                    ciclo += 1

            elif Verificacion == 4:  # Consultar promedio de estudiantes.
                #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.

                #Le pedimos al usuario el numero de identificación.
                num_identificacion = input("Vamos a buscar al estudiante, por favor, ingresa el número de identificación del estudiante ")

                Condicional = Verificacion_Identificacion(num_identificacion)
                
                if Condicional == True:
                    Si_No_Econtrado = funciones_student.Consultar_promedio_student(num_identificacion)
                    print(Si_No_Econtrado)
                else:
                    print("El número ingresado no se econtro dentro de la base de datos, intenta registrarlo, seleccionado la opcion pertinente")
                
            elif Verificacion == 5:  # Matricular un estudiante en un curso.
                #Le pedimos los datos, los verificamos, y le preguntamos donde quiere registrar al estudiante.
                
                #Le pedimos los datos.
                num_identificacion = input("Ingresa el número de identificación ")
                
                #Los buscamos en la base de datos.
                Si_No_Econtrado = funciones_student.Verificacion_Identificacion_BBD(num_identificacion)
                
                #Verificamos y evaluamos.
                if Si_No_Econtrado == True:
                    print("")
                else:
                    print("El número de identifición ingresado es incorrecto, vuelvelo a intentar nuevamente.")
            elif Verificacion == 6: #Regresa al menu principal, cambiando los valores pertinentes, "Retroceder"
                Menu_Inicial = True
                Menu_secund_students = False
                Menu_secund_cursos = False
            else:
                Menu_Inicial = False
                Menu_secund_students = False
                Menu_secund_cursos = False
    
    #Menu de cursos.
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
                
                #la funcion pide datos y verica retornando sus respectivo valores.
                Condicional, Num_creditos, Name_curso, Num_notas = funciones_cursos.Verificacion_Add_Curso()
                
                if Condicional == True:
                    #Concatenamos los datos ingresados por el usuario.
                    subjects_data_concatenada = funciones_cursos.Concatenacion_Data(Num_creditos, Name_curso, Num_notas)
                                        
                    #Estamos llamando a la función para añadir la nueva data con los datos ingresados por el usuario.
                    Crear_new_data_subjects(subjects_data_concatenada)
                else:
                    print("No se pudo añadir el curso, hubo un error.")
                
            elif Verificacion == 2:  # Mostrar todos los cursos registrados.
                Lista_Cursos = funciones_cursos.Obtener_Cursos(subjects_data)
                ciclo = 1
                print("\n")
                print("Estos son todos los cursos registrados hasta momento.")
                for name_curso in Lista_Cursos:
                    print (ciclo, name_curso, end="")
                    ciclo += 1

            elif Verificacion == 3:  # Consultar estudiantes matriculados en un curso.
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                print()

            elif Verificacion == 4:  #Porcentaje de estudiantes que gano y perdio un curso.
            #elif Verificacion == opciones_list_estudiantes[Verificacion -1]
                print()

            elif Verificacion == 5:  # Regresa al menu principal, cambiando los valores pertinentes, "Retroceder"
                Menu_Inicial = True
                Menu_secund_students = False
                Menu_secund_cursos = False
            else:
                Menu_Inicial = False
                Menu_secund_students = False
                Menu_secund_cursos = False
        
    else:
        Iniciar = False
        Menu_secund_students = False
        Menu_secund_cursos = False