def ip_to_num(ip):
    convert_to_integer = [int(i) for i in ip.split('.')]
    int_to_binary = "".join([bin(i).replace("0b", "").zfill(8) for i in convert_to_integer])
    return int(int_to_binary, base=2)


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
