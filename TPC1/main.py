from ficheiro import Ficheiro

def main():
    dados = Ficheiro.parser()
    choice = -1
    while(choice != "0"):
        print("------------------MENU----------------")
        print("1-Distribuição da doença por genero")
        print("2-Distribuição da doença por escalão")
        print("3-Distribuição da doença por colestrol")
        print("0-Sair")
        choice = input("Escolha uma opção: ")
        if(choice == "1"):
            Ficheiro.distrSexo(dados)
        elif(choice == "2"):
            Ficheiro.distrIdade(dados)
        elif(choice == "2"):
            Ficheiro.distrColestrol(dados)
        else:
            print("Escolha uma opção válida")



if __name__ == '__main__':
    main()