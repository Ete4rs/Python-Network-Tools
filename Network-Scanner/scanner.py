import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = broadcast/arp_request
    answered, unanswered = scapy.srp(packet, timeout=5)
    print_result(answered)


def print_result(answered):
    print('     IP                         Mac Address')
    for client in answered:
        print(client[1].psrc, '                ', client[1].hwsrc)


if __name__ == '__main__':
    scan(input('Ip/network (192.168.1.0/24) : '))
