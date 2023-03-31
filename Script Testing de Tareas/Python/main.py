# Importar el módulo subprocess para ejecutar el código del alumno
import subprocess

# Definir los inputs predefinidos
inputs = ['2\n3\n', '5\n10\n']

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
    resultado = salida[-1].strip()
    
    # Verificar si el resultado es correcto
    resultado_esperado = str(int(entrada.split('\n')[0]) * int(entrada.split('\n')[1])) 
    if resultado == resultado_esperado:
        print(f'Input {i+1}: Correcto')
    else:
        print(f'Input {i+1}: Incorrecto. Resultado esperado: {resultado_esperado}. Resultado recibido: {resultado}')
        
        
