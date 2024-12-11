import re

def validar_nombre (nombre):
    if not nombre.strip():
        return "EL parametro nombre es obligatorio"
    if not all (x.isalpha()or x.isspace()for x in nombre):
        return "El nombre solo debe contener letras y espacios"
    return None

def validar_DNI (DNI):
    if not DNI.isdigit() or len (DNI)!= 8:
        return "El DNI solo debe contener 8 números sin puntos ni comas"
    return None

def validar_mail (mail):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, mail):
        return "El correo electronico es incorrecto"
    return None

def validar_telefono(telefono):
    if not telefono.isdigit() or len (telefono)!= 10:
        return "El telefono debe contener 10 numeros"
    return None

def validar_formulario ():
    print ("Bienvenido aqui va a poder validar su formulario")
nombre = input("Ingrese el nombre completo")
DNI = input("Ingrese el DNI")
mail = input("Ingrese el mail")
telefono = input("ingrese el número telefonico")

errores = []

error_nombre = validar_nombre(nombre)
if error_nombre:
    errores.append(error_nombre)

error_DNI = validar_DNI(DNI)
if error_DNI:
    errores.append(error_DNI)

error_mail = validar_mail
if error_mail:
    errores.append(error_mail)

error_telefono = validar_telefono(telefono)
if error_telefono:
    errores.append(error_telefono)

if errores:
    print("\nErrores encontrados: ")
    for error in errores: 
        print (f"{error}")
    print("\nPorfavor introduzca los datos de forma correcta")
else: print("\nFormulario validado con éxito")

if __name__ == "__main__":
    validar_formulario()
