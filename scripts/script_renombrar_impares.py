from pathlib import Path

carpeta = Path(r"C:\Users\claud\Documents\ShareX\Screenshots\2025-07\impares")
archivos = sorted(carpeta.glob("*.png"), key=lambda f: f.stat().st_mtime)

for i, archivo in enumerate(archivos):
    nuevo_nombre = carpeta / f"page_{2*i + 1:03}.png"
    archivo.rename(nuevo_nombre)
