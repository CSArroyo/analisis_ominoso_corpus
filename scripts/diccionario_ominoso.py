archivo_entrada = "diccionario_ominoso01.txt"
archivo_salida = "diccionario_ominoso_limpio.txt"

# Leer el archivo de entrada
with open(archivo_entrada, "r", encoding="utf-8") as f:
    palabras = [
        linea.strip().lower()
        for linea in f
        if linea.strip()
    ]

# Eliminar duplicados y ordenar alfabéticamente
palabras_limpias = sorted(set(palabras))

# Guardar el resultado
with open(archivo_salida, "w", encoding="utf-8") as f:
    for palabra in palabras_limpias:
        f.write(palabra + "\n")

print(f"Diccionario limpio guardado en: {archivo_salida}")
print(f"Número de términos únicos: {len(palabras_limpias)}")
