from pythonosc import osc_message_builder
from pythonosc import udp_client
import time
import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()

print(args)

ip = "192.168.1.115"
port = 4000

client = udp_client.SimpleUDPClient(ip, port)

def knobs(message):
    print(message)
    for i in range(0,1000):
        client.send_message("/knobs", [i,i,i,i,i,i])
        time.sleep(.07)
knobs('here')


