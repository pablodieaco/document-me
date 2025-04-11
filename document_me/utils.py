from filelock import FileLock
import os
from loguru import logger
def safe_save(path, content):
    # Crear carpeta de locks si no existe
    lock_dir = os.path.join(os.path.dirname(path), ".locks")
    os.makedirs(lock_dir, exist_ok=True)

    filename = os.path.basename(path)
    lock_path = os.path.abspath(os.path.join(lock_dir, f"{filename}.lock"))

    with FileLock(lock_path):
        with open(path, "w") as f:
            f.write(content)
    
    logger.info(f"[Documenter] Documented file saved: {path}")
