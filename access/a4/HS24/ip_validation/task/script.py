#!/usr/bin/env python3

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    return str(octet).isdigit() and 0 <= int(octet) <= 255

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
    if not 1 <= len(hextet) <= 4:
        return False
    
    for char in hextet:
        if not (char.isdigit() or char.lower() in 'abcdef'):
            return False
        
    return True

def is_valid_IPv6(ip):
    hextets = ip.split(':')
    if len(hextets) != 8:
        return False
    
    for hextet in hextets:
        if not is_valid_IPv6_hextet(hextet):
            return False
        
    return True

def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address, False otherwise"""
    return is_valid_IPv4(ip) or is_valid_IPv6(ip)

# You should look at task/test.py and extend the test suite we provided!

# print(is_valid_IPv4("127.0.0.1"))
# print(is_valid_IP("2001:0da8:85a3:0:0000:8a2e:0370:7334"))
# print(is_valid_IP("2001:0db8:85a3:0:0000:8a2e:0370:7334:1234"))  # Invalid IPv6
# print(is_valid_IP("2001:0db8:85a3:0:0000:8a2e:0370:7334:gggg"))  # Invalid IPv6