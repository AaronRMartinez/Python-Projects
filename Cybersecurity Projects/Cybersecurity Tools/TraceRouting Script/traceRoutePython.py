import argparse
import ipaddress
import time
import scapy.all as scapy

R = "\033[1;31m";    #red color
Y = "\033[1:33m";    #yellow color
C = "\033[1:36m";    #cyan color
W = "\033[0m";       #white color

parser = argparse.ArgumentParser(description="IP tracerouting python script")
parser.add_argument('-t','--target_ip_address',             help="Target IP Address to be tracerouted")
parser.add_argument('-m','--max_hop_limit', type=int,       help="Maximum Hop Limit")

## get the arguments
args = parser.parse_args()
target_ip_address = args.target_ip_address
max_hop_limit = args.max_hop_limit

print(target_ip_address,max_hop_limit)

## validate ip address
def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

if(is_valid_ip(target_ip_address) == False):
    print(R, "Invalid IP Address",W)
    exit(1)

# TTL initialization
TTL = 1
print(R,"IP Tracerouting start...",W)
T1 = time.time()
while (TTL <= max_hop_limit):
    ICMP_PKT = scapy.IP(dst=target_ip_address,ttl=TTL)/scapy.ICMP()     #ICMP Packet = IP header + ICMP Header
    ans = scapy.sr1(ICMP_PKT,timeout=3,retry=1,verbose=False)           #send ICMP Packet
    ## valid response is received
    if(isinstance(ans,type(None)) == False):
        ##ICMP TTL expired
        if(ans[1].type == 11 and ans[1].code == 0):
              print("router",C,ans[0].src,W," | TTL:",TTL)
              TTL += 1
        ##ICMP echo reply
        if(ans[1].type==0):
            print("router",C,target_ip_address,W," | TTL:",TTL)
            break
    ##no response is received
    else:
        print(R,"Unknown router",W," | TTL:",TTL)

T2 = time.time()
print("IP Tracerouting done in",R,T2-T1,W,"seconds")