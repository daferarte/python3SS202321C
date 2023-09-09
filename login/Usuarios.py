from Personas import Personas

class Usuarios:

    def __init__(self, username, password, cedula, nombre, apellidos, fcumple, telefono, sexo):
        self.username=username
        self.password=password
        self.sesionActiva=False
        self.persona=Personas(cedula,nombre,apellidos,fcumple,telefono,sexo)

    def getUsername(self):
        return f'su usuario es: {self.username}'
    
    def getPassword(self):
        return f'su password es: {self.password}'
    
    def getSesionActiva(self):
        return self.sesionActiva
    
    def setUsername(self, username):
        self.username=username

    def setPassword(self, password):
        self.password=password

    def setSesionActiva(self, sesion):
        self.sesionActiva=sesion

    def consultar_informacion(self):
        return f'su informacion de usuario es: {self.getUsername()} {self.getPassword()} {self.persona.consultar_informacion()}'
    
    def iniciarSesion(self, username, password):
        
        if(self.username==username and self.password==password):
            self.setSesionActiva(True)

        return self.sesionActiva