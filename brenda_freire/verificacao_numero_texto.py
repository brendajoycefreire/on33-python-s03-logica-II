def contarCaracteres(texto):
    return len(texto)

entrada = input('Digite uma palavra ou frase: ')

try:
    caracteres = contarCaracteres(entrada)
    print(f"A string '{entrada}' possui {caracteres} caracteres")
except:
    print('Erro: digite uma palavra ou frase')
    
def parImpar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

entrada = input('Digite um número inteiro: ')

try:
    numero = int(entrada)
    resultado = parImpar(numero)
    print(f'O número {numero} é {resultado}')

except:
    print('Erro: digite um número inteiro')