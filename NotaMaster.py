#definir nota de 0 a 10
def obter_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
            return nota
        else:
            print('nota invalida, favor digitar nota de 0 a 10.')

#solicitar notas
nota1= obter_nota('Qual a nota da prova 1?')
nota2= obter_nota('qual a nota da prova 2?')
nota3= obter_nota('qual a nota da prova 3?')

#calcular a media
media= (nota1+nota2+nota3) / 3

#recuperacao automatica em caso de nota0 em alguma prova
if nota1 == 0 or nota2 == 0 or nota3 == 0:
    tmedia = 'em recuperacao'

 # ponto extra em caso de nota 7 ou + em ao menos duas das provas
elif (nota1 >= 7) + (nota2 >= 7) + (nota3 >=7) >= 2:
    media += 1
    tmedia = 'aprovado com ponto extra'

#aprovacao em caso de uma das notas for 10, em caso de ter um 10 e um 0, segue regra de recuperacao
elif media >= 6 < 7 and (nota1 == 10 or nota2 == 10 or nota3 == 10):
    tmedia = "aprovado por ter gabaritado uma prova"
elif 5 < media < 7:
    tmedia = 'em recuperacao'

#resto normal das condicoes
elif media>=7:
    tmedia = "aprovado"
else:
    tmedia = "reprovado"

print(f'o aluno está {tmedia} com media {media:.2f}')

git remote add origin https://github.com/Eairod/NotaMaster.git
git branch -M main
git push -u origin main