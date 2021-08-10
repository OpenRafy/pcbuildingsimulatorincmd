import colorama
from termcolor import colored

from PyInquirer import prompt

colorama.init()

firsttime = True

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
                "Commencer" if firsttime else "Continuer",
                "Placard",
                "Revenir au menu"
            ]
        }
        firsttime = False

        reponse = prompt(QUESTION2).get('command')

        if reponse == "Continuer":
            print("Pas Possible Pour Le Moment")

        elif reponse == "Commencer":
            QUESTION3 = {
                "type": "list",  # Ne pas retirer
                "name": "command",  # Ne pas retirer
                "message": "Choisissez une action",  # Question

                # Choix
                "choices": [
                    "Monter mon premier pc",
                    "Revenir au menu"
                ]
            }
            reponse = prompt(QUESTION3).get('command')

            if reponse == "Monter mon premier pc":
                QUESTION4 = {
                    "type": "list",  # Ne pas retirer
                    "name": "command",  # Ne pas retirer
                    "message": "Choisissez une action",  # Question

                    # Choix
                    "choices": [
                        "CPU",
                        "Carte Mere",
                        "RAM",
                        "GPU",
                        "PSU",
                        "Stockage",
                        "Refroidissement",
                        "Pate Thermique",
                        "Retour"
                    ]
                }
                reponse = prompt(QUESTION4).get('command')

                if reponse == "CPU":
                    QUESTION5 = {
                        "type": "list",  # Ne pas retirer
                        "name": "command",  # Ne pas retirer
                        "message": "Choisissez une action",  # Question

                        # Choix
                        "choices": [
                            "Intel",
                            "AMD",
                            "Retour"
                        ]
                    }
                    reponse = prompt(QUESTION5).get('command')

                    if reponse == "Intel":
                        QUESTION6 = {
                            "type": "list",  # Ne pas retirer
                            "name": "command",  # Ne pas retirer
                            "message": "Choisissez une action",  # Question

                            # Choix
                            "choices": [
                                "Intel i9 11900K",
                                "Intel i7 11800K",
                                "Intel i5 11600K",
                                "Intel i3 11300K",
                                "Intel i9 10900K",
                                "Intel i7 10800K",
                                "Intel i5 10600K",
                                "Intel i3 10300K",
                                "Intel i9 9900K",
                                "Intel i7 9800K",
                                "Intel i5 9600K",
                                "Intel i3 9300K",
                                "Intel i7 8800K",
                                "Intel i5 8600K",
                                "Intel i3 8300K",
                                "Intel i7 7800K",
                                "Intel i5 7600K",
                                "Intel i3 7300K",
                                "Retour"
                            ]
                        }
                        reponse = prompt(QUESTION6).get('command')

                    if reponse == "AMD":
                        QUESTION7 = {
                            "type": "list",  # Ne pas retirer
                            "name": "command",  # Ne pas retirer
                            "message": "Choisissez une action",  # Question

                                # Choix
                                "choices": [
                                    "AMD Ryzen 9 5950X",
                                    "AMD Ryzen 9 5900X",
                                    "AMD Ryzen 7 5800X",
                                    "AMD Ryzen 5 5500X",
                                    "AMD Ryzen 3 5300X",
                                    "AMD Ryzen 5 4500G",
                                    "AMD Ryzen 3 4300G",
                                    "AMD Ryzen 9 3900X",
                                    "AMD Ryzen 7 3700X",
                                    "AMD Ryzen 5 3600X",
                                    "AMD Ryzen 5 3600",
                                    "AMD Ryzen 3 3300X",
                                    "AMD Ryzen 3 3200G",
                                    "AMD Ryzen 7 2700X",
                                    "AMD Ryzen 5 2600X",
                                    "AMD Ryzen 5 2600",
                                    "AMD Ryzen 3 2200",
                                    "AMD Ryzen 3 2200G",
                                    "AMD FX 8350",
                                    "Retour"
                                ]
                            }
                        reponse = prompt(QUESTION7).get('command')

                if reponse == "Carte Mere":

                    QUESTION8 = {
                            "type": "list",  # Ne pas retirer
                            "name": "command",  # Ne pas retirer
                            "message": "Choisissez une action",  # Question

                                # Choix
                                "choices": [
                                    "ASUS",
                                    "ASROCK",
                                    "Biostar,"
                                    "Colorful",
                                    "EVGA",
                                    "Gigabyte",
                                    "Intel Desktop Board",
                                    "MSI",
                                    "NZXT",
                                    "Sapphire",
                                    "XFX",
                                    "Retour"
                                ]
                            }
                    reponse = prompt(QUESTION8).get('command')

                if reponse == "RAM":
                    QUESTION9 = {
                        "type": "list",  # Ne pas retirer
                        "name": "command",  # Ne pas retirer
                        "message": "Choisissez une action",  # Question

                        # Choix
                        "choices": [
                            "Aorus",
                            "Balistix",
                            "Corsair",
                            "Crucial",
                            "Gigabyte",
                            "GSkill",
                            "HyperX",
                            "Viper",
                            "Retour"
                        ]
                    }
                    reponse = prompt(QUESTION9).get('command')
                if reponse == "GPU":
                    QUESTION10 = {
                        "type": "list",  # Ne pas retirer
                        "name": "command",  # Ne pas retirer
                        "message": "Choisissez une action",  # Question

                        # Choix
                        "choices": [
                            "AMD",
                            "Nvidia",
                            "Retour"
                        ]
                    }
                    reponse = prompt(QUESTION10).get('command')
                    if reponse == "AMD":
                        QUESTION11 = {
                            "type": "list",  # Ne pas retirer
                            "name": "command",  # Ne pas retirer
                            "message": "Choisissez une action",  # Question

                            # Choix
                            "choices": [
                                "AMD Radeon RX 6900XT",
                                "Asus Strix Radeon RX 6900XT",
                                "Gigabyte Radeon RX 6900XT",
                                "Aorus Radeon RX 6900XT",
                                "MSI Radeon RX 6900XT",
                                "Sapphire Radeon RX 6900XT",
                                "XFX Radeon RX 6900XT",
                                "AMD Radeon RX 6800XT",
                                "Asus Strix Radeon RX 6800XT",
                                "Gigabyte Radeon RX 6800XT",
                                "Aorus Radeon RX 6800XT",
                                "MSI Radeon RX 6800XT",
                                "Sapphire Radeon RX 6800XT",
                                "XFX Radeon RX 6800XT",
                                "AMD Radeon RX 6700XT",
                                "Asus Strix Radeon RX 6700XT",
                                "Gigabyte Radeon RX 6700XT",
                                "Aorus Radeon RX 6700XT",
                                "MSI Radeon RX 6700XT",
                                "Sapphire Radeon RX 6700XT",
                                "XFX Radeon RX 6700XT",
                                "AMD Radeon RX 5700XT",
                                "Asus Strix Radeon RX 5700XT",
                                "Gigabyte Radeon RX 5700XT",
                                "Aorus Radeon RX 5700XT",
                                "MSI Radeon RX 5700XT",
                                "Sapphire Radeon RX 5700XT",
                                "XFX Radeon RX 5700XT",
                                "AMD Radeon RX 5600XT",
                                "Asus Strix Radeon RX 5600XT",
                                "Gigabyte Radeon RX 5600XT",
                                "Aorus Radeon RX 5600XT",
                                "MSI Radeon RX 5600XT",
                                "Sapphire Radeon RX 5600XT",
                                "XFX Radeon RX 5600XT",
                                "Retour"
                            ]
                        }
                        reponse = prompt(QUESTION11).get('command')