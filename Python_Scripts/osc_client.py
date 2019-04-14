from pythonosc import osc_message_builder
from pythonosc import udp_client
import time
import sys
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--next", "-n", help="set output width")
parser.add_argument("--prev", "-p", help="set output width")
parser.add_argument("--knob", "-k",type=int, nargs='+',help="set output width")
parser.add_argument("--trigger", "-t", help="set output width")
parser.add_argument("--osd", "-o", help="set output width")
parser.add_argument("--screen", "-s", help="set output width")
parser.add_argument("--autoclear", "-a", help="set output width")
args = parser.parse_args()

print(args.next)
print(args.knob)
print(args.trigger)
print(args.osd)
print(args.screen)
print(args.autoclear)

ip = "192.168.1.115"
port = 4000

client = udp_client.SimpleUDPClient(ip, port)

def prev(message):
    #number must be in range of all available modes
    client.send_message("/key", [1,1])

def next(message):
    #number must be in range of all available modes
    client.send_message("/key", [2,1])

def knobs(message):
    #
    client.send_message("/knobs", message)
    #client.send_message("/knobs", [i,i,i,i,i,i])

def osd(message):
    # toggle on and off
    i = int(message)
    client.send_message("/key", [3,i])

def trigger(i):
    # positive turn on, negative turns off
    client.send_message("/key", [9,i])
 
def screen(i):
    # positive turn on
    client.send_message("/key", [7,i])
  
def autoclear(i):
    # positive turn off negative on
    client.send_message("/key", [8,i])
    

if args.knob:
    knobs(args.knob)
if args.osd:
    osd(int(args.osd))
if args.trigger:
    trigger(int(args.trigger))
if args.prev:
    prev(int(args.prev))
if args.next:
    next(int(args.next))
if args.screen:
    next(int(args.screen))
if args.autoclear:
    autoclear(int(args.autoclear))

