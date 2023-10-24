import random

def jugar_juego():
    numero_secreto = random.randint(0,100)
    intentos=0
    print("Bienvenido al Juego de Adivinanzas")
    print("Estoy pensando en un número entre el 0 y el 100 ¡Te reto a adivinarlo!")
    
    while True:
        try:
            intento = int(input("Tu suposición:  "))
        except ValueError:
            print("Ingrese un número válido")
            continue
        intentos += 1
    
        if intento<numero_secreto:
            print("¡Tu número es demasiado bajo! Inténtalo otra vez...")
        elif intento>numero_secreto:
            print("¡Tu número es demasiado alto! Inténtalo de nuevo...")
        else:
            print(f"¡Felicidades, adivinaste el número! lo hiciste en {intentos} intentos ¿Puedes hacerlo en menos intentos?")
            break
    
if __name__=="__main__":
    jugar_juego()