#Este documento incluye el arhivo principal del programa.
"""
Este archivo contendra diferentes funciones; Menu, Dato_CC_Verificacion, Add_Curso

-->> Menu; La utilizaremos mostrar en pantalla las opciones que se le ofrecera al usuario, dentro de las cuales estan; Estudiantes, Curso, Salir.
    ->Dentro de estas ofreceremos las diferentes opciones dentro de las cuales destacamos la de retroceder, el cual volvera a invocar la función menu.
    
    -->>Estudiante; Cargaremos las siguientes opciones asociandolas a sus respectivas funciones.
        -->Matricular estudiante en un curso;
            ->Invocaremos la función que le pedira los respectivos datos, cedula, realizando con anterioridad la respectiva verificación, asociandolas a los objetos de la funcion.
            ¡Cabe resaltar que debemos verificar si este valor ingresado por el usuario, se encuentra dentro de la base de datos de estudiantes, si es así, asociamos el nombre a una variable!
        -->Mostrar todos los estudiantes registrados;
            ->La funcion desarrollara su procedimiento por si sola.
        -->Consultar pomedio de estudiante.
            ->Invocaremos la funcion que le pedira los datos respectivos, realizando la respectiva verificación.
        -->Consultar materias matriculadas por un estudiante;
            Volveremos a invocar funcion que pide los datos (cedula) y los verifica.
            
    -->>Curso; Cargaremos las siguientes opciones asociandolas a sus respectivas funciones.
        -->Crear nuevo curso; 
            ->Invocaremos a la variable Add_Curso, la cual nos pedira el nombre del curso y el numero de creditos, e invocaremos a la respectiva funcion pasandoles los paramentros obtenidos de la funcion Add_Curso
        -->Mostrar todos los cursos registrados;
            ->Invocaremos la funcion pertinente, mostrando los resultados.
        -->Consultar estudiantes matriculados en un curso;
            ->Le pedimos al usuario que seleccione una opcion, deplegamos una lista con con los cursos, e invocamos la funcion pertinente con el valor asociado al curso.
        -->Porcentaje de estudiantes que gano y perdio un curso;
            ->Invocamos la función pertinente y retornamos los datos.
    -->>Salir; Salimos del programa.
    
    ¡Cuando etramos dentro de una de estas opciones nos cargara la opcion de retroceder, invocando nuevamente la funcion Menu!
    
-->>Dato_CC_Verificacion; Esta funcion le pedira al usuario un numero de cédula y rornara el nombre asociado a ese numero.
Si es correcto retornara el valor asociado a ese número.
Si no es así le volvera a pedir otro dato hasta un numero maximo de tres intento, cuando finalice estos tres intentos retornara "None", y volvera al menu principal.

-->>Add_Curso; Le pedira dos datos, Nombre del curso y numero de creditos.

Cabe resaltar que esta funciones estaran dentro de la funcion menu. 
"""
from curses.ascii import isdigit
import imp


import os
import Funciones.funciones_estudiante
import Funciones.funciones_curso

msg_principal_menu = "Seleciona una de las siguientes opciones, marcando el número correspodiente." #Aqui almacenaremos información referente a la ejecución del programa.
msg_secun_estudiantes = "Has selecionado la opcion de Estudiantes, ahora seleciona que deseas hacer, marcando el número correspondiente"
msg_secun_cursos = "Has selecionado la opcion de Cursos, ahora seleciona que deseas hacer, marcando el número correspondiente"

def Iniciar():       
    #Funcion que busca el valor de la cedula ingresada, verifica y retorna el valor asociado.
    def Dato_CC_Verificacion (nombre_user):
        
        return()
    
    #Esta funcion nos retorna el nombre del curso y creditos
    def Add_Curso(Nom_curso, Num_creditos):
        Num_creditos = input()
        
        while Num_creditos.isdigit() == True:
            
        
        if Num_creditos >= 1 and Num_creditos <= 7:
            return (Num_creditos)
        else:
            while isdigit.
                aux = input(("El número de creditos añadidos se encuentra fuera de rango"))
        if len(Nom_curso) <= 20:
            
            Nom_curso
        return(Nom_curso, Num_creditos)
    
    def Add_studen():
        return()
    
    #############################################################
    #Cargamos el menu principal mostrando las siguientes opciones.
    #############################################################
    def Menu_Principal ():
        #Definimos las variables
        global Add_Curso, Dato_CC_Verificacion
        global msg_principal_menu, msg_secun_cursos
        
        def Imprime_Lists(list):
            for objeto_list in list:
                return print(objeto_list)

        opciones_list_menu = ["Estudiantes", "Cursos", "Salir",]
        print(msg_principal_menu, end="\n")
        print("Menu principal")
        print(Imprime_Lists(opciones_list_menu))
        #print("Estudiantes; --> 1\n", "Cursos; --> 2\n", "Salir; --> 3\n")
        
        #Le pedimos al usuario que ingrese una opcion y verificamos.
        selection_user = input("Seleciona una opción marcando el número correspondiente: ")
        Verificacion = Opcion_user(selection_user)

        def Opcion_user(selection_user):
            """
            Esta funcion nos permitira establecer que la opcion seleccionada por el usuario sea correcta, verificando si el dato ingresado por el usuario es un numero o string, debe cumplir la condicion, donde su logitud == 1.
            Ademas definimos un limite de intentos, finalizando con la ejecución del programa.
            """
            ciclo = 0
            if len(selection_user) == 1:
                while selection_user.isdigit() == False:
                    if selection_user.isdigit() == False:
                        ciclo += 1
                        option_user_rst = input("Seleciona una opción marcando el número correspondiente: ") #Verificar si hay error de reasignacion de variable.
                        if ciclo > 3:
                            print("Haz ingresado más de 3 opciones, intentalo en otra ocasión")
                            #break
                            os.system("exit") #Sino funciona, llamemos a la funcio salir, tenemos que mover el codigo al final.
                option_user_rst = int(selection_user)
                return(option_user_rst)
            else:
                selection_user = input("Te haz equivocado, haz ingresado más de un caracter, vuelve a intentarlo") #Verificar si hay error por asignar un nuevo valor a la variable de entrada de la funcion.

        if selection_user == 1:
            def Menu_secun_estudiantes():
                #Imprimios el menu de esta funcion.
                selection_user_2 = 0
                os.system("clear")
                opciones_list_estudiantes = ["Agregar estudiante; -->> 1", "Matricular estudiante en un curso--> 2", "Mostrar todos los estudiantes registrados; -->> 3", "Consultar promedio de estudiante; -->> 4", "Consultar materias matriculadas por un estudiante; -->> 5", "Retroceder; -->> 6"]
                print(msg_secun_estudiantes, end="\n")
                print(opciones_list_menu[selection_user - 1])
                #""" Hicimos uso de for, para imprimir esto, menos codigo.
                #print("Agregar estudiante; -->> 1\n", "Matricular estudiante en un curso--> 2\n", "Mostrar todos #los estudiantes registrados; -->> 3\n", "Consultar promedio de estudiante; -->> 4\n", "Consultar #materias matriculadas por un estudiante; -->> 5\n") #Este codigo tambien lo podemos representar, #con un for, una lista, e imprimiendo cada elemento que recorre el for en la lista, o mucho mejor en #una funcion que reciba la lista.
                #""" 
                print(Imprime_Lists(opciones_list_estudiantes), end="\n")
                
                #Le pedimos al usuario que ingrese una opcion y verificamos.
                selection_user_2 = input("Seleciona una opción marcando el número correspondiente: ")
                Verificacion = Opcion_user(selection_user_2)
                
                #Comprobación e invocación de las funciones externas al archivo.
                if Verificacion == 1: #Agregar estudiante.
                    #Le pedimos los datos.
                    
                    #Verificar si cumplen con los criterio.
                    
                    #Invocar la funcion que añade al archivo de texto dichos datos.
                    Add_studen()
                    
                elif Verificacion == 2: #Matricular un estudiante en un curso.
                    #Le pedimos los datos.
                    
                    #Verificamos si cumplen con los criterios.
                    
                    #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                    Add_studen()
                    
                elif Verificacion == 3:  # Mostrar todos los estudiantes registrados.
                    #Invocamos la fucion que muestra los estudiantes registrados en la base de datos.
                    Add_studen()
                    
                elif Verificacion == 4:  # Consultar promedio de estudiantes.
                    #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                    Add_studen()

                elif Verificacion == 5:  # Matricular un estudiante en un curso.
                    #Le pedimos los datos.

                    #Verificamos si cumplen con los criterios.

                    #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                    Add_studen()
                
                elif Verificacion == 6:  # Matricular un estudiante en un curso.
                    #Le pedimos los datos.

                    #Verificamos si cumplen con los criterios.

                    #Invocamos la fucion que matricula al estudiante, añadiendolo en la base de datos.
                    Add_studen()

                
                    
                return()
            
            Menu_secun_estudiantes()#Invocamos a la funcion
        elif selection_user == 2:
            def Menu_secun_cursos(args):
                return()
            
            Menu_secun_cursos()#Invocamos a la funcion
        else:
            def Salir(args):
                return()
        
        
print(Iniciar())