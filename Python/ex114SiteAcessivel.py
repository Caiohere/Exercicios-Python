import urllib.request

try:
    site = urllib.request.urlopen(url='http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mSite não está acessível no momento\033[m')
else:
    print('\033[32mSite está acessível no momento\033[m')
