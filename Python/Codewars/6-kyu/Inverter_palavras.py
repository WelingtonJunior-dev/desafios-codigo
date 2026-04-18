'''
Desafio: "Stop gninnipS My sdroW!" (pare de girar minhas palavras).

Escreva uma função que receba uma string contendo uma ou mais palavras e retorne a mesma string, mas com todas as palavras que possuem cinco ou mais letras invertidas.

Regras:

- As strings passadas consistirão apenas de letras e espaços.
- Os espaços só serão incluídos quando houver mais de uma palavra presente.

Exemplos de Entrada e Saída:

"Hey fellow warriors"  --> "Hey wollef sroirraw"

"This is a test"        --> "This is a test"

"This is another test" --> "This is rehtona test"

'''


def spin_words(frase):
    lista_original = frase.split()
    resultado = []

    for palavra in lista_original:
        if len(palavra) > 5:
            resultado.append(palavra[::1])
        else:
            resultado.append(palavra)
    return " ".join(resultado)


