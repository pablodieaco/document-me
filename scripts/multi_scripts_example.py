def greet(name):
    """Description: Greet a person by name.

    Args:
    name (str): The name to greet."""
    print(f'Hi, {name}!')
    print('Ready?')


def add(a, b):
    """Description: Adds two numbers together.

    Args:
    a (int): The first number to be added.
    b (int): The second number to be added.

    Returns:
    int: The sum of the input numbers."""
    return a + b


def divide(a, b):
    """Description: Divide two numbers.

    Args:
    a (int): The dividend.
    b (int): The divisor."""
    if b == 0:
        raise ValueError('Cannot divide by zero.')
    return a / b


def process_list(items):
    """Description: Process a list of items and return the total sum and the sorted list.

    Args:
    items (list): The input list to be processed.

    Returns:
    tuple: A tuple containing the total sum and the sorted list.

    Raises:
    None."""
    ordered = sorted(items)
    total = sum(ordered)
    return total, ordered


def complex_product(a, b):
    """Description:
    Calculates the product of two complex numbers.

    Args:
    a (tuple): A tuple containing the real and imaginary parts of the first complex number.
    b (tuple): A tuple containing the real and imaginary parts of the second complex number.

    Returns:
    real_part, imag_part (tuple): A tuple containing the real and imaginary parts of the product."""
    a_real, a_i = a
    b_real, b_i = b
    real_part = a_real * b_real - a_i * b_i
    imag_part = a_real * b_i + a_i * b_real
    return real_part, imag_part
