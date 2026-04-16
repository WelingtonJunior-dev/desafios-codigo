# Esse desafio do Codewars consiste em comparar uma string com o final dela, e então retornar verdadeiro ou falso

'''Criei uma função que recebe dois textos: a palavra principal e o trecho final que queremos verificar. 
Primeiro, calculo o tamanho desse trecho final para saber quantos caracteres preciso 'cortar' da palavra principal. 
Usando o fatiamento do Python com índice negativo, extraio exatamente essa parte final da palavra. 
Por fim, comparo se esse pedaço que cortei é igual ao trecho buscado; se for idêntico, a função retorna que é verdadeiro, confirmando que a palavra termina como esperado.'''

def strings_termina_com(text, ending):
    if ending == "":
        return True

    tamanho_final = len(ending)
    final_do_texto = text[-tamanho_final:]
    
    return final_do_texto == ending