def contar_palavras(texto):
    """Função para contar o número de palavras em um texto"""
    palavras = texto.split()
    return len(palavras)

def main():
    print("Bem-vindo ao contador de palavras!")
    texto = input("Digite um texto para contar as palavras: ")
    
    numero_palavras = contar_palavras(texto)
    print(f"O número de palavras no seu texto é: {numero_palavras}")

if __name__ == "__main__":
    main()

