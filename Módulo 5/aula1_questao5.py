import emoji

print("Veja a lista de emojis a seguir!")
print(emoji.emojize ('red_heart: :red_heart:'))
print(emoji.emojize ('thumbs_up: :thumbs_up:'))
print(emoji.emojize ('thinking_face: :thinking_face:'))
print(emoji.emojize ('partying_face: :partying_face:'))

n=str(input("Digite uma frase: "))
y= int (input("Escolha agora um código do emoji, sendo 1 (red_heart) 2(thumbs_up) 3 (thinking_face) 4 (partying_face) "))
if y==1:
   print (emoji.emojize  ( f'{n}:red_heart:'))
if y==2:
   print (emoji.emojize  ( f'{n}:thumbs_up:'))
if y==3:
   print (emoji.emojize  ( f'{n}:thinking_face:')) 
if y==4:
   print (emoji.emojize  ( f'{n}:partying_face:'))        

