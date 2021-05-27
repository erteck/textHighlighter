class Binary:
    
    @classmethod
    def decToBin(cls, dec):
        if(dec == -128):
            return '10000000'
        b = ''
        sign = '0'
        if(dec < 0):
            sign = '1'
        dec = abs(dec)
        for i in range(7):
            b = str(dec % 2) + b
            dec = dec // 2
        b = sign + b
        return b
    
    @classmethod
    def binToDec(cls, bin):
        d = 0
        for i in range(1,8):
            d += int(bin[i]) * (2**(7-i))
        if(bin[0]=='1'):
            d = -d
        return d
    
    def __init__(self, dec):
        self.dec = dec
    
    def __str__(self):
        return self.bin
    
    @property
    def dec(self):
        return self.__dec
    
    @property
    def bin(self):
        return self.__bin
    
    @dec.setter
    def dec(self, dec):
        if(dec < -128):
            dec = -128
        elif(dec > 127):
            dec = 127
        self.__dec = dec
        self.__bin = Binary.decToBin(dec)
    
    @bin.setter
    def bin(self, bin):
        if(len(bin)==8):
            self.__bin = bin
            self.__dec = Binary.binToDec(bin)
    
    def __add__(self, other):
        return Binary(self.dec + other.dec)
    
    def __sub__(self, other):
        return Binary(self.dec - other.dec)
    
    def __and__(self, other):
        r = ''
        for i in range(8):
            if(self.bin[i]=='1' and other.bin[i]=='1'):
                r += '1'
            else:
                r += '0'
        b = Binary(0)
        b.bin = r
        return b

    def __or__(self, other):
        r = ''
        for i in range(8):
            if(self.bin[i]=='1' or other.bin[i]=='1'):
                r += '1'
            else:
                r += '0'
        b = Binary(0)
        b.bin = r
        return b

class BinMat:
    
    def __init__(self, mat):
        self.__mat = mat
    
    def __str__(self):
        r = ''
        for row in self.__mat:
            for element in row:
                r += str(element) + ' '
            r += '\n'
        return r
    
    def __repr__(self):
        return f'Binary Matrix({self.__mat})'
    
    def __add__(self, other):
        r = []
        for i in range(len(self.__mat)):
            rr = []
            for j in range(len(self.__mat[i])):
                rr.append(self.__mat[i][j] + other.__mat[i][j])
            r.append(rr)
        return BinMat(r)
    
    def __sub__(self, other):
        r = []
        for i in range(len(self.__mat)):
            rr = []
            for j in range(len(self.__mat[i])):
                rr.append(self.__mat[i][j] - other.__mat[i][j])
            r.append(rr)
        return BinMat(r)
    
    def __and__(self, other):
        r = []
        for i in range(len(self.__mat)):
            rr = []
            for j in range(len(self.__mat[i])):
                rr.append(self.__mat[i][j] & other.__mat[i][j])
            r.append(rr)
        return BinMat(r)
    
    def __or__(self, other):
        r = []
        for i in range(len(self.__mat)):
            rr = []
            for j in range(len(self.__mat[i])):
                rr.append(self.__mat[i][j] | other.__mat[i][j])
            r.append(rr)
        return BinMat(r)

def main():
    print('Testing Binary')
    
    print('Basics')
    for i in range(-129, 138, 10):
        print(f'{i}: {Binary(i)}')
    
    print('\nSetters & Getters')
    b1 = Binary(10)
    print(f'dec: {b1.dec}, bin: {b1.bin}')
    b1.dec = 100
    print(f'dec: {b1.dec}, bin: {b1.bin}')
    b1.bin = '11100100'
    print(f'dec: {b1.dec}, bin: {b1.bin}')
    
    print('\nOperators')
    b2 = Binary(20)
    print(f'b1 + b2 = {b1 + b2}')
    print(f'b1 - b2 = {b1 - b2}')
    print(f'b1 & b2 = {b1 & b2}')
    print(f'b1 | b2 = {b1 | b2}')
    
    print('\nTesting BinMat')
    m1 = []
    m2 = []
    for i in range(1,4):
        mm1 = []
        mm2 = []
        for j in range(1,4):
            mm1.append(Binary(i*j))
            mm2.append(Binary(i+j*2))
        m1.append(mm1)
        m2.append(mm2)
    mb1 = BinMat(m1)
    mb2 = BinMat(m2)
    print('MB1:')
    print(mb1)
    print('MB2:')
    print(mb2)
    print(f'MB1 + MB2 = \n{mb1 + mb2}')
    print(f'MB1 - MB2 = \n{mb1 - mb2}')
    print(f'MB1 & MB2 = \n{mb1 & mb2}')
    print(f'MB1 | MB2 = \n{mb1 | mb2}')


main()