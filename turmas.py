import json
import os

def validaTurma(id):
    if os.path.isfile('./data_turmas.json'):
        with open('data_turmas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
    else:
        return True
    
    for index in range(len(data_arr)):
        for key in data_arr[index]:
            if data_arr[index]['Codigo da turma'] == id:
                return False
    return True 


def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_turmas.json'):
        with open('data_turmas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_da_turma = int(input("Codigo da turma\n"))
        codigo_do_professor = int(input("Codigo do professor:\n"))
        codigo_da_disciplina = int(input("Codigo da disciplina:\n"))
        
        data_raw.update({
            'Codigo da turma':codigo_da_turma,
            'Codigo do professor':codigo_do_professor,
            'Codigo da disciplina':codigo_da_disciplina
            })
        valida = validaTurma(codigo_da_turma)
        if valida:
            data_arr.append(data_raw)
            with open ('data_turmas.json', "w") as f:
                json.dump(data_arr, f)
                print('Cadastro efetuado')
        else:
            print('Turma ja cadastrada')
        cad = False

def visualizar():
    if os.path.isfile('./data_turmas.json') == False:
        print('Nada cadastrado')
    else:
        print('Visualizar\n\n')

        with open('data_turmas.json', 'r', encoding='utf-8') as f:
            data_arr = json.load(f)
            i = 1
            for index in data_arr:  
                print('Item :'+str(i))              
                print('Codigo da turma: '+str(index['Codigo da turma']))                  
                print('Codigo do professor: '+str(index['Codigo do professor']))
                print('Codigo da disciplina: '+str(index['Codigo da disciplina']))                
                print('\n\n')
                i+=1


def editar():
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        print('Editar')
        data = []
        if os.path.isfile('./data_turmas.json'):
            with open('data_turmas.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da Turma: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da turma'] == op:
                codigo_da_turma = int(input("Codigo da turma\n"))
                codigo_do_professor = int(input("Codigo do professor:\n"))
                codigo_da_disciplina = int(input("Codigo da disciplina:\n"))
              
                
                my_data[i]['Codigo da turma'] = codigo_da_turma
                my_data[i]['Codigo do professor'] = codigo_do_professor
                my_data[i]['Codigo do disciplina'] = codigo_da_disciplina
                with open ('data_turmas.json', "w") as f:
                    json.dump(my_data, f)
               
                break

def apagar():
    print('Apagar Cadastro')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_turmas.json'):
            with open('data_turmas.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da turma: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da turma'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_turma.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break