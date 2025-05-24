def reverse_text(text):
    return text[::-1]


def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(f"Invalid operator: {operator}")


reversed_text = reverse_text("Hello, World!")
print(f"Reversed text: {reversed_text}!!!")

result = calculator(10, 5, '+')
print(f"Calculator result: {result}!!!!")