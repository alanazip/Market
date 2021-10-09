from threading import Thread
import time, os

def corredor(nome, pausa, distancia):
    percorrido = 0
    print(nome, "iniciou!")
    while percorrido <= distancia:
            print(nome,":", percorrido,"/", distancia,"\n")
            percorrido += 1
            time.sleep(pausa)
    print(nome, "terminou.")

os.system("cls" if os.name == "nt" else "clear")
input("Pressione Enter para iniciar a corrida:\n")

Thread(target=corredor, args=["Onofre", 0.3, 50]).start()
Thread(target=corredor, args=["Godofredo", 0.9, 30]).start()

print("Os corredores iniciaram a corrida!")
time.sleep(10)
input("Pressione Enter para encerrar:\n")