import os

"""Função que limpa a tela"""
def limpar():
    os.system('cls')
"""Fim"""

"""Função que cadastra o carro"""
def cadastro():
    nome = input('Qual o nome desse carro? ').capitalize()
    limpar()
    marca = input('Qual a marca dele? ').capitalize()
    limpar()
    while True:
        ano = input('Qual o ano dele? (XXXX) ')
        limpar()
        if not ano.isdigit():
            print('Isso não é um número!')
            continue            

        if len(ano) < 4:
            print('Digite o ano completo!')
            continue

        if len(ano) > 4:
            print('Digite o ano certo!')
            continue

        if int(ano) > 2025 or int(ano) < 1900:
            print('talvez tenha digitado o ano errado, tente novamente!')
            continue
        break

    cor = input('Qual a cor dele? ').capitalize()
    limpar()
    marca_ano_cor = [f'Marca: {marca}',f'Ano: {ano}', f'Cor: {cor}']
    Carros_usuario[nome] = marca_ano_cor
"""Fim"""

"""Função que cadastra o primeiro carro"""
def bemvindo():
    print('Bem vindo, Usuário!')
    cadastro()
"""Fim"""

"""Váriavel que acumula os carros cadastrados em um dicionario"""
Carros_usuario = {}
"""Fim"""

"""Funcionamento"""
while True:
    if len(Carros_usuario) < 1:
        bemvindo()
    if len(Carros_usuario) >= 1:
        continuar = input('Deseja cadastrar outro carro? [S]im [N]ão: ').lower()
        limpar()
        
        if continuar.isdigit():
            print('Opção desconhecida, digite corretamente!')
            continue
        
        if continuar == 's':
            cadastro()
        else:
            break

for allcar in Carros_usuario:
    print(f'nome: {allcar}')
    for cor_ano_marca in Carros_usuario[allcar]:
        print(cor_ano_marca)
    print()
"""Fim"""