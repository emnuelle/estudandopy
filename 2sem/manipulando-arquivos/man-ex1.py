import re

try:
    f = open('D:/estudandopy/2sem/manipulando-arquivos/lero.txt','r', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Arquivo n encontrado")

# supostamente deveria printar o poema da baatinha :(
# funcionou no pycharm!!!!!!! (pasta no dados(D))