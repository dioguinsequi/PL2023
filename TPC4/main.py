import re
import json


def parser_file(nome_ficheiro):
    resultados = []
    expressoes = ""
    f = open(nome_ficheiro, 'r')
    primeiralinha = f.readline()
    linhas = f.readline()[1:]
    cabecalho = re.findall(r"(\w+(?:{\d+}(?:::(?:\w)+)*|{\d+,\d+}(?:::(?:\w)+)*)*)", primeiralinha)
    for l in cabecalho:
        n = re.search(r"{(\d+)}", l)
        grupo = re.match(r"(\w+)", l)
        if n:
            numero = re.search(r"(\d+)", l)
            for i in range(int(numero.group())):
                expressoes += f"(?P<{grupo}{i}>\d+),"
        else:
            n = re.search(r"({(\d+),(\d+)})", l)
            if n:
                numeros = re.findall(r"(\d+)", l)
                for i in range(numeros[0]):
                    expressoes += f"(?P<{grupo}{i}>\d+),"
                for i in range(numeros[0], numeros[1]):
                    expressoes += f"(?P<{grupo}{i}>\d*),"
            else:
                expressoes += f"(?P<{grupo}>\w+),"
    expressoes = expressoes[:-1]

    for line in linhas:
        match = re.match(expressoes, line)
        if match:
            dict = {}
            for i in range(len(cabecalho)):
                if "{" not in cabecalho[i]:
                    dict[cabecalho[i]] = match.group(cabecalho[i])
                else:
                    grupo = match.split("{")[0]
                    dictaux = match.groupdict()
                    listanumeros = [dictaux[grupo + "0"]]
                    j = 1
                    key = grupo + str(j)
                    while True:
                        if dictaux[key] == "":
                            break
                        listanumeros.append(dictaux[key])
                        j += 1
                        key = grupo + str(j)
                    funcao = cabecalho[i].split("::")[1]
                    if funcao == "":
                        dict[grupo] = listanumeros
                    elif funcao == "sum":
                        lista_valores = list(map(int, listanumeros))
                        dict[grupo] = str(sum(lista_valores))
                    elif funcao == "media":
                        lista_valores = list(map(int, listanumeros))
                        dict[grupo] = str(sum(lista_valores) / len(lista_valores))
                    elif funcao == "maior":
                        dict[grupo] = str(max(listanumeros, key=int))
                    elif funcao == "menor":
                        dict[grupo] = str(min(listanumeros, key=int))
                    resultados.append(dict)

    return resultados


def jsonfunc(resultados):
    with open("dados.json", "w") as f:
        for i in range(20):
            json.dump(resultados[i], f, indent=2)


def main():
    resultados = parser_file("myheart.csv")
    jsonfunc(resultados)


if __name__ == "__main__":
    main()
