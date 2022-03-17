"""
En este archivo crearemos funciones que impliquen; las consulta de información de los arhivos.
-->>Crear nuevo curso;

-->>Mostrar todos los cursos registrados;

-->>Consultar estudiantes matriculados en un curso;

-->>Porcentaje de estudiantes que gano y perdio un curso;
"""

def Obtener_Cursos(datos_subjects):
    lista_cursos = []
    convert_string = datos_subjects[0]
    new_list_data_subjects = convert_string.split("\n\n")
    for curso in new_list_data_subjects:
        name_curso = curso.split(";", 1)
        name_curso = name_curso[0] + "\n"
        name_curso = [name_curso]
        lista_cursos += name_curso
    return lista_cursos

def Verificacion_Add_Curso ():
    Instrucciones = "Te haz equivocado, no seguistes las instrucionesm intentanlo en otra ocación."
    check_creditos = False
    check_name = False
    check_notas = False
    Condicional = "" 
    rst_num_creditos = "" 
    rst_name = ""
    rst_num_notas = ""
    
    
    while check_creditos == False: #Pedimos y verificamos retornando su valor junto con una condicional.
        def V_num_creditos ():
            global Condicional, rst_num_creditos, rst_name, rst_num_notas
            print("\nInstrucciones; Debes ingresar un número menor a 5 y de una logitud de 1, nada de letras o caracteres especiales.")
            Num_creditos = input("Ingrese el número de creditos del curso: ")
            
            if int(Num_creditos) <= 5:
                return True, Num_creditos
            else:
                return False, Num_creditos
        
        condicional_creditos, rst_num_creditos = V_num_creditos()
        
        if condicional_creditos == True:
            check_creditos = True
        else:
            print(Instrucciones)
            break
            
    while check_name == False: #Verificamos nombe, pedimos y retornamos.
        def V_name_curso ():
            global Condicional, rst_num_creditos, rst_name, rst_num_notas
            print("\nInstrucciones; Debes ingresar solo letras, nada de números, la longitud debe ser <= a 120")
            name_curso = input("Ingrese el nombre del curso: ")

            for caracter in name_curso:
                aux_verificacion_num = caracter.isdigit()
                if aux_verificacion_num == True:
                    return False, name_curso
                    break
            if len(name_curso) <= 120:
                return True, name_curso
            else:
                return False, name_curso
        condicional_name, rst_name = V_name_curso()

        if condicional_name == True:
            check_name = True
        else:
            print(Instrucciones)
            break
    while check_notas == False: #Verificamos notas, pedimos y retornamos.
        def V_num_notas ():
            global Condicional, rst_num_creditos, rst_name, rst_num_notas
            print("\nInstruciones; Debes ingresar solo números, el numero no puede ser mayor a 6, la logitud debe ser de 1")
            Num_notas = input("Ingrese el número de notas que tendra el curso: ")
            if int(Num_notas) <= 6:
                return True, Num_notas
            else:
                return False, Num_notas
        condicional_notas, rst_num_notas = V_num_notas()

        if condicional_notas == True:
            check_notas = True
        else:
            print(Instrucciones)
            break
    if check_creditos == True and check_name == True and check_notas:
        Condicional = True
    else:
        Condicional = False

    return Condicional, rst_num_creditos, rst_name, rst_num_notas

def Concatenacion_Data (Num_Creditos, Name_curso, Num_notas):
    "Utilizamos esta función para concatenar los datos ingresados por el usuario, en cuanto a añadir cursos se deba."
    resul_concatenacion = (str(Name_curso) + ";" + str(Num_Creditos) + ";" + str(Num_notas) + "\n" )
    return resul_concatenacion
