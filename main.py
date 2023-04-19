from typing import Tuple


def calculate(expression: str) -> Tuple[float, float]:
    expression_array = expression.split(" ")
    operand = expression_array[0]
    if expression_array[1].isdigit():
        first_val = float(expression_array[1])
        second_val_pointer = 2
    else:
        first_val, inner_pointer = calculate(" ".join(expression_array[1:]))
        second_val_pointer = 2 + inner_pointer

    if expression_array[second_val_pointer].isdigit():
        second_val = float(expression_array[second_val_pointer])
    else:
        second_val, _ = calculate(" ".join(expression_array[second_val_pointer:]))

    return make_operation(operand, first_val, second_val), second_val_pointer


def make_operation(operand: str, first_val: float, second_val: float) -> float:
    return eval(f"{first_val} {operand} {second_val}")


def main():
    result, _ = calculate("* 3 4")
    print(result)
    result, _ = calculate("* + 3 4 5")
    print(result)
    result, _ = calculate("/ - 3 4 + 2 5")
    print(result)


if __name__ == '__main__':
    main()
