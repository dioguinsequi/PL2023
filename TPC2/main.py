import sys

def soma(line):
  soma =0
  posicao = 0
  ligado = 1
  while posicao<len(line):
    if 48<ord(line[posicao])<59 and ligado ==1:
      soma+= int(line[posicao])
    elif line[posicao] == "=":
      print(soma)
    elif (line[posicao] == "o" or line[posicao] == "O") and (line[posicao+1] == "n" or line[posicao+1] == "N"):
      ligado = 1
    elif (line[posicao] == "o" or line[posicao] == "O") and (line[posicao+1] == "f" or line[posicao+1] == "F") and (line[posicao+2] == "f" or line[posicao+2] == "F"):
      ligado = 0
    posicao +=1
  return soma





def main():
  for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    a = soma(line)
    print(a)
    

    


if __name__ == '__main__':
    main()

     