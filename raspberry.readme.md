# Rasberry Read Me
## SD
- format
    - Etcher app
- flash
    ```bash
    diskutil list
    diskutil unmountDisk /dev/disk[n]
    sudo dd bs=1m if=[path_of_your_image].img of=/dev/rdisk[n]
    sudo diskutil eject /dev/rdisk[n]
    ```

## Find IP
- default network
    - 192.168.0.0
- nmap
```bash
sudo nmap -sP 192.168.0.0/24
```

----------
## OS
- Raspbian
    - default
        - user: pi
        - password: raspberry

----------
## IOT
- rpi 1
    - SD: 4GB
    - IP: DHCP
    - OS: Raspbian Lite
- rpi 2
    - SD: 16GB
    - IP: DHCP
    - OS: Raspbian Lite

----------

## Ideas

- alarm
    - led
    - voice
- sensor
    - temperature
    - air
    - proximity
- weather
    - station
- server
    - router
    - media center
    - cloud
    - storage
- bot
    - robot
    - chatbot
    - machine learning center

----------

## Setup
### Update the device
```bash
sudo apt-get update
sudo apt-get install vim
sudo apt-get install wpasupplicant
```
### SSH
- Enable SSH port
    - create a file named 'ssh' in /boot

- Connection
```bash
ssh [user]@[ip]
```
- Purge key
```bash
ssh-keygen -R [IP]
```

### WIFI
- Connect a dongle
```bash
# check the device network
ifconfig
# check the wifi network
sudo iwlist wlan0 scan
# get the name ESSID:"[name]"
# get the authentification IE: IEEE 802.11i/WPA2 Version 1
# this works for WPA/WPA2
```
- /etc/wpa_supplicant/wpa_supplicant.conf
```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network = {
    id_str='id'
    ssid = "[ESSID-1]"
    psk = "[password-1]"
    group = CCMP TKIP
    pairwise = CCMP TKIP
    key_mgmt = WPA-PSK
}
network = {
    id_str='id'
    ssid = "[ESSID-2]"
    psk = "[password-2]"
    group = CCMP TKIP
    pairwise = CCMP TKIP
    key_mgmt = WPA-PSK
}
```
- /etc/network/interfaces
```bash
# interfaces(5) file used by ifup(8) and ifdown(8)
# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback
allow-hotplug wlan0 eth0

iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

# DHCP
iface default inet dhcp

# Static IP
iface default inet static
    address 192.168.1.100
    netmask 255.255.255.0
    network 192.168.1.0
    gateway 192.168.1.1

# Multiple IP
iface [network-1] inet static
    address [network-1 address]
    netmask [network-1 netmask]
    network [network-1 network]
    broadcast [network-1 broadcast]
    gateway [network-1 gateway]

iface [network-2] inet static
    address [network-2 address]
    netmask [network-2 netmask]
    network [network-2 network]
    broadcast [network-2 broadcast]
    gateway [network-2 gateway]

```

- reboot
```bash
#sudo /etc/init.d/networking restart
#sudo ifup wlan0
#sudo ifdown wlan0
#sudo ifconfig wlan0 down
#sudo ifconfig wlan0 up
sudo reboot
```
### Users
- Add user
```bash
sudo adduser [user name]
```
- Delete user
```bash
sudo userdel -r [user name]
```
- Change user password
```bash
sudo passwd [user name]
```
- Remove user password
```bash
sudo passwd [user name] -d
```
- Sudoer
```bash
# set vim as default editor
sudo update-alternatives --set editor /usr/bin/vim.tiny
# edit sudo file
sudo visudo
```

### Machine
- /etc/hosts
```bash
127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

127.0.1.1       [machine name]
```
- /etc/hostname
```bash
[machine name]
```
- commit
```bash
sudo /etc/init.d/hostname.sh
```

### Run script at boot
- /etc/rc.local
