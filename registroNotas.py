from alumnos import Alumno 
# Lista para almacenar los alumnos registrados
sistemasAlumnos = []

# Variable para el promedio de notas
promedio_notas = 0

# Variable para la suma de notas
suma_notas = 0
# Ciclo principal del programa
print("! Bienvenidos al ingreso de Notas !")
while True:
    print("\nIngrese un comando (R, C, P, S, X):")
    comando = input().upper()

    if comando == "R":
        print("Ingrese los datos del alumno:")
        nombreAlumno = input("Nombre: ")
        apellidoAlumno = input("Apellido: ")
        edadAlumno = input("Edad: ")
        nacionalidadAlumno = input("Nacionalidad: ")
        alumno = Alumno(nombreAlumno, apellidoAlumno, edadAlumno, nacionalidadAlumno)
        sistemasAlumnos.append(alumno)
        print("Alumno registrado exitosamente.")

    elif comando == "C":
        for alumno in sistemasAlumnos:
            while True:
                try:
                    nota = float(input(f"Ingrese la nota del alumno {alumno.nombreAlumno} {alumno.apellidoAlumno}: "))
                    if nota >= 0 and nota <= 20:
                        alumno.notas.append(nota)
                        break
                    else:
                        print("La nota debe estar en un rango de 0 a 20.")
                except ValueError:
                    print("Ingrese un número válido.")

    elif comando == "P":
        total_alumnos = len(sistemasAlumnos)
        if total_alumnos > 0:
            suma_notas = 0
            for alumno in sistemasAlumnos:
                suma_notas += sum(alumno.notas) / total_alumnos
            print(f"El promedio de notas para {total_alumnos} alumnos es: {suma_notas}")
        else:
            print("No hay alumnos registrados.")

    elif comando == "S":
        total_alumnos = len(sistemasAlumnos)
        if total_alumnos > 0:
            suma_notas = 0
            for alumno in sistemasAlumnos:
                suma_notas += sum(alumno.notas)
            print(f"La suma de notas de {total_alumnos} alumnos es: {suma_notas}")
        else:
            print("No hay alumnos registrados.")

    elif comando == "X":
        print("Programa finalizado.")
        break

    else:
        print("Comando no válido. Intente nuevamente.")