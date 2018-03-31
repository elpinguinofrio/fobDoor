# DCTRL smart crypto door
## prepare raspberry pi 3 model B
Install new Raspbian Lite OS on (https://www.raspberrypi.org/downloads/raspbian/)
#### install wifi
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
# add text to the file
network={
    ssid="55C9EA"
    psk=*DCTRL_wifi_password*
}
```
#### turn on SSH
```
sudo raspi-config
> Interfacing Options
> SSH
```
#### fix locale (probably still doesn’t work)
```
export LANGUAGE=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
dpkg-reconfigure locales
LC_MESSAGES=en_US.UTF-8
LC_CTYPE=en_US.UTF-8
LC_ALL=en_US.UTF-8
```
#### rename hostname
```
# edit default hostname “raspberrypi” in the two files, for something cool like dctrl_door_pi_1
sudo nano /etc/hosts
sudo nano /etc/hostname
sudo /etc/init.d/hostname.sh
sudo reboot
```
#### Login to the pi and install the repo code
now everything should work, so try to login to the pi via ssh
```
ssh pi@*ip_address_of_the_pi*
# default pi password is “raspberry”
git clone https://github.com/elpinguinofrio/fobDoor.git
```
## prepare python3 environment
```
sudo apt-get install git
sudo apt-get install python3-pip
sudo pip3 install python-dateutil --upgrade
sudo pip3 install gtts —upgrade
```
## run a python3 code
```
sudo python3 door.py
```
## install autoreboot
```
sudo chown root:root startup.sh
sudo chmod ug+x startup.sh
```
add line `/home/pi/fobDoor/startup.sh &` to `/etc/rc.local` file

## enjoy

## todo
make project according to http://docs.python-guide.org/en/latest/writing/structure/
