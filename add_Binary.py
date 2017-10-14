class solution(object):
    def add_Binary(self,a,b):
        print(eval('0b' + a) + eval('0b' + b))
        # return bin(eval('0b' + a) + eval('0b' + b))[2:]
        # z = 0b100
        # print(z)

if __name__ == '__main__':
    sol = solution()
    sol.add_Binary('11','1')
    sol.add_Binary('101','1001')