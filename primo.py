"""
Modulo para mostrar si un número es primo o no
"""


def is_primo(number: int) -> bool:
    res_list: List[int] = [ n for n in range(2, number) if number % n == 0]
    return len(res_list) == 0


def run():
    num: int = int(input('ingrese un numero:\n'))
    print("El número {} es primo: {}".format(num, is_primo(num)))

if __name__ == '__main__':
    run()