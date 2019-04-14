from pythonosc import osc_message_builder
from pythonosc import udp_client
import time
import sys
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--program", "-p", help="set output width")
parser.add_argument("--knob", "-k", help="set output width")
args = parser.parse_args()

print(args.program)

ip = "192.168.1.115"
port = 4000

client = udp_client.SimpleUDPClient(ip, port)

def knobs(message):
    print(message)
    for i in range(message,message+1):
        client.send_message("/knobs", [i,i,i,i,i,i])
        time.sleep(.07)
knobs(int(args.knob))


