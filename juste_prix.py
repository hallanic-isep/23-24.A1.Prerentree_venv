# Tirage d'un prix (entier) au hasard entre 1 et 10
import random

cible = random.randint(1,10)

# 5 essais...
for i in range(5):

    # Essai d'un prix
    try:
        essai = int(input(f"essai {i+1} : "))
    except:
        print("Valeur incorrecte...")
        essai = 0 # pour éviter l'erreur si aucune saisie est valide...
        continue

    # Message "BRAVO" si le prix est trouvé
    if (cible == essai):
        print("BRAVO !!!")

        # Fin au bout de 5 esssais ou si le prix est trouvé
        break

    # Message "PAS ASSEZ" si le prix est trop bas
    elif (cible > essai):
        print("PAS ASSEZ...")
    # Message "TROP ELEVE" si le prix est trop haut
    else:
        print("TROP ELEVE...")

# Message "PERDU" au bout de 5 essais
if (cible != essai):
    print("PERDU...")

print("FIN...")