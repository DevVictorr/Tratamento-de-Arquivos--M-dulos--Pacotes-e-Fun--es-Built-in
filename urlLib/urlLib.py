import urllib.request


resposta = urllib.request.urlopen('https://github.com/DevVictorr')

html = resposta.read()

print(html)