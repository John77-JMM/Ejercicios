# -*- coding: utf-8 -*-
"""EjExplorador6_42.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzRGF0fadqZPNH9xba0UmttC9WH_Krfd
"""

#IMC
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es: {imc:.2f}")