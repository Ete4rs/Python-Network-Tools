import scapy.all as scapy
from argparse import ArgumentParser
from scapy.layers import http

def get_args():
    arg_parser = ArgumentParser('Argument Parser')
    arg_parser.add_argument('-i', '--interface', help='Interface', required=True, dest='interface')
    return arg_parser.parse_args()


def get_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet.show())


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=get_sniff_packet)


if __name__ == '__main__':
    sniff(get_args().interface)
