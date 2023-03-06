import re
import json


def parser_file(nome_ficheiro):
    resultados = []
    exp = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<resto>.*)::"
    rexp = re.compile(exp)
    f = open(nome_ficheiro, 'r')
    for line in f:
        match = rexp.finditer(line)
        for m in match:
            if match:
                resultados = resultados + [m.groupdict()]

    return resultados




def primeironome(nome):
    nomes = nome.split()
    return nomes[0]


def ultimonome(nome):
    nomes = nome.split()
    return nomes[-1]


def freq_processos_ano(resultados):
    dict_por_ano = {}

    for dict in resultados:
        if dict["ano"] not in dict_por_ano:
            dict_por_ano[dict["ano"]] = 0

        dict_por_ano[dict["ano"]] += 1

    print("\n")
    print(dict_por_ano)


def top5_nomes_seculo(resultados, seculo):
    dict_top5_nomes = {}
    for dict in resultados:
        if (int(dict["ano"]) // 100) + 1 == seculo:
            nome = primeironome(dict["nome"])
            if nome in dict_top5_nomes:
                dict_top5_nomes[nome] += 1
            else:
                dict_top5_nomes[nome] = 1
            nome = primeironome(dict["nome_pai"])
            if nome in dict_top5_nomes:
                dict_top5_nomes[nome] += 1
            else:
                dict_top5_nomes[nome] = 1
            nome = primeironome(dict["nome_mae"])
            if nome in dict_top5_nomes:
                dict_top5_nomes[nome] += 1
            else:
                dict_top5_nomes[nome] = 1
    return sorted(dict_top5_nomes.items(), key=lambda x: x[1], reverse=True)[:5]


def top5_apelidos_seculo(resultados, seculo):
    dict_top5_apelidos = {}
    for dict in resultados:
        if (int(dict["ano"]) // 100) + 1 == seculo:
            apelido = ultimonome(dict["nome"])
            if apelido in dict_top5_apelidos:
                dict_top5_apelidos[apelido] += 1
            else:
                dict_top5_apelidos[apelido] = 1
            apelido = ultimonome(dict["nome_pai"])
            if apelido in dict_top5_apelidos:
                dict_top5_apelidos[apelido] += 1
            else:
                dict_top5_apelidos[apelido] = 1
            apelido = ultimonome(dict["nome_mae"])
            if apelido in dict_top5_apelidos:
                dict_top5_apelidos[apelido] += 1
            else:
                dict_top5_apelidos[apelido] = 1
    return sorted(dict_top5_apelidos.items(), key=lambda x: x[1], reverse=True)[:5]


def seculo_para_intervalo(seculo):
    primeiro_ano = (seculo - 1) * 100 + 1
    ultimo_ano = primeiro_ano + 99

    return (primeiro_ano, ultimo_ano)


def top5_nomes(resultados):
    nome = {}
    apelido = {}

    for i in range(1, 22):
        nome[i] = top5_nomes_seculo(resultados, i)
        apelido[i] = top5_apelidos_seculo(resultados, i)

    print("\n")
    print(nome)
    print("\n")
    print(apelido)


def encontra_fam(linha):
    regex = r"(?:,(([A-Z][a-z]+ )*([A-Z][a-z]+))\. Proc.\d+)"
    return re.findall(regex, linha)


def freq_familia(resultados):
    familia = {}
    for dict in resultados:
        lista = encontra_fam(dict["resto"])
        for grau in lista:
            if grau in familia:
                familia[grau] += 1
            else:
                familia[grau] = 1
    print("\n\n")
    print(familia)


def jsonfunc(resultados):
    with open("dados.json", "w") as f:
        for i in range(20):
            json.dump(resultados[i], f, indent=2)


def main():
    resultados = parser_file("processos.txt")
    freq_processos_ano(resultados)
    top5_nomes(resultados)
    freq_familia(resultados)
    jsonfunc(resultados)

if __name__ == "__main__":
    main()
