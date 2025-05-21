def autenticar_usuario():
    senha_correta = "senha123"
    palavra_chave_correta = "codigo456"
    
    print("Sistema de Autenticação de Dois Fatores")
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta! Acesso negado.")
        return
    palavra_chave = input("Digite a palavra-chave: ")
    if palavra_chave != palavra_chave_correta:
        print("Palavra-chave incorreta! Acesso negado.")
        return
    print("Autenticação bem-sucedida! Acesso permitido.")

autenticar_usuario()