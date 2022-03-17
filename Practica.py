x = open("BBD_student/subjects.txt", mode="r", encoding="UTF-8")
t = x.read()
datos_subjects = [t]
#print (datos_subjects)
x.close()

x = open("BBD_student/students.txt", mode="r", encoding="UTF-8")
t = x.read()
datos_students = [t]
x.close

#Matricular un estudiantes, buscar en student.txt, si esta tomar esos datos y llevarlos al curso donde desar matricularo, invocando la función que muestra los cursos.



lista_General_Cursos = {}
Student_Identifcacion = []
Curso = ()

