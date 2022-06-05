""" original IP address
192.168.1.1

breaks down into 4 binary octets
11000000 . 10101000 . 00000001 . 00000001

which are merged together (unsigned 32-bit binary)
11000000101010000000000100000001

and finally converted to base 10
3232235777

original base 10
3232235777

converted to base 2

add ! every 8th index


https://www.codewars.com/kata/541a354c39c5efa5fa001372"""


"""def ip_to_num(ip):
    binary = "".join([bin(int(i)).replace("0b", "".zfill(8)) for i in ip.split('.')])
    return print(int(binary, base =2))"""
def ip_to_num(ip):
    print("1",ip)
    test = ip.split('.')
    print("2",test)
    convert_to_integer = [int(i) for i in test]
    print("3",convert_to_integer)
    int_to_binary = [bin(i).replace("0b", "") for i in convert_to_integer]
    zero = "0"
    for octet in (int_to_binary):
        print("why do i work",octet)
        if len(octet) <= 7:
            place = int_to_binary.index(octet)
            diff = 8 - len(octet)
            new_octet = ("0" * diff) + octet
            int_to_binary[place] = new_octet
            print(new_octet)
    num = "".join(int_to_binary)
    print(num)
    x = int(num,base = 2)
    print(x)


def num_to_ip(num):
    binary, lst, bin_string = bin(num).replace("0b", "").zfill(32), [], ""
    for i in range(len(binary)):
        bin_string += binary[i]
        if (i % 8) == 7:
            bin_string += '!'
    ip = " ".join(bin_string.split('!')).rstrip().split(" ")
    for i in range(4):
        lst.append(int(ip[i], base=2))
    return ".".join([str(i) for i in lst])




#ip_to_num('192.168.1.1')
num_to_ip(167772160)
print("num_to_ip should equal 10.0.0.0")