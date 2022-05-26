"""
Averiguar si una cadena de caracteres en un palindromo
"""


def is_palindrome(string: str) -> bool:
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def run():
    print(is_palindrome('Ligar es ser agil'))

if __name__ == '__main__':
    run()