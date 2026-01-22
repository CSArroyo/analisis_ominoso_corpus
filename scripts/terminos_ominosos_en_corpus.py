import csv

archivo_diccionario = "diccionario_ominoso_limpio.txt"
archivo_corpus = "terminos_corpus.csv"
archivo_salida = "terminos_ominosos_en_corpus.csv"

# Cargar diccionario ominoso
with open(archivo_diccionario, "r", encoding="utf-8") as f:
    diccionario_ominoso = set(
        linea.strip().lower() for linea in f if linea.strip()
    )

resultados = []

with open(archivo_corpus, "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    cabecera = next(lector)  # saltamos la primera fila

    for fila in lector:
        termino = fila[0].strip().lower()
        frecuencia = fila[1].strip()

        if termino in diccionario_ominoso:
            resultados.append((termino, frecuencia))

# Guardar resultados
with open(archivo_salida, "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["termino", "frecuencia"])
    escritor.writerows(resultados)

print(f"Archivo generado: {archivo_salida}")
print(f"Términos ominosos encontrados: {len(resultados)}")

