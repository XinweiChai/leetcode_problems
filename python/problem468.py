class Solution:
    def validIPAddress(self, IP: str) -> str:
        def ipv4(s):
            s = s.split('.')
            if len(s) != 4:
                return False
            for i in s:
                if not i.isdigit() or (i != '0' and i[0] == '0') or int(i) > 255:
                    return False
            return True

        def ipv6(s):
            s = s.split(':')
            if len(s) != 8:
                return False
            for i in s:
                if len(i) == 0 or len(i) > 4:
                    return False
                for j in i:
                    if (j.isupper() and j > 'F') or (j.islower() and j > 'f'):
                        return False
            return True

        if '.' in IP:
            if ipv4(IP):
                return "IPv4"
            return 'Neither'
        elif ':' in IP:
            if ipv6(IP):
                return 'IPv6'
            return 'Neither'
        return 'Neither'


if __name__ == '__main__':
    print(Solution().validIPAddress("256.256.256.256"))
    # print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
