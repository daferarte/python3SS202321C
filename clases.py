class Animales:
    nombre=''
    peso=''
    color=''
    edad=''

    def __init__(self, nombre, peso, color, edad):
        self.color=color
        self.nombre=nombre
        self.peso=peso
        self.edad=edad
    
    def comer(self, comida):
        return f'estoy comiendo {comida}'
    
    def dormir(self):
        print(f'soy {self.nombre} y estoy durmiendo')

class gato(Animales):
    garras=''

    def __init__(self, nombre, peso, color, edad, garras):
        super().__init__(nombre,peso,color,edad)
        self.garras=garras

    def dormir(self, lugar):
        return super().dormir()
        return f'soy {super().nombre} y estoy durmiendo en {lugar}'

# animal1=Animales("pascual",25.5,"dorado",12)
# animal1.dormir()
# animal1.comer

pelusa = gato("pelusa",25.5,"dorado",12,True)
print(pelusa.dormir("sofa"))

        