import csv
class Ficheiro:

    def distrSexo(dados1):

        doente,homem,mulher = 0,0,0

        for item in dados1:
            sexo = item.get('sexo')
            doente = item.get('doente')
            if (sexo == "M") and (doente == 1):
                homem += 1
                doente += 1
            elif (sexo == "F") and (doente == 1):
                mulher += 1
                doente += 1

        doenteM = (homem/doente)*100
        doenteF = (mulher/doente)*100
        print("-------------------------------------------------------------------")
        print("|                Distribuiçao da doença por genero                |")
        print("|Homem doentes -> "+ str(doenteM)+"%                              |")
        print("|Mulher doentes -> "+ str(doenteF)+"%                             |")
        print("-------------------------------------------------------------------")

    def distrIdade(dados):
        idades = {}
        for item in dados:
            idade = item.get('idade')
            doente = item.get('doente')
            etaria = idade/5
            if (doente == 1):
                idades[etaria] += 1
                doente += 1
           
        lista = idades.keys().sort()
        
        print("-------------------------------------------------------------------")
        print("|                Distribuiçao da doença por idades                |")

        for n in lista:
            print("|["+n*5+"-"+n*5+4+"] -> "+(idades.get(n)/doente)*100+"|")
        print("-------------------------------------------------------------------")

    def distrColestrol(dados):
        colestrols = {}
        for item in dados:
            col = item.get('colestrol')
            doente = item.get('doente')
            etario = col/10
            if (doente == 1):
                colestrols[etario] += 1
                doente += 1
            
        listac = colestrols.keys().sort()
        
        print("-------------------------------------------------------------------")
        print("|                Distribuiçao da doença por idades                |")

        for n in listac:
            print("|["+n*10+"-"+n*10+9+"] -> "+(colestrols.get(n)/doente)*100+"|")
        print("-------------------------------------------------------------------")   


    def parser():
        dados = []
        path="myheart.csv"
        file = open(path,"r")
        inform = file.read().split('\n') 

        next(inform)

        for linha in inform:
            if int(linha[0]) > 0 and int(linha[3]) > 0 and (linha[1] == 'M' or linha[1] == 'F') and (int(linha[5]) == 0 or int(linha[5]) == 1):
                    idade = int(linha[0])
                    sexo = linha[1]
                    colestrol = int(linha[3])
                    doente = int(linha[5])

                    dict = {"idade": idade,"sexo": sexo,"colestrol": colestrol,"doente": doente}
                    dados.append(dict)

        return dados

    