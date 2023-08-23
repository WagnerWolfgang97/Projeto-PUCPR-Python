import json
import os

def validaUser(cpf):
    if os.path.isfile('./data_aluno.json'):
        with open('data_aluno.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
    else:
        return True
    
    for index in range(len(data_arr)):
        for key in data_arr[index]:
            if data_arr[index]['CPF do aluno'] == cpf:
                return False
    return True            


def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_aluno.json'):
        with open('data_aluno.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_do_aluno = int(input("Codigo do aluno\n"))
        nome_do_aluno = input("Nome do aluno\n")
        CPF_do_aluno = input("CPF do aluno\n")

        data_raw.update({
            'Codigo do aluno':codigo_do_aluno,
            'Nome do aluno':nome_do_aluno,
            'CPF do aluno':CPF_do_aluno
            })
        valida = validaUser(CPF_do_aluno)
        if valida:
            data_arr.append(data_raw)
            with open ('data_aluno.json', "w") as f:
                json.dump(data_arr, f)
                print('Cadastro efetuado')
        else:
            print("Usuario ja cadastrado")
        cad = False

def visualizar():
    print('Visualizar\n\n')
    if os.path.isfile('./data_aluno.json') == False:
        print('Nada cadastrado')
    else:
        with open('data_aluno.json', 'r', encoding='utf-8') as f:
            data_arr = json.load(f)
            lista = []
            i = 1
            for index in data_arr:  
                print('Item :'+str(i))              
                print('Codigo do aluno: '+str(index['Codigo do aluno']))                  
                print('Nome do aluno: '+index['Nome do aluno'])              
                print('CPF do aluno: '+str(index['CPF do aluno'])) 
                print('\n\n')
                i+=1



def editar():
    print('Editar')
    if os.path.isfile('./data_aluno.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_aluno.json'):
            with open('data_aluno.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo do aluno: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo do aluno'] == op:
                codigo_do_aluno = int(input("Codigo do aluno\n"))
                nome_do_aluno = input("Nome do aluno\n")
                CPF_do_aluno = input("CPF do aluno\n")
                
                my_data[i]['Codigo do aluno'] = codigo_do_aluno
                my_data[i]['Nome do aluno'] = nome_do_aluno
                my_data[i]['CPF do aluno'] = CPF_do_aluno
                
                
                with open ('data_aluno.json', "w") as f:
                    json.dump(my_data, f)
                
                break

def apagar():
    print('Apagar Cadastro')
    if os.path.isfile('./data_aluno.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_aluno.json'):
            with open('data_aluno.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo do aluno: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo do aluno'] == op:
                print(my_data[i])
                del my_data[i]
                print(my_data)
                with open ('data_aluno.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break