import subprocess
import Levenshtein

# Definir los inputs predefinidos
inputs = ['2\n3\n', '5\n10\n']
expected_outputs = ['6', '50']

# Definir el umbral de similitud
similarity_threshold = 0.8

# Abrir el archivo del alumno para leer su código
with open('pruebaalumno.py', 'r') as f:
    codigo_alumno = f.read()

# Ejecutar el código del alumno con cada input y verificar la salida
for i, entrada in enumerate(inputs):
    # Ejecutar el código del alumno con el input actual
    proceso = subprocess.run(['python', '-c', codigo_alumno],
                              input=entrada.encode(),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    
    # Obtener la salida del código del alumno y separarla en líneas
    salida = proceso.stdout.decode().strip().split('\n')
    
    # Obtener la última línea de la salida (que debería ser el resultado)
    resultado_obtenido = salida[-1].strip()
    
    # Verificar si el resultado es correcto
    resultado_esperado = expected_outputs[i]
    if resultado_obtenido == resultado_esperado:
        print(f'Input {i+1}: Correcto')
    else:
        # Calcular la similitud entre el resultado obtenido y el esperado
        similarity = Levenshtein.ratio(resultado_obtenido, resultado_esperado)
        if similarity >= similarity_threshold:
            print(f'Input {i+1}: Duda. Resultado esperado: {resultado_esperado}. Resultado obtenido: {resultado_obtenido}. Porcentaje de similitud: {similarity*100:.2f}%')
        else:
            print(f'Input {i+1}: Incorrecto. Resultado esperado: {resultado_esperado}. Resultado obtenido: {resultado_obtenido}. Porcentaje de similitud: {similarity*100:.2f}%. Revisar por un humano.')