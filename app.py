# Versão 1.3 (em desenvolvimento)
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)."

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Iniciar")
    print("2. Sair")
    print("------------")

autor = "Seu Nome"
print(f"Software de Exemplo | Autor: {autor}")
print(saudacao("Usuário"))
mostrar_menu()