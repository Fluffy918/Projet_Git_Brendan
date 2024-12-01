# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if 0 <= index < len(todos):
            todos[index]['fait'] = not todos[index]['fait']
            print(f"Statut du todo '{todos[index]['titre']}' modifié.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")
