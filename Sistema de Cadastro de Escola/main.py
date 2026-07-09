import pyodbc

dados_conexao = (
    "Driver={MySQL ODBC 9.7 ANSI Driver};"
    "Server=localhost;"
    "port=3306;"
    "UID=root;"
    "PWD=2010;"
    "Database=escola;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

print('Sistema de cadastro de alunos com Python e SQL')

menu = int(input("""MENU: 
1) Registrar Aluno
2) Atualizar Infos
3) Excluir Aluno
4) Consulta

Escolha uma opcao (1-4): """))

nome = ' '.strip().lower()
idade = ' '
sala = ' '

def validarcad():
    if not nome or not isinstance(nome,str):
        print('Erro no cadastro.')
        return False
    elif not isinstance(idade,int) or (idade < 3 or idade > 22):
        print('Erro no cadastro.')
        return False
    elif not isinstance(sala,int) or sala < 1 or sala > 50:
        print('Erro no cadastro.')
        return False

    return True

def validarat():
    if opc == 1:
        if not nome.strip():
            print("Erro na atualização.")
            return False

    elif opc == 2:
        if not isinstance(idade, int) or idade < 3 or idade > 22:
            print("Erro na atualização.")
            return False

    elif opc == 3:
        if not isinstance(sala, int) or sala < 1 or sala > 50:
            print("Erro na atualização.")
            return False

    elif opc == 4:
        if not nome.strip():
            print("Erro na atualização.")
            return False

        if not isinstance(idade, int) or idade < 3 or idade > 22:
            print("Erro na atualização.")
            return False

        if not isinstance(sala, int) or sala < 1 or sala > 50:
            print("Erro na atualização.")
            return False

    return True

def cadastro():
    cmdcadastro = """
    INSERT INTO alunos(nome, idade, sala) values 
    (?,?,?);
    """
    cursor.execute(cmdcadastro, (nome, idade, sala))
    conexao.commit()

def atualizar():
    if opc == 1:
        cmdatualizar = """
        update alunos
        set nome = ?
        where id = ?;
        """
        cursor.execute(cmdatualizar, (nome, atid))
    elif opc == 2:
        cmdatualizar = """
        update alunos
        set idade = ?
        where id = ?;
        """
        cursor.execute(cmdatualizar, (idade, atid))
    elif opc == 3:
        cmdatualizar = """
        update alunos
        set sala = ?
        where id = ?;
        """
        cursor.execute(cmdatualizar, (sala, atid))
    elif opc == 4:
        cmdatualizar = """
        update alunos
        set nome = ? idade = ? sala = ?
        where id = ?;
        """
        cursor.execute(cmdatualizar, (nome, idade, sala, atid))

    conexao.commit()

def validarexc():
    if not isinstance(idexc, int) or idexc < 1:
        print('Erro na exclusao')
        return False

    return True

def exluiral():
    cmdexc = """
    delete from alunos
    where id = ?;
    """
    cursor.execute(cmdexc, idexc)
    conexao.commit()

def consultaal():
    cursor.execute("select * from alunos where id = ?", idcons)
    aluno = cursor.fetchone()

    if aluno:
        print(f"""
    ID: {aluno[0]}
    Nome: {aluno[1]}
    Idade: {aluno[2]}
    Sala: {aluno[3]}
    """)
    else:
        print("Aluno não encontrado.")

def validarcons():
    if not isinstance(idcons, int) or idcons < 1:
        print('Erro na consulta.')
        return False

    return True

if menu == 1:
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    sala = int(input('Digite o numero da sala aluno: '))
    if validarcad():
        cadastro()
        print('Aluno cadastrado com sucesso.')
elif menu == 2:
    opc = 0
    atid = int(input('Digite o ID do aluno que deseja atualizar: '))
    oqatualizar = input('Perfeito! Agora digite oque deseja atualizar: ').strip()
    if oqatualizar.lower() == 'nome':
        opc = 1
        nome = str(input('Digite o nome do aluno: '))
        if validarat():
            atualizar()
            print('Aluno atualizado com sucesso.')
    elif oqatualizar.lower() == 'idade':
        opc = 2
        idade = int(input('Digite o idade do aluno: '))
        if validarat():
            atualizar()
            print('Aluno atualizado com sucesso.')
    elif oqatualizar.lower() == 'sala':
        opc = 3
        sala = int(input('Digite o numero da sala aluno: '))
        if validarat():
            atualizar()
            print('Aluno atualizado com sucesso.')
    elif ('nome' and 'idade' and 'sala') in oqatualizar.lower():
        opc = 4
        nome = str(input('Digite o nome do aluno: '))
        idade = int(input('Digite o idade do aluno: '))
        sala = int(input('Digite o numero da sala aluno: '))
        if validarat():
            atualizar()
            print('Aluno atualizado com sucesso.')
elif menu == 3:
    idexc = int(input('Digite o ID do aluno que deseja excluir: '))
    if validarexc():
        exluiral()
        print('Aluno exlcuido com sucesso.')
elif menu == 4:
    idcons = int(input('Digite o ID do aluno que deseja consultar: '))
    if validarcons():
        consultaal()