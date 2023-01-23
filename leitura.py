import pandas as pd
from datetime import date

f = open('registro.txt', 'r')
cont = 0
texto = ''
nsr = []
marcacao = []
data = []
hora = []
pis = []

#gab_comissionado = ['016261']
# if len(line) < 40 and line[22:34] in gab_comissionado:
#if len(line) < 40 and line[22:34] == '012872351657':

for line in f:
    if len(line) < 40:
        print(80 * "-")
        print('Leitura linha: {} '.format(cont))
        print('Valor AFD: {}'.format(line))
        print('Tamanho Linha AFD: {}'.format(len(line)))
        texto = line
        print('NSR..............[00-09] : {}'.format(line[:9]))
        print('Tipo de marcação.[09-10] : {}'.format(line[9:10]))
        print('Data............ [10-18] : {}/{}/{}'.format(line[10:12], line[12:14], line[14:18]))
        data.append('{}/{}/{}'.format(line[10:12], line[12:14], line[14:18]))
        #print('Data............ [10-18] : {}-{}-{} {}:{}'.format(line[14:18], line[12:14], line[10:12], line[18:20],line[20:22]))
        #data.append('{}-{}-{} {}:{}'.format(line[14:18], line[12:14], line[14:18], line[18:20], line[20:22]))
        print('Hora.............[18-22] : {}:{}'.format(line[18:20], line[20:22]))
        hora.append('{}:{}'.format(line[18:20], line[20:22]))
        print('PIS............  [22-34] : {}'.format(line[22:34]))  # 013185391488
        pis.append(line[22:34])
        cont += 1
        #if ('{}/{}/{}'.format(line[10:12], line[12:14], line[14:18]) == '13/05/2022' and '{}:{}'.format(line[18:20], line[20:22]) == '11:56' ):
         #   input('Enter continuar')
        #input('Enter continuar')


#insert into registro (reg_nsr, reg_pis, reg_tipo_marcacao, reg_data) values ();



def arquivo(marcacao):
    reg = open(marcacao,'r')
    values = []
    exececao = []
    for line in reg:
        if len(line) < 40:
            values.append("{}, '{}', {}, '{}-{}-{} {}:{}'".format(line[:9], line[22:34], line[9:10], line[14:18], line[12:14], line[10:12], line[18:20], line[20:22]))
        else:
            exececao.append(line)
    print(exececao)
    return values
d = {'pis': pis, 'data': data, 'hora': hora}
dados = pd.DataFrame(data=d)
dados.to_excel(f'dados_{date.today()}.xlsx', index=False)
#print(pis)
#input('Enter continuar')
#print(data)
#input('Enter continuar')
#print(hora)
#input('Enter continuar')
#print(dados)
#input('Enter continuar')

