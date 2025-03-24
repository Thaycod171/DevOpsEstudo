import random

def gerar_numero_aleatorio(inicio, fim):
    """Função para gerar um número aleatório entre um intervalo"""
    return random.randint(inicio, fim)

def main():
    print("Bem-vindo ao gerador de números aleatórios!")
    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input("Digite o valor final do intervalo: "))
    
    numero_aleatorio = gerar_numero_aleatorio(inicio, fim)
    print(f"O número aleatório gerado entre {inicio} e {fim} é: {numero_aleatorio}")

if __name__ == "__main__":
    main()
