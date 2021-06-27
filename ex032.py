from datetime import date

ano = int(input('Digite uma ano para ver se ele é Bissexto, ou 0 para ano atual: '))
# Caso o usuario tecle 0
if ano == 0:
    ano = date.today().year # pega o ano atual do sistema operacional

# Caso o usuario digite o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é Bissexto.'.format(ano))
else:
    print('Ano {} não é Bissexto.'.format(ano))