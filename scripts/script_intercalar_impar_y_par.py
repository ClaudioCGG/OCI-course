from pathlib import Path
from shutil import copy2

# Carpetas base
carpeta_impares = Path(r"C:\Users\claud\Documents\ShareX\Screenshots\2025-07\impares")
carpeta_pares = Path(r"C:\Users\claud\Documents\ShareX\Screenshots\2025-07\pares")
carpeta_final = Path(r"C:\Capturas\Intercaladas")
carpeta_final.mkdir(exist_ok=True)

# Ordenar por fecha de modificación
impares = sorted(carpeta_impares.glob("*.png"), key=lambda f: f.stat().st_mtime)
pares = sorted(carpeta_pares.glob("*.png"), key=lambda f: f.stat().st_mtime)

# Intercalado y copia
for i, (impar, par) in enumerate(zip(impares, pares), 1):
    copy2(impar, carpeta_final / f"page_{2*i - 1:03}.png")
    copy2(par, carpeta_final / f"page_{2*i:03}.png")

print(f"Listo: {len(impares) + len(pares)} imágenes intercaladas en '{carpeta_final}'")
