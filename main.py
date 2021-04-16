from banco_de_dados import BancoDeDados


"""
    1.	Criar uma classe para o banco de dados

    2.	Criar funções para todas as operações de CRUD
    
    3.	Deve ser possível executar as funções com e sem WHERE
    
    4.	A listagem (em print()) deve ser feita em formato de tabela
    •	Ex: 
    •	Nome – Cpf – Idade – Altura
    •	Gustavo – 000 – 100 – 1.8
    •	Amanda – 154 – 45 – 1.64
    
    5.	Deve ser feito o tratamento de erro para caso o usuário faça besteira (exceto em coisas sem controle do programador. Ex: problema interno do banco)

"""
def validar_campo_float(nome_campo):
    while True:
        valor = 0.0
        valor = input(f"\ninforme valor para {nome_campo}: ")
        try:
            valor = float(valor)
        except:
            valor = 0.0
            print(f"valor incorreto para {nome_campo}.")

        if valor != 0.0 and valor != None:
            return valor

def validar_campo_int(nome_campo):
    while True:
        valor = 0
        valor = input(f"\ninforme valor para {nome_campo}: ")
        try:
            valor = int(valor)
        except:
            valor = 0
            print(f"valor incorreto para {nome_campo}.")

        if valor != 0 and valor != None:
            return valor


def validar_campo_cpf():
    while True:
        cpf = ""
        cpf = input("\ncpf: ")

        if len(cpf) == 11:
            for i in cpf:
                if i not in "0123456789":
                    pass
            else:
                return cpf
        print("Valor incorreto para o cpf, digite 11 numeros.")

def listar_valores(sql):
    cabecalho_consulta, consulta = db.executar_select(sql)
    print(f"{cabecalho_consulta[0][0]} - {cabecalho_consulta[1][0]} - {cabecalho_consulta[2][0]} - {cabecalho_consulta[3][0]} - {cabecalho_consulta[4][0]}")
    for i in range(len(consulta)):
        print(f"{consulta[i][0]} - {consulta[i][1]} - {consulta[i][2]} - {consulta[i][3]} - {consulta[i][4]}")
    return True

db = BancoDeDados()
db.conectarDB()

while True:
    menu = input("""
    1 - CADASTRAR
    2 - LISTAR
    3 - ATUALIZAR
    4 - DELETAR
    5 - SAIR
    Informe a opção desejada: """)
    if menu not in ("12345"):
        break
    else:
        if menu == "1":

            while True:
                nome = input("nome: ")
                if nome != "":
                    break

            cpf = validar_campo_cpf()

            idade = validar_campo_int("idade")

            altura = validar_campo_float("altura")

            sql = f"insert into aqui " \
                  f"(nome, cpf, idade, altura) " \
                  f"values ('{nome.capitalize()}', '{cpf}', {idade}, {altura})"

            db.executar_insert(sql)

        elif menu == "2":

            while True:
                menu_lista = input("""
                1 - Listar tudo
                2 - Listar por id
                3 - Listar por nome
                4 - Listar por cpf
                5 - Listar por idade
                6 - Listar por altura
                7 - Voltar
                informe a opção desejada: """)
                if menu_lista not in ("1234567"):
                    break
                else:
                    if menu_lista == "1":

                        sql = "select * from aqui"
                        listar_valores(sql)

                    elif menu_lista == "2":

                        sql = "select * from aqui"
                        listar_valores(sql)

                        id = validar_campo_int("id")

                        sql = f"select * from aqui where id = {int(id)}"
                        listar_valores(sql)

                    elif menu_lista == "3":

                        sql = "select * from aqui"
                        listar_valores(sql)

                        while True:
                            nome = ""
                            nome = input("\nnome: ")
                            if nome != "":
                                break

                        sql = f"select * from aqui where nome = '{nome.capitalize()}'"
                        listar_valores(sql)

                    elif menu_lista == "4":

                        sql = "select * from aqui"
                        listar_valores(sql)

                        cpf = validar_campo_cpf()

                        sql = f"select * from aqui where cpf = '{cpf}'"
                        listar_valores(sql)
                        pass

                    elif menu_lista == "5":

                        sql = "select * from aqui"
                        listar_valores(sql)

                        while True:
                            idade = input("\nidade: ")
                            try:
                                idade = int(idade)
                            except:
                                print("valor incorreto para idade.")

                            if idade != "":
                                break

                        sql = f"select * from aqui where idade = {idade}"
                        listar_valores(sql)

                    elif menu_lista == "6":

                        sql = "select * from aqui"
                        listar_valores(sql)

                        while True:
                            altura = input("\naltura: ")
                            try:
                                altura = float(altura)
                            except:
                                print("valor incorreto para altura.")

                            if altura != "":
                                break
                        sql = f"select * from aqui where altura like '{str(altura)}%'"
                        listar_valores(sql)

                    elif menu_lista == "7":

                        break

        elif menu == "3":
            while True:

                menu_alterar = input("\n1 - Alterar "
                                     "\n2 - Voltar"
                                     "\nDigite a opção desejada: ")
                if menu_alterar == "1":

                    sql = "select * from aqui"
                    listar_valores(sql)

                    id = validar_campo_int("id")

                    while True:
                        nome = input("nome: ")
                        if nome != "":
                            break

                    cpf = validar_campo_cpf()

                    idade = validar_campo_int("idade")

                    altura = validar_campo_float("altura")

                    sql = f"update aqui " \
                          f"set nome ='{nome.capitalize()}', cpf ='{cpf}', idade = {idade}, altura = {altura}" \
                          f"where id = {id}"

                    db.executar_update(sql)
                elif menu_alterar == "2":
                    break

        elif menu == "4":
            while True:
                menu_deletar = input("\n1 - Deletar por id"
                                     "\n2 - Deletar TUDO"
                                     "\n3 - Voltar"
                                     "\nDigite a opção desejada: ")
                if menu_deletar == "1":

                    sql = "select * from aqui"
                    listar_valores(sql)

                    id = validar_campo_int("id")

                    sql = f"delete from aqui " \
                          f"where id = {id}"

                    db.executar_delete(sql)

                elif menu_deletar == "2":
                    sql = f"delete from aqui"
                    db.executar_delete(sql)
                elif menu_deletar == "3":
                    break

        elif menu == "5":
            break