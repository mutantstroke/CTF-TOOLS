#!/usr/bin/python

print("--------------------------------\nFind flag from two images \n-----------------------------------".upper())

a=str(raw_input("[+] Enter First Image : "))
b=str(raw_input("[+] Enter Second Image : "))

with open(a,'rb') as f:
	imagea=f.read()

with open(b,'rb') as f:
        imageb=f.read()

flag=''

for i in range(min(len(imagea),len(imageb))):
	if imagea[i] != imageb[i]:
		flag+=imageb[i]

print("\n[+]FLAG = "+flag+"\n---------------------------------------")
