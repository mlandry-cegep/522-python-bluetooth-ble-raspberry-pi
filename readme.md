# Packages installés

Voici la liste des packages à installer sur le Raspberry Pi pour que le code fonctionne.

```bash
# Pour bluezero
sudo apt-get install -y libbluetooth-dev libusb-dev libreadline-dev libglib2.0-dev libudev-dev
sudo apt-get install libdbus-1-dev libical-dev libdbus-glib-1-dev python3-pip python3-dbus
sudo apt-get install -y libcairo2-dev libgirepository1.0-dev

.venv/bin/pip install git+https://github.com/ukBaz/python-bluezero.git
```
