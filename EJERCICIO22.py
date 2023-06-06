from queue import Queue

class Personaje:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero
cola_personajes = Queue()
cola_personajes.put(Personaje("Tony Stark", "Iron Man", "M"))
cola_personajes.put(Personaje("Steve Rogers", "Capitán América", "M"))
cola_personajes.put(Personaje("Natasha Romanoff", "Black Widow", "F"))
cola_personajes.put(Personaje("Carol Danvers", "Capitana Marvel", "F"))
cola_personajes.put(Personaje("Scott Lang", "Ant-Man", "M"))
cola_personajes.put(Personaje("Stephen Strange", "Doctor Strange", "M"))
def encontrar_personaje_por_superheroe(cola, superheroe):
    for personaje in list(cola.queue):
        if personaje.superheroe == superheroe:
            return personaje.nombre
    return None
nombre_personaje_capitana_marvel = encontrar_personaje_por_superheroe(cola_personajes, "Capitana Marvel")
print("Nombre del personaje de la superhéroe Capitana Marvel:", nombre_personaje_capitana_marvel)
print("Nombres de los superhéroes femeninos:")
while not cola_personajes.empty():
    personaje = cola_personajes.get()
    if personaje.genero == "F":
        print(personaje.superheroe)
cola_personajes.put(Personaje("Tony Stark", "Iron Man", "M"))
cola_personajes.put(Personaje("Steve Rogers", "Capitán América", "M"))
cola_personajes.put(Personaje("Natasha Romanoff", "Black Widow", "F"))
cola_personajes.put(Personaje("Carol Danvers", "Capitana Marvel", "F"))
cola_personajes.put(Personaje("Scott Lang", "Ant-Man", "M"))
cola_personajes.put(Personaje("Stephen Strange", "Doctor Strange", "M"))
print("Nombres de los personajes masculinos:")
while not cola_personajes.empty():
    personaje = cola_personajes.get()
    if personaje.genero == "M":
        print(personaje.nombre)
def encontrar_superheroe_por_nombre(cola, nombre):
    for personaje in list(cola.queue):
        if personaje.nombre == nombre:
            return personaje.superheroe
    return None
nombre_superheroe_scott_lang = encontrar_superheroe_por_nombre(cola_personajes, "Scott Lang")
print("Nombre del superhéroe del personaje Scott Lang:", nombre_superheroe_scott_lang)
print("Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
while not cola_personajes.empty():
    personaje = cola_personajes.get()
    if personaje.nombre.startswith("S"):
        print("Nombre:", personaje.nombre)
        print("Superhéroe:", personaje.superheroe)
        print("Género:", personaje.genero)
def buscar_personaje_por_nombre(cola, nombre):
    for personaje in list(cola.queue):
        if personaje.nombre == nombre:
            return True
    return False
if buscar_personaje_por_nombre(cola_personajes, "Carol Danvers"):
    print("El personaje Carol Danvers se encuentra en la cola.")
    nombre_superheroe_carol_danvers = encontrar_superheroe_por_nombre(cola_personajes, "Carol Danvers")
    print("Nombre de su superhéroe:", nombre_superheroe_carol_danvers)
else:
    print("El personaje Carol Danvers no se encuentra en la cola.")
