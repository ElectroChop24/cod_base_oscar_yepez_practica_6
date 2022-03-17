"""
En este archivo crearemos funciones que impliquen; la modificación de arhivos.
-->>Agregar estudiante;
    Se le pediran al usuario dos tipos de datos, numero de identificación (int), y nombre, verificaremos que los datos.
    
-->>Matricular estudiante en un curso;

-->>Mostrar todos los estudiantes registrados;

-->>Consultar promedio de estudiante;

-->>Consultar materias matriculadas por un estudiante;

-->> Retroceder;
"""

def Obtener_Name_Student(student_data):
    List_students = []
    student_data = student_data[0]
    student_data = student_data.split("\n")
    for name in student_data:
        if len(name.split(";")) == 2:
            name_studen = name.split(";")
            name_studen = name_studen[1] + "\n"
            List_students.append(name_studen)
            List_students = (List_students)
    return List_students

def Verificacion_Identificacion_BBD (Numero_Buscar): #Verificamos si el número de identificación esta, retornando True o False
    return

def add_student (Identificacion, Nombre, Student_data):
    concatenacion_data_user = (str(Identificacion) + ";" + Nombre + "\n")
    
    Student_data = Student_data[0] + concatenacion_data_user
    print("El estudiante se ha añadido sactifactoriamente")
    return [Student_data] #Retornamos a una lista.

def Matricular_student_curso ():
    return


def Consultar_promedio_student (Numero_identificacion):
    return
