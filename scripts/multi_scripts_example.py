def greet(name):
    print(f"Hi, {name}!")


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
