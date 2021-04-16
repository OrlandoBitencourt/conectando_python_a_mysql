import MySQLdb


try:
    conn = MySQLdb.connect(db="llama", host="localhost", port=3306, user="root")
except:
    print("Não foi possivel conectar ao banco de dados!")
print("Conectado!")

cursor = conn.cursor()


# """SELECT"""
query = "select * from aqui"

cursor.execute(query)

consulta = cursor.fetchall()

for col in cursor.description:
    print(col[0])
#
# for i in range(len(consulta)):
#     print("\n")
#     print(f"{consulta[i][0]};{consulta[i][1]};{consulta[i][2]}")
#     # print(consulta[i][0])
#     # print(consulta[i][1])
#     # print(consulta[i][2])
#     print("\n")


# """INSERT"""
# nome = input("nome: ")
# cpf = input("cpf: ")
# sql = f"insert into aqui " \
#       f"(nome, cpf) " \
#       f"values ('{nome}', '{cpf}')"
# cursor.execute(sql)
# conn.commit()

# nome = input("nome: ")
# cpf = input("cpf: ")
# sql = "insert into aqui values (default, ?, ?)"
# cursor.execute(sql, [nome, cpf])
# conn.commit()


# """UPDATE"""
# id = int(input("id a alterar: "))
# nome = input("novo nome: ")
# cpf = input("novo cpf: ")
# sql = f"update aqui " \
#       f"set nome='{nome}', " \
#       f"cpf='{cpf}' " \
#       f"where id = {id}"
# cursor.execute(sql)
# conn.commit()


# """DELETE"""
# id = int(input("id a deletar: "))
# sql = f"delete from aqui where id = {id}"
# cursor.execute(sql)
# conn.commit()