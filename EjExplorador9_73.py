# -*- coding: utf-8 -*-
"""EjExplorador9_73.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17NQCihH5YDD7ErWEd1SjiQvhHCNY1rIy
"""

#Adivinanza


import random

numero_secreto = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste!")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Inténtalo de nuevo.")
    else:
        print("El número secreto es menor. Inténtalo de nuevo.")