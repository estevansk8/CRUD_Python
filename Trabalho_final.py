###############################################################################################################
#                                                    MAIN
###############################################################################################################

def main():
    matrizprof = abreprof()
    matrizdisc = abredisc()
    matrizprofdisc = abreprofdisc()

    menup(matrizprof,matrizdisc,matrizprofdisc)

###############################################################################################################
#                                                    ABRIR ARQUIVOS
###############################################################################################################

def abreprof():
    arq = open('prof.txt','r')
    conteudoarquivo = arq.readlines()
    matrizprof = [] 
    for linha in conteudoarquivo:
        # se tem @ append na posição de indice 7 QUE SERÁ A LISTA DE EMAIL [] se é só numeros append na posição 8 QUE SERÁ A LISTA DE TELEFONES, É ESSE PROBLEMA QUE PRECISAREMOS RES fecho kkk
        linha = linha.split('|')
        novalinha = []
        linha[0]=linha[0].split()
        for i in linha[0]:
            novalinha.append(i)
        linha[1] = linha[1].split()
        novalinha.append(linha[1])
        linha[2] = linha[2].split()
        novalinha.append(linha[2])
        matrizprof.append(novalinha)
    arq.close()
    return matrizprof

def abredisc():
    arq = open('disc.txt','r')
    conteudoarquivo = arq.readlines()
    matrizdisc = [] 
    for linha in conteudoarquivo:
        linha = linha.split()
        matrizdisc.append(linha)
        print('\n')
    arq.close()
    return matrizdisc

def abreprofdisc():
    arq = open('profdisc.txt','r')
    conteudoarquivo = arq.readlines()
    matrizprofdisc = [] 
    for linha in conteudoarquivo:
        linha = linha.split('|')
        novalinha = []
        linha[0]=linha[0].split()
        for i in linha[0]:
            novalinha.append(i)
        linha[1] = linha[1].split()
        novalinha.append(linha[1])
        linha[2] = linha[2].split()
        novalinha.append(linha[2])
        matrizprofdisc.append(novalinha)
    arq.close()
    return matrizprofdisc


###############################################################################################################
#                                                    FECHAR ARQUIVOS
###############################################################################################################
def fechaprof(matrizprof):
    arq = open("prof.txt","w")
    string = ""
    for i in matrizprof:
        i.insert(7,"|")
        i.insert(9,"|")
        string = str(i)
        string = string.replace("[","").replace("]","").replace(",","").replace("'","")
        arq.write(string)
        arq.write("\n")
    arq.close()

def fechadisc(matrizdisc):
    arq = open("disc.txt","w")
    string = ""
    for i in matrizdisc:
        string = str(i)
        string = string.replace("[","").replace("]","").replace(",","").replace("'","")
        arq.write(string)
        arq.write("\n")
    arq.close()

def fechaprofdisc(matrizprofdisc):
    arq = open("profdisc.txt", "w")
    string = ""
    for i in matrizprofdisc:
        i.insert(5,"|")
        i.insert(7,"|")
        string = str(i)
        string = string.replace("[","").replace("]","").replace(",","").replace("'","")
        arq.write(string)
        arq.write("\n")
    arq.close()


#################################################################################################################
#                                                 MENU PRINCIPAL
#################################################################################################################
def menup(matrizprof,matrizdisc,matrizprofdisc): 
    option = 1
    while option != 5:
        print("\n Menu principal \n 1. Professores \n 2. Disciplina \n 3. Professor-Disciplina \n 4. Relatórios \n 5. Sair")
        option = int(input("Selecione uma opção: "))
        while option < 0 and option > 6:
            option = int(input("Não existe essa seção, digite um número de 1 a 5: "))
        seletor(option,matrizprof,matrizdisc,matrizprofdisc)
    print('Encerrando...')

    ##################################################
    # ESCREVE AS ALTERAÇÕES E NOVOS DADOS NOS ARQUIVOS
    ##################################################

    fechaprof(matrizprof)
    fechadisc(matrizdisc)
    fechaprofdisc(matrizprofdisc)

def seletor(option,matrizprof,matrizdisc,matrizprofdisc): #LEVA PARA O MENU QUE O USUÁRIO ESCOLHEU
    if option == 1:
        menu1(matrizprof)
    elif option == 2:
        menu2(matrizdisc)
    elif option == 3:
        menu3(matrizprofdisc, matrizprof, matrizdisc)
    elif option == 4:
        relatorios(matrizprof,matrizdisc,matrizprofdisc)




########################################################################################################################
#                                                       PROFESSORES
########################################################################################################################
def menu1(matrizprof):
    option = 1
    while option != 6:
        print("\n Seção de Professores \n 1. Listar todos \n 2. Pesquisa  \n 3. Incluir \n 4. Alterar \n 5. Excluir \n 6. Menu Principal")
        option = int(input("\n Selecione uma opção: "))
        while option < 1 and option > 6:
            option = int(input("Não existe essa seção, digite um número de 1 a 6: "))
        
        if option == 1:
            print("Lista Completa") #listar todos
            for i in range(len(matrizprof)):
                print(matrizprof[i])
        
        elif option == 2:
            print("Pesquisa") #Pesquisa um elemento
            pesquisaprof(matrizprof)
        
        elif option == 3:
            print("INCLUIR") #Inclui um elemento
            matrizprof = incluirprof(matrizprof)
        
        elif option == 4:
            print("Alterar") #Altera um elemento
            alteraprof(matrizprof)
        
        elif option == 5:
            print("Excluir")
            matrizprof = excluiprof(matrizprof)

def incluirprof(matrizprof): #Incluir professor
    professor=[]
    dadosprofessor=["registro funcional: ", "nome: ", "data de nascimento: ", "sexo: ", "área de pesquisa: ", "titulação: ", "graduação: ", "emails: ", "telefones: "]


    #INSERE OS DADOS DO PROFESSOR ATÉ A GRADUAÇÃO
    x = 0
    
    while len(professor) < 7:
        if x == 0:
            print("Insira o registro funcional com 7 números.")#nao pode ter letra
        
        if x ==1:
            print("Insira o nome corretamente.")#nao pode ter numero
        
        if x == 2:
            print("Insira a data de nascimento correta conforme o padrão: xx/xx/xxxx.")#Colocar os intervalos corretos

        if x == 3:
            print("Insira 'M' para masculino e 'F' para feminino.")

        if x == 4:
            print("Digite a área de pesquisa corretamente.")#nao pode ter numero

        if x == 5:
            print("Digite a titulação corretamente.")#nao pode ter numero

        if x == 6:
            print("Digite a graduação corretamente.")#não pode ter número

            
        dado = input("Insira " + dadosprofessor[x])
        
    
        if x == 0:
            while verifica(matrizprof,dado):
                dado = input("Insira " + dadosprofessor[x])
            
                
        if x ==1:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if dado[i].isdigit(): 
                    dado = input("Insira " + dadosprofessor[x])
                    snumr=False
                i +=1
                           
        if x == 3:
            while dado != 'M' and dado !='F':
                dado = input("Insira " + dadosprofessor[x])

        if x == 4:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if dado[i].isdigit(): 
                    dado = input("Insira " + dadosprofessor[x])
                    snumr=False
                i +=1

        if x == 5:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if dado[i].isdigit(): 
                    dado = input("Insira " + dadosprofessor[x])
                    snumr=False
                i +=1

        if x == 6:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if dado[i].isdigit(): 
                    dado = input("Insira " + dadosprofessor[x])
                    snumr=False
                i +=1
            

        professor.append(dado)
        x += 1

    #INSERE OS EMAILS DO PROFESSOR NUMA SUBLISTA
    dado = 1
    email = []
    while dado != '0': 
        dado = input("Insira " + dadosprofessor[7] + "\n Finalizando digite 0: ")
        if dado != '0':
            email.append(dado)
    professor.append(email)

    #INSERE OS TELEFONES DO PROFESSOR NUMA SUBLISTA
    dado = 1
    telefone = []
    while dado != '0':
        print("Padrão: (xx)xxxxxxxxx")
        dado = input("Insira " + dadosprofessor[8] + "\n Finalizando digite 0: ")

        
        #criar uma estrutura para verificar se está dentro do padrão estabelecido
        if dado != '0':
            telefone.append(dado)
    professor.append(telefone)
    matrizprof.append(professor)
    return matrizprof

def excluiprof(matrizprof):
    registro = input("Digite o Registro Funcional para excluir o cadastro: ")
    #percorre a matriz coluna 0 todas as linhas se achar um igual exclui esse indice
    i=0
    achou = False
    while achou == False and i < len(matrizprof):
        if matrizprof[i][0] == registro:
            del matrizprof[i]
            achou = True
            print("Foi excluído com sucesso!")
        i += 1
    return matrizprof

def pesquisaprof(matrizprof):
    registro = input("Digite o registro funcional: ")
    i = 0
    achou = False
    while achou == False and i < len(matrizprof):
        if matrizprof[i][0] == registro:
            print(matrizprof[i])
            achou = True
        i += 1

def alteraprof(matrizprof):
    registro = input("Digite o registro funcional: ")
    coluna = int(input("Qual informação você gostaria de alterar? \n 1.Nome   2.Data de Nascimento   3.Sexo   4.Área de pesquisa   5.Titulação   6.Graduação   7.Emails   8.Telefones: "))
    i = 0
    achou = False
    while achou == False and i < len(matrizprof):
        if matrizprof[i][0] == registro:
            achou = True
            matrizprof[i][coluna] = input("Digite o novo dado: ")
        i += 1

############################################################################################################################
#                                                          DISCIPLINAS
##############################################################################################################################

def menu2(matrizdisc):
    option = 1
    while option != 6:
        print("\n Seção de Disciplinas \n 1. Listar todas \n 2. Pesquisa  \n 3. Incluir \n 4. Alterar \n 5. Excluir \n 6. Menu Principal")
        option = int(input("\n Selecione uma opção: "))
        while option < 1 and option > 6:
            option = int(input("Não existe essa seção, digite um número de 1 a 6: "))
        
        if option == 1:
            print("Lista Completa") #listar todos
            for i in range(len(matrizdisc)):
                print(matrizdisc[i])
        
        elif option == 2:
            print("Pesquisa") #Pesquisa um elemento
            pesquisadisc(matrizdisc)
        
        elif option == 3:
            print("INCLUIR") #Inclui um elemento
            matrizdisc = incluirdisc(matrizdisc)
        
        elif option == 4:
            print("Alterar") #Altera um elemento
            alteradisc(matrizdisc)
        
        elif option == 5:
            print("Excluir")
            matrizdisc = excluidisc(matrizdisc)

def incluirdisc(matrizdisc): #Incluir DISCIPLINA)
    disciplina=[]
    dadosdisciplina=["Sigla: ", "Nome: ", "Ementa: ", "Bibliografia: ", "Número de Créditos: ", "Carga Horária: "]

    #INSERE OS DADOS DA DISCIPLINA
    x = 0
    while x < 6:
        if x ==0:
            print("Digite uma sigla com até 4 caracteres.")
        
        if x ==1:
            print("Digite um nome valido." )

        if x==4:
            print("Digite somente o NÚMERO de créditos.")

        if x ==5:
            print("Digite somente o NÚMERO de horas. ")


        dado = input("Insira " + dadosdisciplina[x])

        if x ==0:
            while verifica(matrizdisc,dado):

                dado = input("Insira " + dadosdisciplina[x])

        if x ==1:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if dado[i].isdigit(): 
                    dado = input("Insira " + dadosdisciplina[x])
                    snumr=False
                i +=1
        

        if x ==4:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if not dado[i].isdigit(): 
                    dado = input("Insira " + dadosdisciplina[x])
                    snumr=False
                i +=1
        
        if x ==5:
            i=0
            snumr = True
            while i<len(dado) and snumr:
                if not dado[i].isdigit(): 
                    dado = input("Insira " + dadosdisciplina[x])
                    snumr=False
                i +=1
        disciplina.append(dado)
        x = x+1
    boleano = verifica(matrizdisc,disciplina)
    controlador = True # pode ser inserido :)
    if boleano:
        #menup(matrizprof,matrizdisc)
        controlador = False # não pode ser inserido ;(
    if controlador:
        matrizdisc.append(disciplina)
    return matrizdisc

def excluidisc(matrizdisc):
    sigla = input("Digite a sigla para excluir o cadastro: ")
    #percorre a matriz coluna 0 todas as linhas se achar um igual exclui esse indice
    i=0
    achou = False
    while achou == False and i < len(matrizdisc):
        if matrizdisc[i][0] == sigla:
            del matrizdisc[i]
            achou = True
            print("Foi excluído com sucesso!")
        i += 1
    return matrizdisc

def pesquisadisc(matrizdisc):
    sigla = input("Digite a sigla: ")
    i = 0
    achou = False
    while achou == False and i < len(matrizdisc):
        if matrizdisc[i][0] == sigla:
            print(matrizdisc[i])
            achou = True
        i += 1

def alteradisc(matrizdisc):
    sigla = input("Digite a sigla: ")
    coluna = int(input("Qual informação você gostaria de alterar? \n 1.Nome   2.Ementa   3.Bibliografia   4.Número de Créditos   5.Carga Horária: "))
    i = 0
    achou = False
    while achou == False and i < len(matrizdisc):
        if matrizdisc[i][0] == sigla:
            achou = True
            matrizdisc[i][coluna] = input("Digite o novo dado: ")
        i += 1

############################################################################################################################
#                                         PROFESSORES - DISCIPLINAS
##############################################################################################################################


def menu3(matrizprofdisc, matrizprof, matrizdisc):
    option = 1
    while option != 6:
        print("\n Seção de PROFESSOR-DISCIPLINA \n 1. Listar todas \n 2. Pesquisa  \n 3. Incluir \n 4. Alterar \n 5. Excluir \n 6. Menu Principal")
        option = int(input("\n Selecione uma opção: "))
        while option < 1 and option > 6:
            option = int(input("Não existe essa seção, digite um número de 1 a 6: "))
        
        if option == 1:
            print("Lista Completa") #listar todos
            for i in range(len(matrizprofdisc)):
                print(matrizprofdisc[i])
        
        elif option == 2:
            print("Pesquisa") #Pesquisa um elemento
            pesquisaprofdisc(matrizprofdisc)
        
        elif option == 3:
            print("INCLUIR") #Inclui um elemento
            matrizprofdisc = incluirprofdisc(matrizprofdisc, matrizprof, matrizdisc)
        
        elif option == 4:
            print("Alterar") #Altera um elemento
            alteraprofdisc(matrizprofdisc)
        
        elif option == 5:
            print("Excluir")
            matrizprofdisc = excluiprofdisc(matrizprofdisc)
    

def incluirprofdisc(matrizprofdisc, matrizprof, matrizdisc): #Incluir PROFESSOR-DISCIPLINA)
    profdisciplina=[]
    dadosprofdisciplina=["Registro Funcional Professor: ","Sigla Disciplina: ", "Ano: ", "Semestre: ", "Curso: ", 'Dias da semana: ',"Horários de início: "]

    #INSERE OS DADOS DO PROFESSOR-DISCIPLINA
    x = 0
    while x < 5:
            dado = input("Insira " + dadosprofdisciplina[x])
            
            if x == 0:
                while not verifica(matrizprof,dado):#se o dado não existir ele não consegue inserir
                    dado = input("Insira " + dadosprofdisciplina[x])
            
            if x == 1:
                while not verifica(matrizdisc,dado):
                    dado = input("Insira" + dadosprofdisciplina[x])

            profdisciplina.append(dado)
            x += 1

#######################################################################
####### INSERE OS DIAS DA SEMANA
    dado = 1
    dias = []
    while dado != '0': 
        dado = (input("Insira os dias da semana (um por vez e igual as opções) nos quais a disciplina será disponível \n  segunda   terca   quarta   quinta   sexta  \n Finalizando digite 0: "))
        if dado != '0':
            dias.append(dado)
    profdisciplina.append(dias)

    #######################################################################
####### INSERE OS HORARIOS
    dado = 1
    horario = []
    while dado != '0': 
        dado = input("Insira " + dadosprofdisciplina[6] + "\n Finalizando digite 0: ")
        if dado != '0':
            horario.append(dado)
    
    profdisciplina.append(horario)
    matrizprofdisc.append(profdisciplina)
    return matrizprofdisc

def excluiprofdisc(matrizprofdisc):
    registro = input("Digite o registro funcional para excluir o cadastro: ")
    sigla = input("Digite a sigla para excluir o cadastro: ")
    #percorre a matriz coluna 0 todas as linhas se achar um igual exclui esse indice
    i=0
    achou = False
    while achou == False and i < len(matrizprofdisc):
        if matrizprofdisc[i][0] == registro and matrizprofdisc[i][1] == sigla:
            del matrizprofdisc[i]
            achou = True
            print("Foi excluído com sucesso!")
        i += 1
    return matrizprofdisc

def pesquisaprofdisc(matrizprofdisc):
    registro = input("Digite o registro: ")
    sigla = input("Digite a sigla: ")
    i = 0
    achou = False
    while achou == False and i < len(matrizprofdisc):
        if matrizprofdisc[i][0] == registro and matrizprofdisc[i][1] == sigla:
            print(matrizprofdisc[i])
            achou = True
        i += 1

def alteraprofdisc(matrizprofdisc):
    registro = input("Digite o registro: ")
    sigla = input("Digite a sigla: ")
    coluna = int(input("Qual informação você gostaria de alterar? \n 0.Registro Funcional   1.Sigla   2.Ano   3.Semestre   4.Curso   5.Dias da semana   6.Horários de início \n"))
    i = 0
    achou = False
    while achou == False and i < len(matrizprofdisc):
        if matrizprofdisc[i][0] == registro and matrizprofdisc[i][1] == sigla:
            achou = True
            matrizprofdisc[i][coluna] = input("Digite o novo dado: ")
        i += 1

################################################################################################################
#                                             RELATÓRIOS
################################################################################################################
def relatorios(matrizprof,matrizdisc,matrizprofdisc):
    option = 1
    while option != 4:
        option = int(input("\n Relatórios \n Escolha o tipo de relatório: \n 1.Titulação   2.Créditos   3.Professor disciplina   4.Menu Principal: "))
        if option == 1:
            relatorio_titulo(matrizprof)

        elif option == 2:
            relatorio_credito(matrizdisc)
            
        elif option == 3:
            relatorio_profdisc(matrizprof,matrizdisc,matrizprofdisc)

###############################################################################################################
#                                           FUNÇÕES RELATORIO
################################################################################################################
def relatorio_titulo(matrizprof):
    titulo = ''
    option = int(input('\nEscolha qual título: \n 1.Mestrado   2.Doutorado: '))
    if option == 1:
        titulo = 'mestrado'
    else:
        titulo = 'doutorado'
    
    i = 0
    while i < len(matrizprof):
        if titulo == matrizprof[i][5]:
            print(matrizprof[i])
        i += 1

def relatorio_credito(matrizdisc):
    option = int(input('\n Imprimir disciplinas com mais de <numero de créditos>: '))
    i = 0
    while i < len(matrizdisc):
        if int(matrizdisc[i][4]) > option:
            print(matrizdisc[i])
        i += 1

def relatorio_profdisc(matrizprof,matrizdisc,matrizprofdisc):
    mat_linha_relatorio = []
    i = 0
    while i < len(matrizprofdisc):
        j = 0
        linha_relatorio = []
        while j < len(matrizprofdisc[i][5]):
            if matrizprofdisc[i][5][j] == 'terca' or matrizprofdisc[i][5][j] == 'quinta':

                # ADCIONAA A LINHA DA MATRIZ QUE CONTEM TERÇA OU QUINTA, já que ela possui todos elementos que precisamos
                linha_relatorio.append(matrizprofdisc[i])

                #PESQUISAR NOME DO PROFESSOR
                k =0
                encontrou = False
                while not encontrou:
                    if matrizprofdisc[i][0] == matrizprof[k][0]:
                        linha_relatorio.append(matrizprof[k][1])
                        encontrou = True
                    k+=1

                #PESQUISAR NOME DA DISCIPLINA
                l = 0
                encontrou =False
                while not encontrou:
                    if matrizprofdisc[i][1] == matrizdisc[l][0]:
                        linha_relatorio.append(matrizdisc[l][1])
                        encontrou = True
                    l +=1
                mat_linha_relatorio.append(linha_relatorio)

            j+=1
        i+=1
    print(mat_linha_relatorio)

################################################################################################################
#                                             VERIFICAÇÃO DE REPETIÇÃO
################################################################################################################

def verifica(matriz,dado):
    i = 0
    while i < len(matriz):
        j=0
        while j < len(matriz[i]):
            if matriz[i][j] == dado:
                print("Já existe esse cadastro!")
                return True
            j +=1
        i+=1
    return False # se ele vir nessa linha significa que ele n encontrou

#########################
# PROGRAMA PRINCIPAL
#########################
main()