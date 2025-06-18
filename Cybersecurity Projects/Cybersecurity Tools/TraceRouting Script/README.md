# Python Tracerouting Tool

## What is Traceroute?

Traceroute is a network diagnostic tool used to track the path that data packets take from your computer to a destination (like a website or server) across a network, usually the Internet. When you send data over the Internet, it travels through several devices called routers before reaching its destination. Traceroute helps you see each of these "hops" along the way.

### How Does It Work?

1. **Packets with Time-To-Live (TTL):** Traceroute sends packets with a small "time-to-live" (TTL) value. TTL tells the packet how many routers it can pass through before being discarded.

2. **Each Hop Responds:** When a router discards the packet because its TTL reached 0, it sends a "Time Exceeded" message back. Traceroute records this response.

3. **Increment TTL:** Traceroute increases TTL by 1 and sends the packet again. This way, it discovers the next router in the path.

4. **Repeat Until Destination:** This process continues until the packet reaches the final destination or until a set number of hops is reached.

---

## This Python Tool

This Python script is a basic Traceroute implementation. It sends ICMP packets (like "ping") to a destination IP address, gradually increasing the TTL (Time-To-Live) to map the path (hops) through the network, revealing each router along the way.

### Argument Parsing (Command Line Inputs)

```python
parser = argparse.ArgumentParser(description="IP tracerouting python script")
parser.add_argument('-t','--target_ip_address', help="Target IP Address to be tracerouted")
parser.add_argument('-m','--max_hop_limit', type=int, help="Maximum Hop Limit")

args = parser.parse_args()
target_ip_address = args.target_ip_address
max_hop_limit = args.max_hop_limit
```

The script accepts:
* `-t` or `--target` : IP you want to trace
* `-m` or `--max_hop_limit` : Maximum number of hops to attempt

### IP Validation

```python
def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
```

Checks if the provided IP is valid and if the IP is invalid, the scripts prints out an error and exits.

### Traceroute Logic

```python
TTL = 1
print(R,"IP Tracerouting start...",W)
T1 = time.time()
```

Starts TTL at 1 and records the start time to measure duration.

```python
while (TTL <= max_hop_limit):
    ICMP_PKT = scapy.IP(dst=target_ip_address,ttl=TTL)/scapy.ICMP()
    ans = scapy.sr1(ICMP_PKT,timeout=3,retry=1,verbose=False)
```

Creates an ICMP packet with the current TTL of 1 and sends the packet and waits for a reply.

```python
if(ans[1].type == 11 and ans[1].code == 0):
    print("router",C,ans[0].src,W," | TTL:",TTL)
    TTL += 1
```

Checks if a response is received, will print the routers that have replied.

```pyhton
if(ans[1].type==0):
    print("router",C,target_ip_address,W," | TTL:",TTL)
    break
```

Returns the final destination and breaks the loop.

```python
else:
    print(R,"Unknown router",W," | TTL:",TTL)
```

If no ICMP reply is received (timeout), it prints "Unknown router".

```python
T2 = time.time()
print("IP Tracerouting done in",R,T2-T1,W,"seconds")
```

Prints how long the entire traceroute took.
