import json
import professores
import disciplinas
import turmas
import matriculas
import alunos
def menu():
    print('Selecione um módulo')
    print('[1] Professores')
    print('[2] Diciplinas')
    print('[3] Turmas')
    print('[4] Matrículas')
    print('[5] Alunos')
    print('[0] Sair')

def submenu():
    print('Escolha uma ação')
    print('[1] Cadastrar')
    print('[2] Visualizar')
    print('[3] Editar')
    print('[4] Apagar')
    print('[0] Sair')

menu()
op = int(input())

while op != 0: 
    if op == 1:
        print("Professores")
        submenu()
        subop = int(input())
        if subop == 1:
            professores.cadastrar()
        elif subop ==2:
            professores.visualizar()
        elif subop == 3: 
            professores.editar()
        elif subop == 4:
            professores.apagar()
        else :
            print('Escolha invalida')
    elif op == 2:
        print("Diciplinas") 
        submenu()
        subop = int(input())
        if subop == 1:
            disciplinas.cadastrar()
        elif subop ==2:
            disciplinas.visualizar()
        elif subop == 3: 
            disciplinas.editar()
        elif subop == 4:
            disciplinas.apagar()
        else :
            print('Escolha invalida')
    elif op == 3:
        print("Turmas") 
        submenu()
        subop = int(input())
        if subop == 1:
            turmas.cadastrar()
        elif subop ==2:
            turmas.visualizar()
        elif subop == 3: 
            turmas.editar()
        elif subop == 4:
            turmas.apagar()
        else :
            print('Escolha invalida')    
    elif op == 4:
        print('Matrículas')
        submenu()
        subop = int(input())
        if subop == 1:
            matriculas.cadastrar()
        elif subop ==2:
            matriculas.visualizar()
        elif subop == 3: 
            matriculas.editar()
        elif subop == 4:
            matriculas.apagar()
        else :
            print('Escolha invalida')
    elif op == 5:
        print('Alunos')
        submenu()
        subop = int(input())
        if subop == 1:
            alunos.cadastrar()
        elif subop ==2:
            alunos.visualizar()
        elif subop == 3: 
            alunos.editar()
        elif subop == 4:
            alunos.apagar()
        else :
            print('Escolha invalida')
    else:
        print("\nSelecione uma opção válida\n\n")
    menu()
    op = int(input())

print("Obrigado por usar o sistema.")