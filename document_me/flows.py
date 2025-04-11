from loguru import logger
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner

from document_me.llm import generate_docstring
from document_me.parser import (
    extract_undocumented_functions,
    insert_docstrings,
    save_to_output,
)


@task
def analyze_file(file_path):
    return extract_undocumented_functions(file_path)


@task
def document_function(func_code, model_name: str = "llama3"):
    return generate_docstring(func_code, model_name)


@flow(name="document_script_flow", task_runner=ConcurrentTaskRunner(max_workers=1))
def document_script_flow(file_path: str, model_name: str = "llama3"):
    functions = analyze_file(file_path)

    documented = []
    for func in functions:
        doc = document_function(func["source"], model_name)
        documented.append((func, doc))

    logger.info(f"[Documenter] Starting documentation for: {file_path}")

    modified_code = insert_docstrings(file_path, documented)
    logger.info(f"[Documenter] Finished documentation for: {file_path}")

    save_to_output(file_path, modified_code)
