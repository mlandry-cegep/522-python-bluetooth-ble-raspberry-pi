import logging

# Modules Bluezero pour la gestion Bluetooth Low Energy (BLE)
from bluezero import adapter
from bluezero import peripheral

# UUID du service principal
BOT_SERVICE_PRINCIPAL = '15ff0fcd-6481-4565-9fe0-388628769cce'
# UUID de la caractéristique des commandes
BOT_CARACTERISTIQUE_COMMANDES = '34a28b10-1486-4c61-9fa1-878296fd0262'

def write_value(value, options):
    # Fonction de callback appelée lors de la réception d'une commande d'écriture
    print(f"Demande d'écriture reçue: {value}")	
    # Conversion des données reçues en chaîne de caractères UTF-8
    cmd_str = value.decode("utf-8")

    print(f"Commande reçue: {cmd_str}")

def main(adapter_address):
    # Initialisation du périphérique BLE
    logger = logging.getLogger('localGATT')
    logger.setLevel(logging.DEBUG)

    print('Initialisation du périphérique BLE')
    # Création du périphérique BLE avec le nom local et l'apparence spécifiés
    bot_monitor = peripheral.Peripheral(adapter_address,
                                        local_name='mlandry PI - bot', # TODO: Modifier le nom du périphérique
                                        appearance=1344)
    # Ajout du service principal
    bot_monitor.add_service(srv_id=1, uuid=BOT_SERVICE_PRINCIPAL, primary=True)
    # Ajout de la caractéristique des commandes avec les callbacks appropriés
    bot_monitor.add_characteristic(srv_id=1, chr_id=1, uuid=BOT_CARACTERISTIQUE_COMMANDES,
                                   value=[], notifying=False,
                                   flags=['write', 'write-without-response'],
                                   read_callback=None,
                                   write_callback=write_value,
                                   notify_callback=None
                                   )

    # Publication du périphérique BLE
    bot_monitor.publish()

if __name__ == '__main__':
    # Démarrage du périphérique BLE
    main(list(adapter.Adapter.available())[0].address)