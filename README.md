# Worthington-Cryo-Logger
This script connects to the virtual com port (Phisically connected to the control unit on the remote site) and sends a trigger command to receive the temperature data from the control unit.
Get temperature logs from Worthington Cryo Tanks Control Units using RS232 over TCP-IP

Control Panel (M507CE-IEC) has a Digi Connect ME RS232 to Ethernet Adapter which makes the RS232 port on the control unit available over TCP/IP network.

## Requirements

* You should install the Realport Driver to your operating system and make sure that you have a virtual COM port (tty on linux) working. To validate the communication, connect to the specific port and send "@03S000000000096" string exactly. If you receive a string like "@03R2212201408AB0000001BC1" that means you are good to go. (Hint: Putty for Windows or Screen for Linux)

You can download the realport driver files here : https://hub.digi.com/support/products/realport/?path=/support/asset-collection/connect-sp-os-specific-drivers/

## Example string received from control unit:
@03R2212201408AB0000001BC1

@03R - 22 - 12 - 20 - 14 - 08 - AB - 0000001BC1

1. Part - Unknown
2. Part - Year
3. Part - Month
4. Part - Day
5. Part - Hour
6. Part - Minute
7. Part - Temperature in Celsius in HEX
8. Part - Unknown (Possible event/log id, should be always increasing)

Temperature part is the 7th part.

## Installation

pip install -r requirements.txt

## Usage

python3 getData.py
