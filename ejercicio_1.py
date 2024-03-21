import threading
x = 0

#Creando un bloqueo para la sección crítica
lock = threading.Lock()

#Adquirir el bloqueo antes de entrar en la sección crítica
def incremento():
    global x
    with lock:  
        x += 1

def TareaThread():
    for _ in range(100000):
        incremento()

def TareaPrin():
    global x
    x = 10 
    #Se crean los hilos
    t1 = threading.Thread(target=TareaThread)
    t2 = threading.Thread(target=TareaThread)

    #Inicio de los hilos
    t1.start()
    t2.start()

    #Uniendo los hilos
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        TareaPrin()
        print("Iteración {0}: x = {1}".format(i, x))

