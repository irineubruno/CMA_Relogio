import coletar
import conexao
import leitura

coletar.pagina_acesso('http://10.10.10.210')
coletar.login('bruno', '172839')
coletar.seleciona_eventos('15/07/22 00:00', '16/08/22 23:59')
coletar.sair_pagina()
'''
#insert into registro (reg_nsr, reg_pis, reg_tipo_marcacao, reg_data) values ();
'''

#conexao.insert(leitura.arquivo('registro.txt'), 'registro', 'reg_nsr, reg_pis, reg_tipo_marcacao, reg_data')
