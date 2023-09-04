import re

try:
    f = open('D:/estudandopy/2sem/manipulando-arquivos/lero.txt','r', encoding='utf-8')
    # 96 seria quantidade de caracteres, no caso se fosse 10 iria apenas os 10 
    # f.readline() - le cada linha, da pra colocar varios em print (em casos de duvida ver no versionameto) - inclusive da prsa fazer com a in range - ver2
    for i in range(0,3,1):
        print(f.readline())
    f.close()
except FileNotFoundError:
    print("Arquivo n encontrado")

# supostamente deveria printar o poema da baatinha :(
# funcionou no pycharm!!!!!!! (pasta no dados(D))