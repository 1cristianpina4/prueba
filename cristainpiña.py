usuarios = {}
nombre = ""
cantidad = {}

def validador_usuarios(nombre):
    contador_mayuscula=0
    contador_usuarios=0
    for letra in str(nombre):
        if letra.isnumeric():
            contador_mayuscula+=1
            contador_usuarios+=1

    print("****hola buenas****")  
    if contador_usuarios!=2:
        print("tu usuario debe tener una letra en mayuscula")
        return False
    elif contador_mayuscula!=1:
          print("debe tener una mayuscula")
          return False
    elif len(usuarios)!=8:
        print("la clave debe tener 8 caracteres, 1 letra en mayuscula, 1 numero ")
        return False
    else:
        return True
    

def validado_sexo(sexo):
    if sexo!="F" or sexo!="M":
       print("el sexo se debe ingresar como F para femenino y M masculino")
       return False
    else:
        return True
    
def buscarusuarios(usuarios):
    for clave in usuarios:
        if clave==usuarios:
            print("usuario encontrado")
            return usuarios[clave]
        
    return None
opcion = "0"
while opcion!="4":
    print("***menu principal***")
    print("1.-ingrese usuario.")
    print("2.- buscar usuario.")
    print("3.- eliminar uasuario.")
    print("4.- salir.")

    opcion=input("elija la opcion que desea:")

    match opcion:

        case "1":
            while True:
                asuarios=input("ingrese el nombre del usuario:")
                if validador_usuarios==True:
                    print("registro de usuario correcto")
                    usuarios[nombre]=[]
                    break
                else:
                    print("nombre incorrecto vuelva a ingresarlo")
                    if len(nombre):
                        print("el nombre debe tener 1 caracter")
                    else:
                        usuarios[nombre](nombre)
                        break

            while True:
                sexo=input("ingrese el sexo del dueño ").upper()
                if validado_sexo==True:
                    print("el sexo se ingreso correctamente")
                else:
                    usuarios[nombre].append(sexo)
                    break

        case "2":
                usuarios=input("Ingrese el nombre  que desea buscar: ")
                if validador_usuarios(nombre)==True:
                    print("Entra a este if")
                    infousuario=buscarusuarios(nombre)

        case "3":
            print("-"*50)
            for indice in range(len(nombre)):
                
                print(f"Nombre: {nombre[indice]}  \t Cantidad: {cantidad[indice]} ")
                
            print("-"*50)

        case "4":
            print("saliendo.....")
        case default:
            print("opcion no valida")






      


                    
                  
















    






        


     