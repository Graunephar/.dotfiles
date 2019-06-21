#!/bin/sh


DEVICES=$(ioreg -r -l -n AppleHSBluetoothDevice | egrep '"BatteryPercent" = |^  \|   "Bluetooth Product Name" = ') #Lets get a list of all bluetooth devices

DEVICELINE=$(grep -n "$1" <<< "$DEVICES") #$1 is the device that this script was called with. Lets extract only the line ith that device
if [$DEVICELINE = ""]
then

	echo "" #Device not present, lets give BTT an empty string

else

	LINENR="${DEVICELINE:0:1}" #Then we find out where the line of the device is located

	NEXTLINE=$(expr $LINENR + "1") #The battery level is at the next line therefore we increment the line number
	SEDCOMMAND="p"

	BATTERYLINE=$(echo "$DEVICES" | sed -n  $NEXTLINE$SEDCOMMAND) # Now we can extract the line with the battery percent

	echo $BATTERYLINE | sed 's/[^[:digit:]]//g' #Finally we just need to get the digit and echo that to BTT

fi
