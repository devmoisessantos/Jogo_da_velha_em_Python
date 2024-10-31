print('PROGRAMA DE RECONNHECIMENTO')
print('SIGA AS INSTRUÇÕES ABAIXO: ')
print('INSTRUÇÕES: \n')
print()
print('1. Digite o seu nome de usuário.')
print('2. Digite a sua idade.\n')

nome_usuario = str(input('1. Digite o seu nome de usuário.\n'))
idade = int(input('2. Digite a sua idade.\n'))


usuario = {
        "nome": nome_usuario,
        "idade": idade
} 

print("\nDados do usuário:")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")

'''
...
'''