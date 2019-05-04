# Digital Culture Server
The purpose of the DC Server is to be an MQTT broker and IOT automation hub. 
The services that it will provide is being an MQTT client, and converting some of the MQTT topics into UDP messages.
The benefit of converting some messages to UDP is that they can more easily be consumed by Pure Data and Max MSP.
So, this server allows for artistic expression of IOT data and use of IOT devices.

Based off of Node Red because of its ease of use and support, as well as the web based graphic interface. 

To convert MQTT to UDP, there is a standalone python script that is a MQTT broker and converts to UDP, if Node Red installation is not necessary or desirable.
This implementation will be done on a Raspberry Pi.
 
 ![dashboard1]
 
## Reasoning and Motivations
IOT and the arts:
Stand alone server benefits:
Stand alone wifi-router: This project uses an additional wifi-router that is plugged into my homes wifi router, so it is interntet connected. But, the benefit of having this additional router layer is that I can take it with me to bring the network into locations that wouldn't have accessible wifi. Getting a battery operated wifi could make this potentially able to be run anywhere.

![dashboard2]


## Getting Started

On many Pi OS images there is Node-Red already installed. It can be started from the terminal by typing node-red. The server will start and tell you the ip address that its running on, like:  [info] Server now running at http://127.0.0.1:1880/. Because we gave the Pi a reserved ip on the wifi router, and my laptop is using the same network, I open the Node-Red web interface using the Pis ip, and the port 1880. 


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Networking:
1) Standalond wifi-router, with Pi plugged directly into the ethernet.
2) Adjust the DHCP Reservation of the router to give the Pi a static ip, a reserved ip address.

Running headless:

Running Mosquitto Broker automatically on boot

[dashboard1]: ./Images/node_red_dashboard.png
[dashboard2]:	./Images/ETC_Controls.png
