import logging
import random
from bluezero import adapter
from bluezero import peripheral

# SERVICE UUID
# TODO : Modifier ces GUID pour mettre les vôtres. Vous devez avoir les mêmes dans le code python ET dans votre app mobile
BOT_SERVICE_PRINCIPAL = '15ff0fcd-6481-4565-9fe0-388628769cce'
BOT_CARACTERISTIQUE_COMMANDES = '34a28b10-1486-4c61-9fa1-878296fd0262'


class BLEService:
    def __init__(self):
        # Get the default adapter address
        self.adapter_address = list(adapter.Adapter.available())[0].address
        
        # Création du périphérique BLE
        self.logger = logging.getLogger('localGATT')
        self.logger.setLevel(logging.DEBUG)

        print('Initialisation du périphérique BLE')
        # Create peripheral
        self.bot_monitor = peripheral.Peripheral(self.adapter_address,
                                            local_name='mlandry PI - bot',
                                            appearance=1344)
        
        # Add service
        self.bot_monitor.add_service(srv_id=1, uuid=BOT_SERVICE_PRINCIPAL, primary=True)
        
        # Add characteristic
        self.bot_monitor.add_characteristic(srv_id=1, chr_id=1, uuid=BOT_CARACTERISTIQUE_COMMANDES,
                                       value=[], notifying=False,
                                       flags=['write', 'write-without-response', 'read'],
                                       read_callback=self.read_value,
                                       write_callback=self.write_value,
                                       notify_callback=None
                                       )

    def write_value(self, value, options):
        print(f"Write request received: {value}")	
        # Note use of control_point, to assign one or more values into variables
        # from struct.unpack output which returns a tuple
        try:
            cmd_str = value.decode("utf-8")
            print(f"Commande reçue: {cmd_str}")
        except Exception as e:
            print(f"Erreur de décodage: {e}")

        
    def read_value(self): 
        print(f"Read request received")
        # TODO: retourner les infos demandées.
        cpu_value = random.randrange(3200, 5310, 10) / 100
        return list(int(cpu_value * 100).to_bytes(2, byteorder='little', signed=True))


    def start(self):
        self.bot_monitor.publish()