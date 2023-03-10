#!/bin/bash
device=$(lsusb | grep FT232 | cut -d":" -f1 | cut -d" " -f4)
folder=$(lsusb | grep FT232 | cut -d":" -f1 | cut -d" " -f2)

sudo chmod 777 /dev/bus/usb/$folder/$device
