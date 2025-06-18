# Python Tracerouting Tool

## What is Traceroute?

Traceroute is a network diagnostic tool used to track the path that data packets take from your computer to a destination (like a website or server) across a network, usually the Internet. When you send data over the Internet, it travels through several devices called routers before reaching its destination. Traceroute helps you see each of these "hops" along the way.

### How Does It Work?

1. Packets with Time-To-Live (TTL):
Traceroute sends packets with a small "time-to-live" (TTL) value. TTL tells the packet how many routers it can pass through before being discarded.

2. Each Hop Responds:
When a router discards the packet because its TTL reached 0, it sends a "Time Exceeded" message back. Traceroute records this response.

3. Increment TTL:
Traceroute increases TTL by 1 and sends the packet again. This way, it discovers the next router in the path.

4. Repeat Until Destination:
This process continues until the packet reaches the final destination or until a set number of hops is reached.
