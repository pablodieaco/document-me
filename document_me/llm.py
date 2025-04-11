GOOGLE_STYLE_DOCSTRING = """
    Description:
        {description}:  Description of the function.
    Args:
        {args} (str): Description of the arguments.
    Returns:
        {returns} (str): Description of what the function returns.
    Raises:
        {raises} (str): Description of the exceptions the function may raise.
    """


def generate_docstring(code: str, model_name: str = "llama3") -> str:
    prompt = (
        "You are a Python expert and your task is to generate a Google Style docstring.\n"
        f"The Google Style docstring for Python function is like \n{GOOGLE_STYLE_DOCSTRING}\n\n"
        "Generate a Google Style docstring for the following Python function.\n"
        "Do not include any explanatory text or labels like 'Here is...'.\n"
        "Do not include triple quotes.\n"
        "Return only the content of the docstring (Description, Args, Returns, etc.):\n\n"
        f"```python\n{code}\n```"
    )

    llm = get_llm(model_name)
    result = llm.invoke(prompt)

    # logger.debug(f"[LLM] Generated docstring:\n{result}")

    return result.strip()


def get_llm(model_name: str = "llama3"):
    from langchain_community.llms import Ollama

    return Ollama(
        model=model_name,  # ← Este es el nombre que usas en `ollama run`
        temperature=0.1,
        top_p=0.95,
        repeat_penalty=1.1,
        num_ctx=4096,
    )


# def get_llm(model_id=MODEL_ID, local_dir=LOCAL_DIR):
#     if not os.path.exists(local_dir):
#         logger.info(
#             f"[LLM] Not found local model {local_dir}, downloading {model_id}..."
#         )
#         tokenizer = AutoTokenizer.from_pretrained(model_id)
#         model = AutoModelForSeq2SeqLM.from_pretrained(
#             model_id, device_map="auto", torch_dtype="auto"
#         )
#         # Guarda localmente
#         logger.info("[LLM] Saving model locally...")
#         os.makedirs(local_dir, exist_ok=True)
#         tokenizer.save_pretrained(local_dir)
#         model.save_pretrained(local_dir)
#     else:
#         logger.info("[LLM] Loading local model...")
#         tokenizer = AutoTokenizer.from_pretrained(local_dir)
#         model = AutoModelForSeq2SeqLM.from_pretrained(
#             local_dir, device_map="auto", torch_dtype="auto"
#         )

#     hf_pipeline = pipeline(
#         "text-generation",
#         model=model,
#         tokenizer=tokenizer,
#         temperature=0.1,  # recomendable temperatura baja
#         top_p=0.95,  # controlar calidad y diversidad
#         repetition_penalty=1.1,  # evitar repeticiones
#         max_new_tokens=150,  # reducción recomendada
#         eos_token_id=tokenizer.eos_token_id,
#         do_sample=True,
#     )

#     logger.info("[LLM] Model loaded successfully.")

#     return HuggingFacePipeline(pipeline=hf_pipeline)
