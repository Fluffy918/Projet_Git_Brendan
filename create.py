# Fonction pour créer un todo 
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append({'titre': titre, 'fait': False})
    print(f"Todo '{titre}' ajouté.")
