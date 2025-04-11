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
        model=model_name,
        temperature=0.1,
        top_p=0.95,
        repeat_penalty=1.1,
        num_ctx=4096,
    )
