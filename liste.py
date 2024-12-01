# Liste pour stocker les todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    print("\n==== Liste des todos ====")
    if not todos:
        print("Aucun todo pour le moment.")
    else:
        for i, todo in enumerate(todos, start=1):
            statut = "O" if todo['fait'] else "X"
            print(f"{i}. {todo['titre']} - {statut}")
    print("=========================")
