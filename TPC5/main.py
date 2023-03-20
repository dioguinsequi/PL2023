import re

#MOEDA 1c, 2e, 3e, 5c, 20c, 30e,

def saldolista(lista):
    saldo = 0
    for elem in lista:
        if len(elem) == 2:
            if "c" in elem:
                saldo += int(elem[:1]) * 0.01
            if "e" in elem:
                saldo += int(elem[:1])
        elif len(elem) == 3:
            saldo += int(elem[:2]) * 0.01
    return saldo




def levantar():
    saldo = 0
    moedasex=["1c","2c","5c","10c","20c","50c","1e","2e"]
    padraozero = r"T=00"
    padraobloq = re.compile("^(T=601|T=604)")
    padraodois = r"T=2"
    padraooito = r"T=800"
    padraooitoz = r"T=808"
    listafiltrada = []
    listafalsa=[]
    print("maq:Introduzir moedas:")
    padraomoeda = r"MOEDA"
    padraotelefone = r"T"
    while True:
        entrada = input()
        if entrada == "POUSAR":
            print("maq:troco="+str(saldo)+"€; Volte sempre!")
            break
        correspondenciamoeda = re.match(padraomoeda, entrada)
        correspondenciatelefone = re.match(padraotelefone, entrada)
        if correspondenciamoeda:
            lista = re.findall(r"\d+[ce]", entrada)
            print(lista)
            for elemento in lista:
                if elemento in moedasex:
                    listafiltrada.append(elemento)
                else:
                    listafalsa.append(elemento)
            saldo = saldolista(listafiltrada)
            if len(listafalsa) >= 1:
                print("maq:",end="")
                print(listafalsa,end="")
                print("moedas invalidas; saldo ="+str(saldo)+"€")
            else:
                print("maq:saldo ="+str(saldo)+"€")
        elif correspondenciatelefone:
            tipobloq= re.match(padraobloq,entrada)
            tipozero = re.match(padraozero,entrada)
            tipodois = re.match(padraodois,entrada)
            tipooito= re.match(padraooito,entrada)
            tipooitoz =re.match(padraooitoz,entrada)
            if tipozero:
                if saldo <= 1.5:
                    print("maq:Saldo insuficiente!")
                else:
                    saldo -= 1.5
                    print("saldo ="+str(saldo)+"€")
            elif tipobloq and len(entrada)==11:
                print("maq:Esse número não é permitido neste telefone. Queira discar novo número!")
            elif tipodois and len(entrada)==11:
                if saldo <= 0.25:
                    print("maq:Saldo insuficiente!")
                else:
                    saldo -= 0.25
                    print("saldo =" + str(saldo) + "€")
            elif tipooito and len(entrada)==11:
                print("saldo =" + str(saldo) + "€")
            elif tipooitoz and len(entrada)==11:
                if saldo <= 0.10:
                    print("maq:Saldo insuficiente!")
                else:
                    saldo -= 0.10
                    print("saldo =" + str(saldo) + "€")
            else:
                print("maq:Numero invalido.Queira discar novo número!")
        elif entrada == "ABORTAR":
            saldo = 0
            print("maq: as suas moedas foram retiradas com sucesso!")
        else:
            print("ERROR404")



def main():
    ativo = 0
    while True:
        entrada = input()
        if entrada == "LEVANTAR":
            if ativo == 1:
                print("maq:Ja esta levantado")
            ativo =1
            print("boi")
            levantar()
            break
        elif entrada == "POUSAR":
            if ativo == 0:
                print("maq:ja esta pousado")
            ativo = 0
            break


if __name__ == "__main__":
    main()
