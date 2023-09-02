from Personas import Personas

class Usuarios:

    def __init__(self, username, password, cedula, nombre, apellidos, fcumple, telefono, sexo):
        self.username=username
        self.password=password
        self.persona=Personas(cedula,nombre,apellidos,fcumple,telefono,sexo)

    def getUsername(self):
        return f'su usuario es: {self.username}'
    
    def getPassword(self):
        return f'su password es: {self.password}'
    
    def setUsername(self, username):
        self.username=username

    def setPassword(self, password):
        self.password=password

    