def greet(name):
    print(f"Hi, {name}!, I am changing this file to test the documenter.")


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def process_list(items):
    ordered = sorted(items)
    total = sum(ordered)
    return total, ordered


def complex_product(a, b):
    a_real, a_i = a
    b_real, b_i = b

    real_part = a_real * b_real - a_i * b_i
    imag_part = a_real * b_i + a_i * b_real
    return real_part, imag_part


def get_llm():
    from langchain_community.llms import Ollama

    return Ollama(
        model="llama3",  # ← Este es el nombre que usas en `ollama run`
        temperature=0.1,
        top_p=0.95,
        repeat_penalty=1.1,
        num_ctx=4096,
    )


def safe_save(path, content):
    import os

    from filelock import FileLock
    from loguru import logger

    # Crear carpeta de locks si no existe
    lock_dir = os.path.join(os.path.dirname(path), ".locks")
    os.makedirs(lock_dir, exist_ok=True)

    filename = os.path.basename(path)
    lock_path = os.path.abspath(os.path.join(lock_dir, f"{filename}.lock"))

    with FileLock(lock_path):
        with open(path, "w") as f:
            f.write(content)

    logger.info(f"[Documenter] Documented file saved: {path}")
