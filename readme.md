# Packages installés

Voici la liste des packages à installer sur le Raspberry Pi pour que le code fonctionne.

```bash
# Installation des packages
sudo apt-get install -y libbluetooth-dev libusb-dev libreadline-dev libglib2.0-dev libudev-dev libdbus-1-dev libical-dev libdbus-glib-1-dev python3-pip python3-dbus

# Création de l'environnement virtuel et activation
python3 -m .venv --system-site-packages .venv && source .venv/bin/activate

# Installation du package bluezero dans l'environnement virtuel
pip install git+https://github.com/ukBaz/python-bluezero.git
```
