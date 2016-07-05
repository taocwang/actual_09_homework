def ip_check(ip):
    q = ip.split('.')
    return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, \
        map(int, filter(lambda x: x.isdigit(), q)))) == 4

if __name__ == '__main__':
   print ip_check('256.123.123.123')