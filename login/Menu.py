from Usuarios import Usuarios

print ('Bienvenido al software de login')

opcion=1

while(opcion != 0):
    print('1. Agregar usuario')
    print('2. Mostrar usuario')
    print('3. Iniciar sesion')
    print('4. cerrar sesion')
    print('0. salir')

    opcion = int(input('digite su opcion: '))
    
    if(opcion == 1):
        print('agregando usuario')
        usu=Usuarios(input('usuario: '),input('Contrasenia usuario: '),input('cedula usuario: '),input('Nombre usuario: '),input('Apellido usuario: '), input('fecha cumpleanos usuario: '), input('telefono usuario: '), input('Sexo usuari: '))
    elif(opcion == 2):
        print('Mostar usuario')
        print(usu.consultar_informacion())
    elif(opcion == 3):
        print('Iniciar sesion')
        if(usu.getSesionActiva()==False):
            if( usu.iniciarSesion(input('Digite su usuario: '), input('Digite su contrasena: '))== True ):
                print('Su sesion esta activa')
            else:
                print('Usuario incorrecto')
        else:
            print('su sesion ya fue iniciada')
    elif(opcion == 4):
        print('Cerrar sesion')
        if(usu.getSesionActiva()==True):
            usu.setSesionActiva(False)
            print('Usted ha cerrado sesion')
        else:
            print('Usted no ha iniciado sesion')
    elif(opcion == 0):
        print('Adios')
    else:
        print('Opcion desconocida')