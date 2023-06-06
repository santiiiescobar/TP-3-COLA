import queue
cola_impresion = queue.PriorityQueue()
cola_impresion.put((1, "Documento 1 (Empleado)"))
cola_impresion.put((1, "Documento 2 (Empleado)"))
cola_impresion.put((1, "Documento 3 (Empleado)"))
primer_documento = cola_impresion.get()[1]
print("Imprimiendo:", primer_documento)
cola_impresion.put((2, "Documento 4 (Staff TI)"))
cola_impresion.put((2, "Documento 5 (Staff TI)"))
cola_impresion.put((3, "Documento 6 (Gerente)"))
segundo_documento = cola_impresion.get()[1]
tercer_documento = cola_impresion.get()[1]
print("Imprimiendo:", segundo_documento)
print("Imprimiendo:", tercer_documento)
cola_impresion.put((1, "Documento 7 (Empleado)"))
cola_impresion.put((1, "Documento 8 (Empleado)"))
cola_impresion.put((3, "Documento 9 (Gerente)"))
print("Imprimiendo todos los documentos de la cola de impresión:")
while not cola_impresion.empty():
    documento = cola_impresion.get()[1]
    print("Imprimiendo:", documento)
