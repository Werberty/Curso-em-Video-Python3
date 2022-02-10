import urllib
from urllib import request
try:
    page = request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessivel no momento!\033[m')
else:
    print('\033[32mConsegui acessar o site pudim com sucesso!\033[m')
    print(page.read())

