def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()
    
    # TODO: Se a string ficou vazia após o strip, retorne a string vazia
    # Dica: verifique se o texto ficou vazio após retirar espaços
    if texto == "":
        return ""

    # Separe em palavras (isso já remove múltiplos espaços) e reuna com um espaço
    palavras = texto.split()

    mensagem_formatada = " ".join(palavras).lower()

    return mensagem_formatada

# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)