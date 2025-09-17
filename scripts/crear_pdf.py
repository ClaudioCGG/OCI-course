from pathlib import Path
from PIL import Image

# 📂 Carpeta con las imágenes ordenadas
carpeta = Path(r"C:\Users\claud\Documents\ShareX\Screenshots\2025-07")
imagenes = sorted(carpeta.glob("page_*.png"))

# 📘 Crear PDF con resolución alta
if imagenes:
    imagenes_pil = [Image.open(im).convert("RGB") for im in imagenes]

    # DPI sugerido para impresión o lectura nítida
    salida = carpeta / "documento_final.pdf"
    imagenes_pil[0].save(
        salida,
        save_all=True,
        append_images=imagenes_pil[1:],
        resolution=300  # 👈 Este parámetro mejora la calidad en lectores PDF
    )

    print(f"✅ PDF creado con alta resolución: {salida}")
else:
    print("⚠️ No se encontraron imágenes en la carpeta.")