class Usuario:
    cedula=''
    nombres=''
    apellidos=''
    sexo=''
    correo=''
    telefono=''

    def __init__(self,cedula,nombres,apellidos,sexo,correo='',telefono=''):
        self.cedula=cedula
        self.nombres=nombres
        self.apellidos=apellidos
        self.sexo=sexo
        self.correo=correo
        self.telefono=telefono

    def AgendarCita(self, fecha, hora):
        return f'cita disponible para el dia {fecha} y con hora {hora}'
    
