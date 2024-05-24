import wifi

# Fonction pour scanner les réseaux WiFi visibles
def scan_wifi_networks():
    cells = wifi.Cell.all('wlan0')
    
    print("Réseaux WiFi disponibles :")
    for i, cell in enumerate(cells):
        print(f"{i+1}. {cell.ssid}")

    choice = int(input("Veuillez choisir le numéro du réseau WiFi auquel vous souhaitez vous connecter : ")) - 1
    selected_network = cells[choice]
    
    return selected_network

# Fonction pour se connecter au réseau WiFi sélectionné
def connect_to_network(selected_network):
    password = input(f"Veuillez saisir le mot de passe pour {selected_network.ssid} : ")

    try:
        scheme = wifi.Scheme.for_cell('wlan0', selected_network.ssid, selected_network, password)
        scheme.save()
        print("Connexion réussie!")
    except wifi.exceptions.ConnectionError:
        print("Mot de passe incorrect. Veuillez réessayer.")

# Scanner les réseaux WiFi et se connecter
selected_network = scan_wifi_networks()
connect_to_network(selected_network)
