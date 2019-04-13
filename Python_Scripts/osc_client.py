
from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":
client = udp_client.SimpleUDPClient(, args.port)

  for x in range(10):
    client.send_message("/filter", random.random())
    time.sleep(1)
