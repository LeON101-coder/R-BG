#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# This R-BG just for Tool Remove Background a Foto
# Use with simple not skill editor

import os;
import sys;
from time import *
import random;

try:
	import requests;
except:
	exit("[*] 'requests' module: bad")

def Remove():
	os.system('clear');
	print("[*] Remove Background a foto with simple step");
	print("[*] Not require editor skill");
	print(68*"-");
	print();
	file = input("[?] File Address a Foto : ");
	op = open(file, 'rb')
	if file == "":
		exit("Error");
	else:
		pass
	sleep(1)
	print("\nProcessing...");
	print();
	DATA = requests.post('https://api.remove.bg/v1.0/removebg', files = {'image_file':op}, data = {'size':'auto', 'bg_color':None}, headers = {'X-Api-Key': 'cD5ogD7V12dLAdkSfutJcHgT'},)
	if DATA.status_code == requests.codes.ok:
		files = open(file+'_result.png', 'wb');
		files.write(DATA.content);
		pass
	else:
		exit(DATA.text);
	print("\nSucc, file saved : "+file+'_result.png');

if __name__=='__main__':
	try:
		Remove();
	except IOError:
		exit("[!] Foto not found");
	except (KeyboardInterrupt, EOFError):
		exit();
