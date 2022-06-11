import os
import time

os.system("cls")

print('Bem vindo ao jogo da forca *\(^o^)/* \n ') 
nomedoJogador = input("\nJogador diga seu nome:\n")
nomedoDesafiante = input("\nDesafiante diga seu nome:\n")
print("\nBem vindo ao jogo da forca!",nomedoJogador,"Você será desafiado pela(o):",nomedoDesafiante)
os.system("cls")
print(nomedoDesafiante,"Siga as instruções ")
pSecreta = (input("Escolha a palavra secreta: "))
print(nomedoDesafiante,"\nAgora defina as dicas!\n")
dica1 = input("\nDigite a DICA 1: ")
dica2 = input("\nDigite a DICA 2: ")
dica3 = input("\nDigite a DICA 3: ")
tentativas = []
chances = 6
os.system("cls")


while True:
    escolher_dica = input ('''
    (1) Para a dica 1.
    (2) Para a dica 2.
    (3) Para a dica 3.
    (4) Não quer uma dica.
    Selecione uma opção: ''' )
    if escolher_dica == "1":
            print('\nDica 1: ',dica1)
            time.sleep(3)
            os.system("cls")
    elif escolher_dica == '2':
            print('\nDica 2: ',dica2)
            time.sleep(3)
            os.system("cls")
    elif escolher_dica == '3':
            print('\nDica 3: ',dica3)
            time.sleep(3)
            os.system("cls")
    elif escolher_dica == '4':
            os.system("cls")
    else:
            print("Opção inválida!\n")
            time.sleep(3)
            os.system("cls")

    letras = str(input("Jogador digite uma letra: "))
    os.system("cls")


    if len(letras)>1:
        print("Só é possivel digitar uma letra. \n ")
        continue

    if letras in tentativas:
        print("Você já digitou essa letra. \n ")
        continue
    
    tentativas.append(letras)

    verificacao = ''
    for letra_secreta in pSecreta:
        if letra_secreta in tentativas:
            verificacao += letra_secreta
        else:
            verificacao += '*'

    if verificacao == pSecreta:
         arquivo = open('arq01.txt','w')
         arquivo = arquivo.write(nomedoJogador + "\nganhou o jogo\n" +"\ndesafiado pelo (a)\n"+nomedoDesafiante )
         print(f'A palavra secreta era: {verificacao}')
         print("Você venceu! \(^-^)/ ")
         print("     ___________      ")
         print("    '._==_==_=_.'     ")
         print("    .-\:      /-.     ")
         print("   | (|:.     |) |    ")
         print("    '-|:.     |-'     ")
         print("      \::.    /       ")
         print("       '::. .'        ")
         print("         ) (          ")
         print("       _.' '._        ")
         print('       """""""        ')
         break
            
    else:
            print(f'Palavra secreta = {verificacao} \n ')
        
    if letras not in pSecreta:
            chances -= 1
            print(f'A palavra secreta não contém "{letras}" -1 chance')
    
    if chances == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        
    
    if chances == 5:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_      ")
        print()
        
    
    if chances == 4:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|    | ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
       
    
    if chances == 3:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /| ")
        print("|    | ")
        print("|      ")
        print("_      ")
        print()
       
    
    if chances == 2:
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|       ")
        print("_       ")
        print()
        
    
    if chances == 1:
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|   /   ")
        print("_       ")
        print()
        

    if chances == 0:
        arquivo = open('arq01.txt','w')
        arquivo = arquivo.write(nomedoJogador + "\nperdeu o jogo\n"+"\nfoi desafiado pelo(a)\n"+ nomedoDesafiante)
        print("Você foi enforcado ¯\_('-')_/¯ ")
        print()
        print("|-----  ")
        print("|    |  ")
        print("|    O  ")
        print("|   /|\ ")
        print("|    |  ")
        print("|   / \ ")
        print("_       ")
        print()
        print("Mais sorte da próxima vez :)")
        break
        
    
    print(f'Você tem {chances} chances \n ')

    
    
