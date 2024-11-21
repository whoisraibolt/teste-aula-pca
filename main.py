'''
Crie um arquivo chamado exemplo.txt e escreva nele algum texto, como
"Olá, este é um exemplo de leitura em Python.". Depois, escreva um código em Python
que abra este arquivo, leia o conteúdo e o exiba no console.
'''


# # Código para criar o arquivo exemplo.txt
# with open('exemplo.txt', 'w') as arquivo:
#     arquivo.write('Olá, este é um exemplo de leitura em Python.')


# # Código para criar o arquivo exemplo.txt
# texto = open('exemplo.txt', 'w', encoding = 'utf-8')

# # Escrevendo no arquivo exemplo.txt
# texto.write('Olá, este é um exemplo de leitura em Python.')

# # Ler o arquivo exemplo.txt
# texto = open('exemplo.txt', 'r', encoding = 'utf-8')

# # Exibir o conteúdo do arquivo exemplo.txt
# print(texto.read())

# # Fechar o arquivo exemplo.txt
# texto.close()

# print('Finalizado!')


# # Lista com as linhas do arquivo exemplo.txt
# lista = [
#     'Olá, este é um exemplo de leitura em Python.',
#     'Esse é o segundo exemplo de leitura em Python.',
#     'Esse é o terceiro exemplo de leitura em Python.'
# ]

# # Código para criar o arquivo exemplo_2.txt
# texto = open('exemplo_2.txt', 'w', encoding = 'utf-8')

# # Escrevendo no arquivo exemplo_2.txt
# for linha in lista:
#     texto.write(linha + '\n')

# print('Finalizado!')

# # TODO: Não se esqueça de fechar o arquivo

# Importando biblioteca csv
import csv

# Criando o arquivo exemplo_3.csv
texto = open('exemplo_3.csv', 'w', newline = '', encoding = 'utf-8')

# Criando o objeto de escrita
escritor = csv.writer(texto, delimiter = ';')

# Escrevendo o cabeçalho
escritor.writerow(['Nome', 'Idade', 'Cidade'])

# Escrevendo os dados
escritor.writerow(['Carlos', 30, 'São Paulo'])
escritor.writerow(['Maria', 25, 'Rio de Janeiro'])
escritor.writerow(['José', 21, 'Curitiba'])
escritor.writerow(['Ana', 35, 'Belo Horizonte'])
escritor.writerow(['Pedro', 40, 'Salvador'])

# Fechando o arquivo
texto.close()

print('Finalizado!')
