#Jogo da Forca desenvolvido por Rafael Greca Vieira, estudante de Ciência da computação da UNIFEI
#Caso for utilizar o código, por favor deixar os créditos
#Sugestões e críticas são sempre bem vindas
#Meu github: https://github.com/rafaelgreca
#O dicionário de palavras utilizado no programa é encontrado em: https://github.com/thoughtworks/dadoware
#e foi modificado (retirado os acentos e caracteres especiais, assim como algumas palavras desnecessárias)

from os import system, name
from time import sleep
from unicodedata import normalize
import random

#Introdução do programa
def intro():

    for i in range (15,0,-1):
        print(" => Bem-vindo ao Jogo da Forca criado por Rafael Greca, estudante de Ciência da Computação na UNIFEI")
        print("O código está livre para quem quiser utilizar, porém seja legal e coloqueo os créditos.")
        print("Sugestões e críticas são sempre bem-vindas.")
        print("\n => Github: https://github.com/rafaelgreca")
        print(" => As palavras utilizadas nesse código foram retiradas desse repositório:\n https://github.com/thoughtworks/dadoware")
        print("\n Bom jogo =) \n")

        print("O JOGO IRÁ SE INICIAR EM  %d SEGUNDOS!" %i)
        sleep(1)
        limparATela()

    palavra = sortearPalavras()
    letras = []
    letrascertas = []
    letraserradas = []
    tentativas = 0
    desenho1(palavra,letras,letrascertas,letraserradas,tentativas)

#Abre o arquivo que contém as palavras
def sortearPalavras():

    listapalavras = open("palavras.txt", "r")
    palavras = []

    for i in listapalavras:
        #rstrip tira o '\n' do final das palavras
        palavra = tiraAcentoPalavras(i.rstrip('\n'))
        palavras.append(palavra)
    
    listapalavras.close()
    return selecionaPalavra(palavras)

#Seleciona uma palavra aleatória da lista de palavras
def selecionaPalavra(palavras):

    return random.choice(palavras)

#Tira os acentos e caracteres especiais das palavras do dicionário
def tiraAcentoPalavras(palavra):

    palavra  = palavra.lower()
    palavraSemAcento = normalize('NFKD', palavra).encode('ASCII','ignore').decode('ASCII')

    return palavraSemAcento

def limparATela(): 
  
    # para windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # para mac ou linux 
    else: 
        _ = system('clear') 

def desenho1(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")

    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))

        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)
        
def desenho2(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")
    
    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))
        
        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)
        
def desenho3(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t          |       |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")
    
    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))
        
        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)
        
def desenho4(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t         /|       |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")

    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))
        
        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)
        
def desenho5(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t         /|\      |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")

    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))
        
        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)

def desenho6(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t         /|\      |")
    print("\t\t         /        |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t            _____/|\_____")
    
    if checaVitoria(palavra,letras):
        print("\n\nParabéns! Você acertou!")
        print("A palavra era: %s" %palavra)
        sleep(5)
        limparATela()
    else:
        print("\nA palavra é: %s e possui %d letras" %(mostraLetrasJaDescobertas(palavra,letras),len(palavra)))
        print("\nLetras certas: ")
        print(" ".join(letrascertas))
        print("Letras erradas: ")
        print(" ".join(letraserradas))
        
        while True:
            letra = input("\nDigite uma letra: ")
            
            if checaLetra(letra,letras)==False:
                break
        letras.append(letra.lower())
        checaLetraNaPalavra(palavra,letras,letra.lower(),letrascertas,letraserradas,tentativas)

def desenho7(palavra,letras,letrascertas,letraserradas,tentativas):

    limparATela()
    print("\t\t          _________")
    print("\t\t          |      \|")
    print("\t\t          |       |")
    print("\t\t          O       |")
    print("\t\t         /|\      |")
    print("\t\t         / \      |")
    print("\t\t                  |")
    print("\t\t                  |")
    print("\t\t           _____/|\_____")
    print("\n\nVocê perdeu! A palavra era %s" %palavra)
    print("\nLetras certas: ")
    print(" ".join(letrascertas))
    print("Letras erradas: ")
    print(" ".join(letraserradas))
    sleep(5)
    limparATela()

#Checa se a letra já foi digitada
def checaLetra(letra,letras):

    if letra in letras:
        return True
    else:
        return False

def mostraLetrasJaDescobertas(palavra,letras):

    p = ''

    for i in palavra:
        if i in letras:
            p += i
        else:
            p += '_'
    
    return p

#Checa se o jogador descobriu a palavra
def checaVitoria(palavra,letras):
    
    vitoria = True

    for i in palavra:
        if i not in letras:
            vitoria = False
    
    return vitoria

def checaLetraNaPalavra(palavra,letras,letra,letrascertas,letraserradas,tentativas):
    
    contem = False

    for i in palavra:
        if i == letra:
            contem = True

    if contem:
        letrascertas.append(letra)
    else:
        letraserradas.append(letra)
        tentativas += 1
    
    if tentativas == 0:
        desenho1(palavra,letras,letrascertas,letraserradas,tentativas)
    elif tentativas == 1:
        desenho2(palavra,letras,letrascertas,letraserradas,tentativas)
    elif tentativas == 2:
        desenho3(palavra,letras,letrascertas,letraserradas,tentativas)
    elif tentativas == 3:
        desenho4(palavra,letras,letrascertas,letraserradas,tentativas)
    elif tentativas == 4:
        desenho5(palavra,letras,letrascertas,letraserradas,tentativas)
    elif tentativas == 5:
        desenho6(palavra,letras,letrascertas,letraserradas,tentativas)
    else:
        desenho7(palavra,letras,letrascertas,letraserradas,tentativas)

if __name__ == '__main__':
    
    while True:
        limparATela()
        intro()

        jogar = input("Deseja jogar de novo (S=SIM/N=NAO)? ")

        if jogar=='N' or jogar=='n':
            break