import json
import os

def validaMatricula(id):
    if os.path.isfile('./data_matriculas.json'):
        with open('data_matriculas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
    else:
        return True
    
    for index in range(len(data_arr)):
        for key in data_arr[index]:
            if data_arr[index]['Codigo do estudante'] == id:
                return False
    return True

def cadastrar():
    data_arr = []
    print('Cadastrar\n\n')
    if os.path.isfile('./data_matriculas.json'):
        with open('data_matriculas.json', 'r', encoding='utf-8') as f:
            my_data = json.load(f)
            data_arr = my_data
            
    
    data_raw = {}
    cad = True
    while cad:
        codigo_da_dscipina = int(input("Codigo da turma\n"))
        codigo_do_estudante = int(input("Codigo do estudante:\n"))


        data_raw.update({
            'Codigo da turma':codigo_da_dscipina,
            'Codigo do estudante':codigo_do_estudante,
            })
        valida = validaMatricula(codigo_do_estudante)
        if valida:
            data_arr.append(data_raw)
            with open ('data_matriculas.json', "w") as f:
                json.dump(data_arr, f)
                print('Cadastro efetuado')
        else: 
            print('Matricula ja cadastrada')
        cad = False

def visualizar():
    if os.path.isfile('./data_matriculas.json') == False:
        print('Nada cadastrado')
    else:
        print('Visualizar\n\n')

        with open('data_matriculas.json', 'r', encoding='utf-8') as f:
            data_arr = json.load(f)
            i = 1
            for index in data_arr:  
                print('Item :'+str(i))              
                print('Codigo da turma: '+str(index['Codigo da turma']))                  
                print('Codigo do estudante: '+str(index['Codigo do estudante']))              
                print('\n\n')
                i+=1


def editar():
    print('Editar')
    if os.path.isfile('./data_matriculas.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_matriculas.json'):
            with open('data_turmas.json', 'r', encoding='utf-8') as f:
                my_data = json.load(f)
                data_arr = my_data
                data = my_data
        print(my_data)
        op = int(input("Digite codigo da turma: \n\n"))
        
        for i in range(len(my_data)):
            if my_data[i]['Codigo da turma'] == op:
                codigo_da_turma = int(input("Codigo da turma\n"))
                codigo_do_estudante = input("Codigo do estudante\n")
              
                
                my_data[i]['Codigo da turma'] = codigo_da_turma
                my_data[i]['Codigo do estudante'] = codigo_do_estudante
                with open ('data_matriculas.json', "w") as f:
                    json.dump(my_data, f)
                
                break

def apagar():
    print('Apagar Cadastro')
    if os.path.isfile('./data_prof.json') == False:
        print('Nada cadastrado')
    else:
        data = []
        if os.path.isfile('./data_matriculas.json'):
            with open('data_matriculas.json', 'r', encoding='utf-8') as f:
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
                with open ('data_matriculas.json', "w") as f:
                    json.dump(my_data, f)
                    print('Cadastro Apagado')
                    break