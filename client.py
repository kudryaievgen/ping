import struct
import socket
import time
import sys
import bug

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    s = socket.socket()
    s.connect((host, port))
    packet_count = 0
    print("Pinging " + host)
    while packet_count != 4:
        packet_count += 1
        packet = struct.pack("!Hd", packet_count, time.time())
        s.send(packet)
        print("Sent packet " + str(packet_count))
        callback = s.recv(1024)
        (seq, timestamp) = struct.unpack("!Hd", callback)
        delay = time.time() - timestamp
        delay *= 1000
        print("Packet " + str(packet_count) + " has delay in " + str(delay) + "ms")
        time.sleep(1)
