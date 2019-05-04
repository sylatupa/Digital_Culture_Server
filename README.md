# Digital Culture Server
The purpose of the DC Server is to be an MQTT broker, IOT automation hub, and Web Interface for sending UDP messages. This server allows for artistic expression of IOT data and use of IOT devices. The benefit of converting some messages to UDP is that they can more easily be consumed by Pure Data and Max MSP. This largely uses Node-Red because of its ease of use and support, as well as the web based graphic interface. 

To convert MQTT to UDP, there is a standalone python script that is a MQTT broker and converts to UDP, if Node Red installation is not necessary or desirable.
This implementation will be done on a Raspberry Pi.
The services that it will provide are: 
- [x] Node-Red is an MQTT client, and converting some of the MQTT topics into UDP messages.
- [x] Node-Red provides a dashboard that allows for easy charting of data being published to the mosquitto server.
- [x] Graphical controls (sliders and buttons) that control the Critter and Guittari ETC Video Synthesizer and Pure Data sound synthesizer. 
- [x] Some custom python scripts that send OSC messages, as the Node-Red objects werent working well.

 
 ![dashboard1]
 
This project uses an additional wifi-router that is plugged into my homes wifi router, so it is interntet connected. But, the benefit of having this additional router layer is that I can take it with me to bring the network into locations that wouldn't have accessible wifi. Getting a battery operated wifi could make this potentially able to be run anywhere.

![dashboard2]



## Getting Started

On many Pi OS images there is Node-Red already installed. It can be started from the terminal by typing node-red. The server will start and tell you the ip address that its running on, like:  [info] Server now running at http://127.0.0.1:1880/. Because we gave the Pi a reserved ip on the wifi router, and my laptop is using the same network, I open the Node-Red web interface using the Pis ip, and the port 1880. 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

To build the dashboards and controls in Node-Red, import the following flow file into your Node-Red instance. It will require the addition of the Dashboard plugin.
[node_red_flows.json](./node_red_flows.json)


### Prerequisites

Networking:
1) Standalond wifi-router, with Pi plugged directly into the ethernet.
2) Adjust the DHCP Reservation of the router to give the Pi a static ip, a reserved ip address.


Running headless:

Running Mosquitto Broker automatically on boot

## parallel_projects
The Digital_Thing is built in the context of a Digital Culture, Arts Media and Engineering, Master of Arts program and some of the following project examples are with interactive art and media. 
* [Digital_Culture_Server](https://github.com/sylatupa/Digital_Culture_Server)
** A collection of Node-Red Flows and Python Scripts. This runs on a Raspberry Pi and is connected to WiFi.
** The Digital_Thing takes sensor data and sends it over an MQTT Network. Node Red recieves this data and sends it the ETC Video Synthesizer and the Digital_Culture_Sound_Client, over OSC.  
* [Digital_Culture_Sound_Client](https://github.com/sylatupa/Digital-Culture-Sound-Client)
** A sound synthesizer written in Pure Data. This runs on a Raspberry Pi and is connected to Wifi and controlled by Node-Red and This_Thing.
* [Video_Synth-ETC_Mother_and-Modes](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes)
** written by Critter and Guitari for the ETC. This is installed on a Raspberry Pi that is connected to WiFi and controlled by Node-Red and This_Thing.


[dashboard1]: ./Images/node_red_dashboard.png
[dashboard2]:	./Images/ETC_Controls.png
