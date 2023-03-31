# Verificador automático de código de Python

Este programa ejecuta el código de un alumno con diferentes entradas predefinidas y verifica si las salidas son correctas. Si alguna salida no es correcta, utiliza el algoritmo de comparación de cadenas de Levenshtein para calcular la similitud entre la salida obtenida y la esperada. Si la similitud es mayor que un umbral predefinido, la prueba se considera una duda y se muestra un mensaje indicándolo. Si la similitud es menor que el umbral, la prueba se considera incorrecta y se muestra un mensaje indicando que se debe revisar el código del alumno.

## Instalación

Este programa requiere la instalación de las siguientes librerías de Python:

- `Levenshtein`

Puedes instalar estas librerías ejecutando el siguiente comando:

``pip install Levenshtein``

## Uso

Para usar este programa, sigue los siguientes pasos:

1. Supongamos que tenemos un archivo llamado `pruebaalumno.py` con el código del alumno que deseas verificar en la misma carpeta que el programa principal.
2. Define las entradas predefinidas y las salidas esperadas en las variables `inputs` y `expected_outputs`, respectivamente.
3. Ejecuta el programa.


## Ejemplos de uso

Supongamos que tenemos el siguiente código del alumno:

```
a = int(input())
b = int(input())
print(a * b)
```

Luego, podemos definir las entradas predefinidas y las salidas esperadas en el siguiente código:

```
inputs = ['2\n3\n', '5\n10\n']
expected_outputs = ['6', '50']
```

Finalmente, podemos ejecutar el programa con el comando `python verificador.py` y obtendremos el siguiente resultado:

```
Input 1: Incorrecto. Resultado esperado: 6. Resultado obtenido: 7. Porcentaje de similitud: 66.67%. Revisar por un humano.
Input 2: Duda. Resultado esperado: 50. Resultado obtenido: 51. Porcentaje de similitud: 97.14%
```

## Ejemplos de outputs

A continuación, se muestran algunos ejemplos de outputs que puede generar el programa de testing:

* Si la salida es correcta, se mostrará el siguiente mensaje:

```
Input 1: Correcto
Input 2: Correcto
```

* Si la salida no es correcta pero la similitud entre la salida esperada y la obtenida es mayor al umbral de similitud, se mostrará el siguiente mensaje:

```
Input 1: Duda. Resultado esperado: 6. Resultado obtenido: 7. Porcentaje de similitud: 83.33%
Input 2: Duda. Resultado esperado: 50. Resultado obtenido: 49. Porcentaje de similitud: 97.96%
```

* Si la salida no es correcta y la similitud entre la salida esperada y la obtenida es menor al umbral de similitud, se mostrará el siguiente mensaje:

```
Input 1: Incorrecto. Resultado esperado: 6. Resultado obtenido: 8. Porcentaje de similitud: 50.00%. Revisar por un humano.
Input 2: Incorrecto. Resultado esperado: 50. Resultado obtenido: 49. Porcentaje de similitud: 97.96%. Revisar por un humano.
```

## Umbral de similitud

Puedes modificar la variable `similarity_threshold` para ajustar el umbral de similitud necesario para considerar que la salida obtenida por el código del alumno es correcta.

Un valor bajo de `similarity_threshold` permitirá aceptar salidas que son similares pero no idénticas a las esperadas, mientras que un valor alto requerirá una coincidencia más exacta.

Aquí hay algunos ejemplos de cómo modificar la variable similarity_threshold para ajustar su comportamiento:

* `similarity_threshold = 0.5`: Este valor permitirá aceptar salidas que tienen al menos el 50% de similitud con la salida esperada. Puede ser útil en casos donde la salida es compleja y puede haber varias formas de expresar la respuesta correcta.

* `similarity_threshold = 0.8`: Este valor es el que se establece en el código original y requiere que la salida obtenida sea al menos un 80% similar a la salida esperada. Es un buen valor por defecto para la mayoría de los casos.

* `similarity_threshold = 0.95`: Este valor requerirá una coincidencia muy cercana entre la salida obtenida y la esperada. Puede ser útil en casos donde la salida es simple y solo hay una forma clara de expresar la respuesta correcta.

Recuerda que debes ajustar este valor en función de la complejidad de la salida esperada y de cuántas formas diferentes hay para expresar la respuesta correcta.