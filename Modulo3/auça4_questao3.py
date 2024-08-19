#entrada
#Descobrir se o ano é bissexto

ano=int (input ("Insira um ano com 4 dígitos: "))

#processamento
#Bissexto: se o ano for divisível por 4 e não divisível por 100 ou se o ano for divisível por 400

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0 :
    print("É Bissexto")
else:
    print ("Não é bissexto")    