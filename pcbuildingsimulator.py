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
                                "AMD Radeon RX 5500XT",
                                "Asus Strix Radeon RX 5500XT",
                                "Gigabyte Radeon RX 5500XT",
                                "Aorus Radeon RX 5500XT",
                                "MSI Radeon RX 5500XT",
                                "Sapphire Radeon RX 5500XT",
                                "AMD Radeon RX 590",
                                "Asus Strix Radeon RX 590",
                                "Gigabyte Radeon RX 590",
                                "Aorus Radeon RX 590",
                                "MSI Radeon RX 590",
                                "Sapphire Radeon RX 590",
                                "XFX Radeon RX 590",
                                "AMD Radeon RX 580",
                                "Asus Strix Radeon RX 580",
                                "Gigabyte Radeon RX 580",
                                "Aorus Radeon RX 580",
                                "MSI Radeon RX 580",
                                "Sapphire Radeon RX 580",
                                "XFX Radeon RX 580",
                                "AMD Radeon RX 570",
                                "Asus Strix Radeon RX 570",
                                "Gigabyte Radeon RX 570",
                                "Aorus Radeon RX 570",
                                "MSI Radeon RX 570",
                                "Sapphire Radeon RX 570",
                                "XFX Radeon RX 570",
                                "AMD Radeon RX 560",
                                "Asus Strix Radeon RX 560",
                                "Gigabyte Radeon RX 560",
                                "Aorus Radeon RX 560",
                                "MSI Radeon RX 560",
                                "Sapphire Radeon RX 560",
                                "XFX Radeon RX 560",
                                "AMD Radeon RX 550",
                                "Asus Strix Radeon RX 550",
                                "Gigabyte Radeon RX 550",
                                "MSI Radeon RX 550",
                                "Sapphire Radeon RX 550",
                                "XFX Radeon RX 550",
                                "Retour"
                            ]
                        }
                        reponse = prompt(QUESTION11).get('command')

                    if reponse == "Nvidia":
                        QUESTION12 = {
                            "type": "list",  # Ne pas retirer
                            "name": "command",  # Ne pas retirer
                            "message": "Choisissez une action",  # Question

                                # Choix
                                "choices": [
                                    "Nvidia RTX 3090",
                                    "Aorus RTX 3090",
                                    "Msi RTX 3090",
                                    "Gigabyte RTX 3090",
                                    "Colorful RTX 3090",
                                    "EVGA RTX 3090",
                                    "Asus RTX 3090",
                                    "Asus Strix RTX 3090",
                                    "Zhingyou RTX 3090",
                                    "Nvidia RTX 3080",
                                    "Aorus RTX 3080",
                                    "Msi RTX 3080",
                                    "Gigabyte RTX 3080",
                                    "Colorful RTX 3080",
                                    "EVGA RTX 3080",
                                    "Asus RTX 3080",
                                    "Asus Strix RTX 3080",
                                    "Zhingyou RTX 3080",
                                    "Nvidia RTX 3070",
                                    "Aorus RTX 3070",
                                    "Msi RTX 3070",
                                    "Gigabyte RTX 3070",
                                    "Colorful RTX 3070",
                                    "EVGA RTX 3070",
                                    "Asus RTX 3070",
                                    "Asus Strix RTX 3070",
                                    "Zhingyou RTX 3070",
                                    "Nvidia RTX 3060",
                                    "Aorus RTX 3060",
                                    "Msi RTX 3060",
                                    "Gigabyte RTX 3060",
                                    "Colorful RTX 3060",
                                    "EVGA RTX 3060",
                                    "Asus RTX 3060",
                                    "Asus Strix RTX 3060",
                                    "Zhingyou RTX 3060",
                                    "Nvidia RTX 2080TI",
                                    "Aorus RTX 2080TI",
                                    "Msi RTX 2080TI",
                                    "Gigabyte RTX 2080TI",
                                    "Colorful RTX 2080TI",
                                    "EVGA RTX 2080TI",
                                    "Asus RTX 2080TI",
                                    "Asus Strix RTX 2080TI",
                                    "Zhingyou RTX 2080TI",
                                    "Nvidia RTX 2080",
                                    "Aorus RTX 2080",
                                    "Msi RTX 2080",
                                    "Gigabyte RTX 2080",
                                    "Colorful RTX 2080",
                                    "EVGA RTX 2080",
                                    "Asus RTX 2080",
                                    "Asus Strix RTX 2080",
                                    "Zhingyou RTX 2080",
                                    "Nvidia RTX 2070TI",
                                    "Aorus RTX 2070TI",
                                    "Msi RTX 2070TI",
                                    "Gigabyte RTX 2070TI",
                                    "Colorful RTX 2070TI",
                                    "EVGA RTX 2070TI",
                                    "Asus RTX 2070TI",
                                    "Asus Strix RTX 2070TI",
                                    "Zhingyou RTX 2070TI",
                                    "Nvidia RTX 2070",
                                    "Aorus RTX 2070",
                                    "Msi RTX 2070",
                                    "Gigabyte RTX 2070",
                                    "Colorful RTX 2070",
                                    "EVGA RTX 2070",
                                    "Asus RTX 2070",
                                    "Asus Strix RTX 2070",
                                    "Zhingyou RTX 2070",
                                    "Nvidia RTX 2060TI",
                                    "Aorus RTX 2060TI",
                                    "Msi RTX 2060TI",
                                    "Gigabyte RTX 2060TI",
                                    "Colorful RTX 2060TI",
                                    "EVGA RTX 2060TI",
                                    "Asus RTX 2060TI",
                                    "Asus Strix RTX 2060TI",
                                    "Zhingyou RTX 2060TI",
                                    "Nvidia RTX 2060",
                                    "Aorus RTX 2060",
                                    "Msi RTX 2060",
                                    "Gigabyte RTX 2060",
                                    "Colorful RTX 2060",
                                    "EVGA RTX 2060",
                                    "Asus RTX 2060",
                                    "Asus Strix RTX 2060",
                                    "Zhingyou RTX 2060",
                                    "Nvidia GTX 1080TI",
                                    "Aorus GTX 1080TI",
                                    "Msi GTX 1080TI",
                                    "Gigabyte GTX 1080TI",
                                    "Colorful GTX 1080TI",
                                    "EVGA GTX 1080TI",
                                    "Asus GTX 1080TI",
                                    "Asus Strix GTX 1080TI",
                                    "Zhingyou GTX 1080TI",
                                    "Nvidia GTX 1080",
                                    "Aorus GTX 1080",
                                    "Msi GTX 1080",
                                    "Gigabyte GTX 1080",
                                    "Colorful GTX 1080",
                                    "EVGA GTX 1080",
                                    "Asus GTX 1080",
                                    "Asus Strix GTX 1080",
                                    "Zhingyou GTX 1080",
                                    "Nvidia GTX 1070TI",
                                    "Aorus GTX 1070TI",
                                    "Msi GTX 1070TI",
                                    "Gigabyte GTX 1070TI",
                                    "Colorful GTX 1070TI",
                                    "EVGA GTX 1070TI",
                                    "Asus GTX 1070TI",
                                    "Asus Strix GTX 1070TI",
                                    "Zhingyou GTX 1070TI",
                                    "Nvidia GTX 1070",
                                    "Aorus GTX 1070",
                                    "Msi GTX 1070",
                                    "Gigabyte GTX 1070",
                                    "Colorful GTX 1070",
                                    "EVGA GTX 1070",
                                    "Asus GTX 1070",
                                    "Asus Strix GTX 1070",
                                    "Zhingyou GTX 1070",
                                    "Nvidia GTX 1060TI",
                                    "Aorus GTX 1060TI",
                                    "Msi GTX 1060TI",
                                    "Gigabyte GTX 1060TI",
                                    "Colorful GTX 1060TI",
                                    "EVGA GTX 1060TI",
                                    "Asus GTX 1060TI",
                                    "Asus Strix GTX 1060TI",
                                    "Zhingyou GTX 1060TI",
                                    "Nvidia GTX 1060",
                                    "Aorus GTX 1060",
                                    "Msi GTX 1060",
                                    "Gigabyte GTX 1060",
                                    "Colorful GTX 1060",
                                    "EVGA GTX 1060",
                                    "Asus GTX 1060",
                                    "Asus Strix GTX 1060",
                                    "Zhingyou GTX 1060",
                                    "Nvidia GTX 1050TI",
                                    "Aorus GTX 1050TI",
                                    "Msi GTX 1050TI",
                                    "Gigabyte GTX 1050TI",
                                    "Colorful GTX 1050TI",
                                    "EVGA GTX 1050TI",
                                    "Asus GTX 1050TI",
                                    "Asus Strix GTX 1050TI",
                                    "Zhingyou GTX 1050TI",
                                    "Nvidia GTX 1050",
                                    "Aorus GTX 1050",
                                    "Msi GTX 1050",
                                    "Gigabyte GTX 1050",
                                    "Colorful GTX 1050",
                                    "EVGA GTX 1050",
                                    "Asus GTX 1050",
                                    "Asus Strix GTX 1050",
                                    "Zhingyou GTX 1050",
                                    "Retour"
                                ]
                            }
                        reponse = prompt(QUESTION12).get('command')