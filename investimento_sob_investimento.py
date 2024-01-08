#calculadora de investimento sob investimento

import os
import matplotlib.pyplot as plt

def investimento(principal, taxa, adicao_mensal, tempo, mes_anterior=0):
    valores = []
    for mes in range(1, tempo+1):
        if mes == 1:
            valor_mensal = principal + adicao_mensal + mes_anterior
        else:
            valor_mensal = valores[mes-2] * (1 + taxa) + adicao_mensal
        valores.append(valor_mensal)
    return valores


principal = float(input('Valor do investimento inicial: '))
taxa = float(input('Taxa de rendimento mensal: '))
adicao_mensal = float(input('Valor da mensalidade: '))
tempo = int(input('Duração do investimento em meses: '))

valores = investimento(principal, taxa, adicao_mensal, tempo)
print()
print()
print("Valor final do investimento após {} meses: R${:.2f}".format(tempo, valores[-1]))
print()

resultadosantigos = []
mes_anterior = 0 
try:
    with open('resultados.txt', 'r') as f:
        for linha in f:
            resultadosantigos.append(float(linha.strip()))
        if len(resultadosantigos) > 0:
            mes_anterior = resultadosantigos[-1]
except FileNotFoundError:
    pass


valores = investimento(principal, taxa, adicao_mensal, tempo, mes_anterior)

resultados_totais = resultadosantigos + valores
with open('resultados.txt', 'w') as f:
    for resultado in resultados_totais:
        f.write(str(resultado) + '\n')

toodles = input('deseja fazer a visualizacao do grafico? (s/n): ')
if toodles == 's' and 'S':
    with open('resultados.txt', 'r') as f:
        valores = [float(linha.strip()) for linha in f]
    meses = list(range(1, len(valores)+1))
    plt.bar(meses, valores)
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title('Evolução do investimento ao longo do tempo')
    plt.show()

    print()
    deletar = input('Deseja excluir os dados atuais? (s/n): ')
    if deletar == 's' and 'S':
        with open('resultados.txt', 'w') as f:
            f.write('')