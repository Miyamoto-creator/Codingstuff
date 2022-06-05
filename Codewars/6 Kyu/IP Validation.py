import ipaddress

def is_valid_IP(string):
    try:
        ipaddress.ip_address(string)
    except:
        return False
    return True

print(is_valid_IP('1.255.56.1'))