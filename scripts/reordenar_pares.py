from pathlib import Path
import re

carpeta = Path(r"C:\Users\claud\Documents\ShareX\Screenshots\2025-07")  # 🟢 Ajustá la ruta si hace falta

# Buscar archivos tipo page_012.png, etc.
archivos = sorted(carpeta.glob("page_*.png"))

patron = re.compile(r"page_(\d{3})\.png")

for archivo in archivos:
    match = patron.match(archivo.name)
    if not match:
        continue

    numero = int(match.group(1))
    if numero % 2 != 0:
        continue  # Solo procesamos pares

    nuevo_numero = numero - 2
    nuevo_nombre = f"page_{nuevo_numero:03}.png"
    nuevo_path = carpeta / nuevo_nombre

    archivo.rename(nuevo_path)