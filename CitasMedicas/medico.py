from especialidad import Especialidad

class Medico:

    cedula=''
    nombres=''
    apellidos=''
    sexo=''
    correo=''
    telefono=''

    def __init__(self,cedula,nombres,apellidos,sexo, especialidad, correo='',telefono=''):
        self.cedula=cedula
        self.nombres=nombres
        self.apellidos=apellidos
        self.sexo=sexo
        self.correo=correo
        self.telefono=telefono
        self.especialidad=Especialidad(especialidad)

