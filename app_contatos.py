from mongoengine import Document, StringField, connect, ValidationError
import secrets

connect('contatos_db')

def gerar_id_curto():
    return secrets.token_hex(4)

class Contato(Document):
    nome = StringField(required=True, max_length=50)
    telefone = StringField(required=True, max_length=20)
    id_contato = StringField(primary_key=True, default=gerar_id_curto)

def criar_contato():
    print("\n====== Criar Contato ======")

    nome = input("Digite o nome do contato para ser adicionado: ").strip()
    telefone = input("Digite o telefone do contato: ").strip()

    if not nome or not telefone:
        print("Nome e telefone são obrigatórios! Por favor digite novamente.")
        return
    try:
        contato = Contato(nome=nome, telefone=telefone)
        contato.save()
        print("Contato salvo com sucesso!")
    except ValidationError as e:
        print("Erro ao salvar o contato:", e)

def listar_contatos():
    print("\n====== Lista de Contatos ======")

    contatos = Contato.objects()
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    for contato in contatos:
        print(f"ID: {contato.id} | Nome: {contato.nome} | Telefone: {contato.telefone}")

def atualizar_contato():
    print("\n====== Atualizar Contato ======")

    listar_contatos()
    contato_id = input("Digite o ID do contato a atualizar: ").strip()

    try:
        contato = Contato.objects.get(id=contato_id)
        novo_nome = input("Digite o novo nome (deixe vazio para manter): ").strip()
        novo_telefone = input("Digite o novo telefone (deixe vazio para manter): ").strip()
        if novo_nome:
            contato.nome = novo_nome
        if novo_telefone:
            contato.telefone = novo_telefone
        contato.save()

        print("Contato atualizado!")

    except Contato.DoesNotExist:
        print("Contato não encontrado!")

    except ValidationError as e:
        print("Erro ao atualizar o contato:", e)

def deletar_contato():
    print("\n====== Deletar Contato ======")

    listar_contatos()
    contato_id = input("Digite o ID do contato a deletar: ").strip()
    try:
        contato = Contato.objects.get(id=contato_id)
        contato.delete()
        print("Contato deletado!")
    except Contato.DoesNotExist:
        print("Contato não encontrado!")

def menu():
    while True:
        print("\n====== Menu de Contatos ======")

        print("1. Criar contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Deletar contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            criar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            atualizar_contato()
        elif opcao == "4":
            deletar_contato()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()