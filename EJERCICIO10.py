class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje
def eliminar_notificaciones_facebook(cola):
    cola_sin_facebook = [notificacion for notificacion in cola if notificacion.aplicacion != 'Facebook']
    return cola_sin_facebook
def mostrar_notificaciones_twitter_python(cola):
    notificaciones_python = [notificacion for notificacion in cola if notificacion.aplicacion == 'Twitter' and 'Python' in notificacion.mensaje]
    return notificaciones_python
def contar_notificaciones_entre_horas(cola, hora_inicio, hora_fin):
    pila_temporal = []
    contador = 0
    for notificacion in cola:
        if hora_inicio <= notificacion.hora <= hora_fin:
            pila_temporal.append(notificacion)
            contador += 1  
    return contador
cola_notificaciones = [
    Notificacion('11:30', 'Facebook', 'Mensaje de Facebook 1'),
    Notificacion('12:00', 'Twitter', 'Mensaje de Twitter con Python'),
    Notificacion('13:30', 'Twitter', 'Mensaje de Twitter sin Python'),
    Notificacion('14:00', 'Facebook', 'Mensaje de Facebook 2'),
    Notificacion('15:00', 'Instagram', 'Mensaje de Instagram'),
    Notificacion('15:30', 'Twitter', 'Mensaje de Twitter con Python'),
]
cola_sin_facebook = eliminar_notificaciones_facebook(cola_notificaciones)
print("Cola sin notificaciones de Facebook:")
for notificacion in cola_sin_facebook:
    print(notificacion.hora, notificacion.aplicacion, notificacion.mensaje)
print()
notificaciones_python = mostrar_notificaciones_twitter_python(cola_notificaciones)
print("Notificaciones de Twitter con la palabra 'Python':")
for notificacion in notificaciones_python:
    print(notificacion.hora, notificacion.aplicacion, notificacion.mensaje)
print()
contador_notificaciones = contar_notificaciones_entre_horas(cola_notificaciones, '11:43', '15:57')
print("Número de notificaciones entre las 11:43 y las 15:57:", contador_notificaciones)
