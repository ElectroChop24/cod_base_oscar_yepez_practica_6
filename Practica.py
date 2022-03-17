x = open("BBD_student/students.txt", mode="r+", encoding="UTF-8")
t = x.read()
datos_busqueda = [t]
print(t)
x.close()

Identify = "1007439868"
Name = "Oscar Daniel Yepez Amin"

def add_student(Identificacion, Nombre, Student_data):
    # Concatenamos los datos del usuario.
    concatenacion_data = (Identificacion + ";" + Nombre + "\n")
    
    #New_Data_Student = Student_data
    #New_Data_Student.append(concatenacion_data)
    
    Student_data.append(concatenacion_data)
    
    return Student_data

New_resul = add_student(Identify, Name, datos_busqueda)

print(New_resul)


Identify = "1007439900"
Name = "Yeffri Yepez Amin"

New_resul = add_student(Identify, Name, datos_busqueda)

print(New_resul)



identificacion = "1007439868"
Nombre = "Oscar Daniel Yepez Amin"

resultado = ((identificacion + ";" + Nombre + "\n"))
print(resultado, end="")
#print("La logitud del string es de", len(resultado))

#print (datos_busqueda)
def Escribir_Archivo():
    global datos_busqueda, resultado
    x = open("BBD_student/students.txt", mode="w", encoding="UTF-8")
    rst1 = datos_busqueda[0]
    rst1 = (rst1 + resultado)
    t = x.write(rst1)
    x.close()

Escribir_Archivo()

x = open("BBD_student/students.txt", mode="r+", encoding="UTF-8")
t = x.read()
print(t)
x.close()