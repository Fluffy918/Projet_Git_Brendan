# Fonction pour supprimer un todo
def supprimer_todo():
    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo à supprimer : ")) - 1
        if 0 <= index < len(todos):
            todo = todos.pop(index)
            print(f"Todo '{todo['titre']}' supprimé.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")
