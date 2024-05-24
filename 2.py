
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
