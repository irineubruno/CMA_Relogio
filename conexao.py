"""
Class Coenxao  condig: utf-8
autor: Bruno Irineu Silva do Nascimento 2022-06-12

instalado 'pip install mysql-connector-python'
           'pip install mysqlclient'
"""
import MySQLdb

host = "localhost"
user = "bruno"
password = "bb172839"
db = "ponto"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

"""
Retornar na forma de dicionario

Assim retorna com matrix  c = con.cursor()
"""
c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):
    global c
    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where
    c.execute(query)
    return c.fetchall()

#result = select("paci_cpf as cpf, paci_nome as nome", "paciente")

#print(result[0]['cpf'], result[0]['nome'])

def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES "+", ".join(["(" + v + ")" for v in values])
    print(query)
    c.execute(query)
    con.commit()


def update(sets, table, where=None):

    global c, con

    query = "UPDATE " + table
    query = query + " SET "+",".join([field + " = " + value + "'" for field, value in sets.item()])

'''
values1 = []
values1.append("'Maria 1', 'Rua Destrito Federal 3355, setor 05', '1997-04-01', 'M', '027.572.502.21'")
values1.append("'João 0k', 'Rua Destrito Federal 3355, setor 05', '1997-04-01', 'M', '027.572.502.21'")

insert(values1, "paciente", "paci_nome, paci_endereco, paci_dt_nacimento, paci_sexo, paci_cpf")
'''