# Funny Numbers
Evita que tus amigos se rian de ti cuando tu código mencione algun numero chistoso.

## Ejemplos
En el primer ejemplo ponemos a prueba el numero _5_ y con el segundo parametro en `True` para mostrar el mensaje, en caso de que no se quiera mostrar usamos `False`.
```py
import funnyNumber as fn
numero = fn.fn(5, True)
print(numero) # 3 + 2, Cuidado con el Funny Number
```
En este ejemplo veremos el mismo código pero sin mostrar el mensaje.

```py
import funnyNumber as fn
numero = fn.fn(5, False)
print(numero) # 3 + 2
```

## Instalación
Para instalar el paquete lo unico que tienes que hacer es poner en la terminal el siguiente comando:

```bash
pip install funnyNumbers
```
