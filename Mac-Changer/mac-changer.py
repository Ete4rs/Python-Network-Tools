from subprocess import run
from sys import exit
from argparse import ArgumentParser
import re


def arg_parsing():
    parser = ArgumentParser(description='Args parser')
    parser.add_argument('-m', '--mac', required=True, help='new mac address', dest='mac_address')
    parser.add_argument('-i', '--interface', required=True, help="Interface", dest='interface')
    return parser.parse_args()


def check_mac_address(mac):
    if re.match('[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$', mac):
        return True
    return False


def change_mac_address():
    run("ifconfig " + args.interface + " down", shell=True)
    run("ifconfig " + args.interface + " hw ether " + args.mac_address, shell=True)
    run("ifconfig " + args.interface + " up", shell=True)


if __name__ == '__main__':
    args = arg_parsing()
    if not check_mac_address(args.mac_address):
        print('invalid mac address')
        exit(0)
    change_mac_address()
