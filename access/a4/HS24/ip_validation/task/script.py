#!/usr/bin/env python3

def is_valid_IPv4_octet(octet):

    return str(octet).isdigit() and 0 <= int(octet) <= 255
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""

def is_valid_IPv4(ip):

    # Check if ip consists of 4 octets 
    if not len(ip.split('.')) == 4:
        return False
    
    for i in ip.split('.'):
        if not is_valid_IPv4_octet(str(i)):
            return False
        
    return True

def is_valid_IPv6_hextet(hextet):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    pass

def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    pass

def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    pass

# You should look at task/test.py and extend the test suite we provided!

print(is_valid_IPv4("127.0.0.1"))