from colorama import Fore, Style, init
import time
import os
import subprocess
import requests

init()

# MIT License
#
# Copyright (c) [2023] [Luden]
#
# Permiso concedido de forma gratuita a cualquier persona que obtenga una copia
# de este software y archivos de documentación asociados (el "Software"), para tratar
# con el Software sin restricciones, incluyendo sin limitación los derechos
# de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
# copias del Software, y para permitir a las personas a las que se les proporcione el Software
# hacerlo, sujeto a las siguientes condiciones:
#
# El aviso de copyright anterior y este aviso de permiso se incluirán en todos los
# copias o partes sustanciales del Software.
#
# EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
# IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
# IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO EL
# AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE CUALQUIER RECLAMO,
# DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O
# DE OTRO MODO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O
# EL USO O OTRAS NEGOCIACIONES EN EL SOFTWARE.

# Files .jar

url = "https://github.com"

# Paper
paper1201 = "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/45/downloads/paper-1.20.1-45.jar"
paper120 = "https://api.papermc.io/v2/projects/paper/versions/1.20/builds/17/downloads/paper-1.20-17.jar"
paper1194 = "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar"
paper1193 = "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar"
paper1192 = "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar"
paper1191 = "https://api.papermc.io/v2/projects/paper/versions/1.19.1/builds/111/downloads/paper-1.19.1-111.jar"
paper119 = "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/81/downloads/paper-1.19-81.jar"
paper1182 = "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/379/downloads/paper-1.18.2-379.jar"
paper1181 = "https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/216/downloads/paper-1.18.1-216.jar"
paper118 = "https://papermc.io/api/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar"
paper1171 = "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar"
paper117 = "https://papermc.io/api/v2/projects/paper/versions/1.17/builds/66/downloads/paper-1.17-66.jar"
paper1165 = "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar"
paper1164 = "https://papermc.io/api/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar"
paper1163 = "https://papermc.io/api/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar"
paper1162 = "https://papermc.io/api/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar"
paper1161 = "https://papermc.io/api/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar"
paper1152 = "https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/391/downloads/paper-1.15.2-391.jar"
paper1144 = "https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/243/downloads/paper-1.14.4-243.jar"
paper1132 = "https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/655/downloads/paper-1.13.2-655.jar"
paper1122 = "https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar"
paper1112 = "https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1104/downloads/paper-1.11.2-1104.jar"
paper1102 = "https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/916/downloads/paper-1.10.2-916.jar"
paper194 = "https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/773/downloads/paper-1.9.4-773.jar"
paper188 = "https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar"

# Spigot
spigot1201 = "https://download.getbukkit.org/spigot/spigot-1.20.1.jar"
spigot1194 = "https://download.getbukkit.org/spigot/spigot-1.19.4.jar"
spigot1193 = "https://download.getbukkit.org/spigot/spigot-1.19.3.jar"
spigot1192 = "https://download.getbukkit.org/spigot/spigot-1.19.2.jar"
spigot1191 = "https://download.getbukkit.org/spigot/spigot-1.19.1.jar"
spigot119 = "https://download.getbukkit.org/spigot/spigot-1.19.jar"

# Magma
magma1193 = "https://git.magmafoundation.org/api/v4/projects/103/packages/maven/org/magmafoundation/Magma/1.19.3-44.1.23-6e6ce905/Magma-1.19.3-44.1.23-6e6ce905-server.jar"
magma1182 = "https://git.magmafoundation.org/api/v4/projects/5/packages/maven/org/magmafoundation/Magma/1.18.2-40.2.10-2129b008/Magma-1.18.2-40.2.10-2129b008-server.jar"
magma1165 = "https://git.magmafoundation.org/api/v4/projects/8/packages/maven/org/magmafoundation/Magma/1.16.5-36.2.39-c1c5a946/Magma-1.16.5-36.2.39-c1c5a946-server.jar"
magma1122 = "https://git.magmafoundation.org/api/v4/projects/7/packages/maven/org/magmafoundation/Magma/1.12.2-de16e0a9/Magma-1.12.2-de16e0a9.jar"


# Logo
print("╔═╗╔═╗───────────────╔═╦╗╔═══╗────────────╔══╗────╔╗──╔╗")
print("║║╚╝║║───────────────║╔╝╚╣╔═╗║────────────║╔╗║────║║──║║")
print("║╔╗╔╗╠╦═╗╔══╦══╦═╦══╦╝╚╗╔╣╚══╦══╦═╦╗╔╦══╦═╣╚╝╚╦╗╔╦╣║╔═╝╠══╦═╗")
print("║║║║║╠╣╔╗╣║═╣╔═╣╔╣╔╗╠╗╔╣║╚══╗║║═╣╔╣╚╝║║═╣╔╣╔═╗║║║╠╣║║╔╗║║═╣╔╝")
print("║║║║║║║║║║║═╣╚═╣║║╔╗║║║║╚╣╚═╝║║═╣║╚╗╔╣║═╣║║╚═╝║╚╝║║╚╣╚╝║║═╣║")
print("╚╝╚╝╚╩╩╝╚╩══╩══╩╝╚╝╚╝╚╝╚═╩═══╩══╩╝─╚╝╚══╩╝╚═══╩══╩╩═╩══╩══╩╝")
print("")
print(Fore.CYAN + "Made by Luden :)")
print(Style.RESET_ALL + "")

time.sleep(1)

# Check Intenert
try:
    print("Checking your internet connection...")
    time.sleep(0.5)
    response = requests.get(url)
    print(Fore.GREEN + "Internet Connected")
    print(Style.RESET_ALL + "")
    time.sleep(0.5)
except requests.exceptions.ConnectionError:
    print("")
    input(
        Fore.RED + "You are not connected to internet, check your connection and try again." + Fore.GREEN + "\nPress enter to exit.")
    exit()

# Main

number2 = ""

while True:
    print("Menu: ")
    print("")
    time.sleep(0.5)
    print("1 | Create a server")
    print("2 | Start a Server")
    print("")
    number = input("Please enter the number: ")
    print("")

    # create server - software types:
    if number == "1":
        print("Software types: ")
        print("")
        time.sleep(0.5)
        print("1 | Paper")
        print("2 | Spigot")
        print("3 | Magma")
        print("")
        number2 = input("Please enter the number: ")
        print("")

    # start server:
    elif number == "2":
        custom_route_create = input("Enter the name of the server folder (Just enter the name): ")

        route_folder = os.path.join(custom_route_create)

        if not os.path.exists(custom_route_create):
            print("This folder does not exist.")
            continue

        found_jar = False

        for filejar in os.listdir(custom_route_create):
            if filejar.endswith(".jar"):
                found_jar = True
                route_folder2 = os.path.join(custom_route_create, filejar)
                print(f"Found .jar file: {filejar}")
                break
        if not found_jar:
            print("Server .jar file could not be found")
            continue

        while True:
            try:
                custom_ram_str = input("How many gigabytes of RAM do you want (With number): ")
                custom_ram = int(custom_ram_str)

                if 1 <= custom_ram <= 64:
                    gb = str(1024 * custom_ram)

                    print(f"Running server with {gb} MB RAM")

                    time.sleep(2)

                    try:
                        subprocess.run(f"java -Xmx{gb}M -Xms512M -jar {filejar} nogui", shell=True,
                                       cwd=custom_route_create)
                    except Exception as e:
                        print("Error executing the command:", e)

                    time.sleep(1)
                    print("good luck:)")
                    exit()
                else:
                    print("Please enter a number between 1 and 64.")
            except ValueError:
                print("Specified input wasn't a number. Please enter a valid number.")

    # Software Versions:

    # PAPER CLASS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # paper - number3
    if number2 == "1":
        time.sleep(1.5)
        print("List of Paper versions:")
        print("")
        print("→ 1.20.1")
        print("→ 1.20")
        print("→ 1.19.4")
        print("→ 1.19.3")
        print("→ 1.19.2")
        print("→ 1.19.1")
        print("→ 1.19")
        print("→ 1.18.2")
        print("→ 1.18.1")
        print("→ 1.18")
        print("→ 1.17.1")
        print("→ 1.17")
        print("→ 1.16.5")
        print("→ 1.16.4")
        print("→ 1.16.3")
        print("→ 1.16.2")
        print("→ 1.16.1")
        print("→ 1.15.2")
        print("→ 1.14.4")
        print("→ 1.13.2")
        print("→ 1.12.2")
        print("→ 1.11.2")
        print("→ 1.10.2")
        print("→ 1.9.4")
        print("→ 1.8.8")
        print("")
        number3 = input("Please enter the version: ")

        if number3 == "1.20.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.20.1-45.jar")

            response = requests.get(paper1201)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.20":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.20-17.jar")

            response = requests.get(paper120)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.19.4":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.19.4-550.jar")

            response = requests.get(paper1194)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.19.3":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.19.3-448.jar")

            response = requests.get(paper1193)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.19.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.19.2-307.jar")

            response = requests.get(paper1192)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.19.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.19.1-111.jar")

            response = requests.get(paper1191)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.19":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.19-81.jar")

            response = requests.get(paper119)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.18.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.18.2-379.jar")

            response = requests.get(paper1182)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.18.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.18.1-216.jar")

            response = requests.get(paper1181)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.18":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.18-66.jar")

            response = requests.get(paper118)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.17.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.17.1-408.jar")

            response = requests.get(paper1171)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.17":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.17-66.jar")

            response = requests.get(paper117)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.16.5":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.16.5-790.jar")

            response = requests.get(paper1165)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.16.4":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.16.4-416.jar")

            response = requests.get(paper1164)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.16.3":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.16.3-253.jar")

            response = requests.get(paper1163)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.16.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.16.2-189.jar")

            response = requests.get(paper1162)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.16.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.16.1-138.jar")

            response = requests.get(paper1161)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.15.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.15.2.jar")

            response = requests.get(paper1152)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.14.4":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.14.4-243.jar")

            response = requests.get(paper1144)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.13.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.13.2-655.jar")

            response = requests.get(paper1132)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.12.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.12.2-1618.jar")

            response = requests.get(paper1122)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.11.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.11.2-1104.jar")

            response = requests.get(paper1112)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.10.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.10.2-916.jar")

            response = requests.get(paper1102)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.9.4":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.9.4-773.jar")

            response = requests.get(paper194)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number3 == "1.8.8":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.8.8-443.jar")

            response = requests.get(paper188)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        else:
            print("Specified input wasn't a versiom.\nPress enter to exit")
            exit()

    # SPIGOT CLASS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # spigot - number4
    elif number2 == "2":
        time.sleep(1.5)
        print("List of Spigot versions:")
        print("")
        print("→ 1.20.1")
        print("→ 1.19.4")
        print("→ 1.19.3")
        print("→ 1.19.2")
        print("→ 1.19.1")
        print("→ 1.19")
        print("")
        number4 = input("Please enter the version: ")

        if number4 == "1.20.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "paper-1.20.1-45.jar")

            response = requests.get(spigot1201)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number4 == "1.19.4":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "spigot-1.19.4.jar")

            response = requests.get(spigot1194)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number4 == "1.19.3":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "spigot-1.19.3.jar")

            response = requests.get(spigot1193)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number4 == "1.19.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "spigot-1.19.2.jar")

            response = requests.get(spigot1192)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number4 == "1.19.1":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "spigot-1.19.1.jar")

            response = requests.get(spigot1191)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number4 == "1.19":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "spigot-1.19.jar")

            response = requests.get(spigot119)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        else:
            print("Specified input wasn't a versiom.\nPress enter to exit")
            exit()

    # MAGMA CLASS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # magma - number4
    elif number2 == "3":
        time.sleep(1.5)
        print("List of Magma versions:")
        print("")
        print("→ 1.19.3")
        print("→ 1.18.2")
        print("→ 1.16.5")
        print("→ 1.12.2")
        print("")
        number5 = input("Please enter the version: ")

        if number5 == "1.19.3":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "Magma-1.19.3-44.1.23-6e6ce905-server.jar")

            response = requests.get(magma1193)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number5 == "1.18.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "Magma-1.18.2-40.2.10-2129b008-server.jar")

            response = requests.get(magma1182)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number5 == "1.16.5":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "Magma-1.16.5-36.2.39-c1c5a946-server.jar")

            response = requests.get(magma1165)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        elif number5 == "1.12.2":
            custom_route = input("Enter the name of the server folder (Just enter the name): ")

            route_folder = os.path.join(custom_route)

            if not os.path.exists(custom_route):
                os.makedirs(custom_route)
                print(f"Created folder: '{custom_route}'")

            print("Wait 5 seconds...")
            time.sleep(5)

            file_path = os.path.join(route_folder, "Magma-1.12.2-de16e0a9.jar")

            response = requests.get(magma1122)

            if response.status_code == 200:
                with open(file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"The .jar file has been successfully downloaded to '{file_path}'.")
                exit()
            else:
                print("The file could not be downloaded. Response code:",
                      response.status_code + "\nPress enter to exit")
        else:
            print("Specified input wasn't a versiom.\nPress enter to exit")
            exit()
