# -*- coding: utf-8 -*-
"""EjExplorador6_45.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KOzx2kax0McWq9rdZnSwDQxQnCwvP_e-
"""

#Precio de venta
precio_producto = float(input("Ingrese el valor del producto: "))

igv = precio_producto * 0.19
precio_venta = precio_producto + igv

print(f"Ingreso general a las ventas: {precio_venta}")
print(f"Precio de venta: {precio_venta}")