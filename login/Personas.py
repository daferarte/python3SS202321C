class Personas:

    # metodo contructor y definicion de atributos
    def __init__(self, cedula, nombre, apellidos, fcumple, telefono, sexo):
       self.cedula=cedula
       self.nombre=nombre
       self.apellidos=apellidos
       self.fcumple=fcumple       
       self.telefono=telefono
       self.sexo=sexo

    # metodos get de consulta de informacion
    def getCedula(self):
        return f'Su cedula es: {self.cedula}'
    
    def getNombre(self):
        return f'Su nombre es: {self.nombre}'
    
    def getApellido(self):
        return f'Sus apellidos son: {self.apellidos}'
    
    def getFCumple(self):
        return f'Su fecha de cumpleaños es: {self.fcumple}'
    
    def getTelefono(self):
        return f'Su telefono es: {self.telefono}'
    
    def getSexo(self):
        return f'Su sexo es: {self.sexo}'
    
    # metodos set para actualizacion de informacion
    def setCedula(self, cedula):
        self.cedula=cedula
    
    def setNombre(self, nombre):
        self.nombre=nombre
    
    def setApellido(self, apellidos):
        self.apellidos=apellidos
    
    def setFCumple(self, fcumple):
        self.fcumple=fcumple
    
    def setTelefono(self, telefono):
        self.telefono=telefono
    
    def setSexo(self, sexo):
        self.sexo=sexo

    def consultar_informacion(self):
        return f' Su informacion de persona es la siguiente: {self.getCedula()} {self.getNombre()} {self.getApellido()} {self.getFCumple()} {self.getSexo()} {self.getTelefono()}'

    def actualizar_info(self, cedula, nombre, apellidos, fcumple, telefono, sexo):
        self.setCedula(cedula)
        self.setNombre(nombre)
        self.setApellido(apellidos)
        self.setfcumple(fcumple)
        self.settelefono(telefono)
        self.setSexo(sexo)
