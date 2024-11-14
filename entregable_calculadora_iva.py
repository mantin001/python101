####CASO HISTORIA
"""
"COMO banco, necesitamos una calculadora online QUE permita a los clientes ingresar dos variables (precio sin IVA e IVA) y obtener como resultado el valor del IVA y el precio con IVA.
 El programa también debe registrar estos datos (inputs y outputs) PARA un análisis posterior."
"""


############## 0. PROGRAMA CALCULADORA IVA 

"""
Queremos un programa que nos permita introducir el precio sin iva, 
El iva (y su porcentaje)
y como salida (output) nos generará el precio sin iva (input ), el iva (output) y precio con iva (output)
Lo ideal sería que los inputs se guardaran en listas independientes para identificar cada variable
"""

import sys

print("            Calculadora IVA           ")
print("   Sumar IVA   ")
nombre=str(input("Indica tu nombre de usuario"))
precio=float(input("Precio sin IVA"))
IVA=int(input("Porcentaje de IVA"))
valor_IVA= precio*(IVA/100)
precio_con_iva= valor_IVA + precio
informe= [nombre,precio,IVA]
print(informe)


############ INFORME HISTÓRICO + MANUAL
"""
Manua de uso: 
Este programa nos ayuda a identificar qué tipo de variables deberíamos utilizar en un contexto práctico.
 Aquí comenzamos con una lista de precios, obtenida a partir de las interacciones entre el programa y el cliente.

Para este ejemplo, hemos creado manualmente una lista de precios como entrada y usamos un porcentaje de IVA fijo del 21%. 
En otros casos, podríamos trabajar con un histórico del IVA representado también como una lista.

Futuras mejoras: Sería ideal que los inputs proporcionados por el usuario (ya sea como listas o conjuntos)
 se almacenaran automáticamente en el historial. 
 Además, se podría agregar un botón de "Generar Historial" que permita visualizar todas las variables de interés recopiladas hasta el momento.

"""

hist_precio= [200,3453,4020.12, 3532.55, 23842.5,45353.20]
porcentaje_IVA= 21 #uno valor fijo

# Listas para almacenar los resultados que luego mostraré en el HISTORIAL
valor_IVA_his = []
precio_con_IVA_his = []

#precio sería el i (item dentro del historial o hist_precio)
for precio in hist_precio:
    valor_IVA = precio * (porcentaje_IVA / 100) #esto es la función
    precio_con_IVA = precio + valor_IVA #esto es la función para el cálculo del valor con IVA
    valor_IVA_his.append(valor_IVA)
    precio_con_IVA_his.append(precio_con_IVA)
print(f"Historial de cálculos:     \n Historial de los valores introducidos: {hist_precio} \n Historial del costo del IVA: {valor_IVA_his}\n Historial de valor con IVA: { precio_con_IVA_his} ")

##Mis pruebas 
"""

--- PRUEBA DE CONTRASTE ---
Valor test: 1000
Valor esperado para IVA: 210.0 (debería ser 210)
Valor esperado con IVA: 1210.0 (debería ser 1210)
prueba (ctrl + SHITF + V ) 

EJEMPLO 1: 
# si valor_Iva = 21
#el precio es 1_000=210
#el valor_IVA= 1_000*(21/100) 
#el precio_con_Iva_ = 1_000 + (210) =1210



| Valor sin IVA (€) | IVA (%) | Valor IVA (€) | Valor con IVA (€) |
|-------------------|---------|---------------|-------------------|
| 1000.00           | 21      | 210.00        | 1210.00          |
| 3453.00           | 21      | 725.13        | 4178.13          |
| 4020.12           | 21      | 844.23        | 4864.35          |
| 3532.55           | 21      | 741.84        | 4274.39          |
| 23842.50          | 21      | 5006.93       | 28849.43         |
| 45353.20          | 21      | 9524.17       | 54877.37         |


"""
