# Digital Culture Server
The purpose of the DC Server is to be an MQTT broker and IOT automation hub. 
The services that it will provide is being an MQTT client, and converting some of the MQTT topics into UDP messages.
The benefit of converting some messages to UDP is that they can more easily be consumed by Pure Data and Max MSP.
So, this server allows for artistic expression of IOT data and use of IOT devices.

Based off of Node Red because of its ease of use and support, as well as the web based graphic interface. 

To convert MQTT to UDP, there is a standalone python script that is a MQTT broker and converts to UDP, if Node Red installation is not necessary or desirable.
This implementation will be done on a Raspberry Pi.





## Getting Started

On many Pi OS images there is Node-Red already installed. It can be started from the terminal by typing node-red. The server will start and tell you the ip address that its running on, like:  [info] Server now running at http://127.0.0.1:1880/. Because we gave the Pi a reserved ip on the wifi router, and my laptop is using the same network, I open the Node-Red web interface using the Pis ip, and the port 1880. 


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Networking:
1) Standalond wifi-router, with Pi plugged directly into the ethernet.
2) Adjust the DHCP Reservation of the router to give the Pi a static ip, a reserved ip address.

Running headless:



```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

