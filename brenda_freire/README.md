# a primeira função usada foi a função len, para contar os caracteres em qualquer palavra ou frase que fosse digitada pelo usuário

def contarCaracteres(texto):
    return len(texto)

entrada = input('Digite uma palavra ou frase: ')

try:
    caracteres = contarCaracteres(entrada)
    print(f"A string '{entrada}' possui {caracteres} caracteres")
except:
    print('Erro: digite uma palavra ou frase')

# em seguida, foi utilizada a função parImpar, para verificar se o número digitado pelo usuário tinha divisão exata por 2. Caso a divisão seja exata, o programa retornará o resultado par

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

# em ambos os casos, o tratamento de erro try e except foi utilizado, justamente para evitar entradas de usuário que não estejam nas condições exigidas pelo programa