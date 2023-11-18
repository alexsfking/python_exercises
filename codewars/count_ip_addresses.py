'''
### kyu 5 ###
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''

def ip_str_to_int(ip:str)->int:
    return int(''.join([bin(int(octet))[2:].zfill(8) for octet in ip.split('.')]),2)

def ips_between(start:str, end:str)->int:
    return ip_str_to_int(end)-ip_str_to_int(start)