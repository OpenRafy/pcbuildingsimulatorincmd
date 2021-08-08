import colorama
from termcolor import colored

from PyInquirer import prompt

colorama.init()

is_running = True

colorama.init()
while is_running:

    print(colored("PC BUILDING SIMULATOR","blue"))

    print(colored("V0.1a","red"))

    QUESTION = {
        "type": "list",  # Ne pas retirer
        "name": "command",  # Ne pas retirer
        "message": "Choisissez un proposition",  # Question

        # Choix
        "choices": [
            "Jouer",
            "Credits",
            "Quitter"
        ]
    }

    reponse = prompt(QUESTION).get('command')

    if reponse == "Credits":
        print("Dev by OpenRafy, Special Thanks for Sigma ! 2021 OpenRafy")

    elif reponse == "Quitter":
        is_running = False

    elif reponse == "Jouer":
        QUESTION2 = {
            "type": "list",  # Ne pas retirer
            "name": "command",  # Ne pas retirer
            "message": "Choisissez un type de pc",  # Question

            # Choix
            "choices": [
                "Continuer",
                "Placard",
                "Revenir au menu"
            ]
        }