import random
import time

print("Simulador de Máquina Tragaperras.\n"+
      "-----------------------------------\n"+
      "Voy a generar secuencias de 3 frutas entre Plátano, Fresa, Manzana, Naranja y Cereza")

# Lista de frutas
fruit_list = ['🍌', '🍓', '🍎', '🍊', '🍒']

# Contador global de jugadas
contador = 0
playAgain = True

while playAgain == True:

    resultado = []
    contador += 1  # Incrementar el contador al inicio de cada jugada

    # Generar las frutas aleatorias
    for _ in range(3):
        rueda = random.choice(fruit_list)
        resultado.append(rueda)
        print(f"{rueda}", end=" ", flush=True)
        time.sleep(0.5)

    print()  # Salto de línea después de imprimir las frutas
    
    
    # Verificar si hay un JACKPOT
    if resultado[0] == resultado[1] == resultado[2]:
        print("\n!!!!!!!!!!!!!!!!!JACKPOT!!!!!!!!!!!!!!!")
        print("Número de veces jugadas: " + str(contador))
        respuesta = input("¿Quieres jugar de nuevo? (si/no)")
        if respuesta.lower() == "si":
            continue
        else:
            playAgain = False
    else:
        input("\n💸Enter para jugar de nuevo💸")
        
        
