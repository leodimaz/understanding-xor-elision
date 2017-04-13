# UNDERSTAING XOR ELISION

import sys

def xor(a,b):
	if a==b:
		return 0
	elif a!=b:
		return 1

def xor_messages(a,b):
	if len(a)!=len(b):
		print "[-] String len must be equal"
		sys.exit(0)
	res=[]
	for x in range(0,len(a)):
		res.append(xor(a[x],b[x]))
	return res

def to_arr(a):
	vect=[]
	for x in range(len(a)):
		vect.append(int(a[x]))
	return vect

def int_arr_to_text_arr(a):
	arr=[]
	for x in range(len(a)):
		arr.append(str(a[x]))
	return arr

def arr_to_string(a):
	return "".join(a)

def usage():
	print "Usage: vernam_chiper.py message key"

def main():
	try:
		message = sys.argv[1]
		key = sys.argv[2]
	except:
		usage()
		sys.exit(0)

	message = to_arr(message)
	key = to_arr(key)
	chipertext = xor_messages(message,key)
	decripted_message = xor_messages(chipertext,key)
	decripted_key = xor_messages(chipertext,message)
	print "\n"
	print "MESSAGE           : "+arr_to_string(int_arr_to_text_arr(message))
	print "KEY               : "+arr_to_string(int_arr_to_text_arr(key))
	print "CHIPERTEXT        : "+arr_to_string(int_arr_to_text_arr(chipertext))+" (MESSAGE xor KEY)" 
	print "\n"
	print "DECRYPTED_MESSAGE : "+arr_to_string(int_arr_to_text_arr(decripted_message))+" (CHIPERTEXT xor KEY)"
	print "DECRYPTED_KEY     : "+arr_to_string(int_arr_to_text_arr(decripted_key))+" (CHIPERTEXT xor MESSAGE)"
	print "\n"

if __name__ == "__main__":
	main()
