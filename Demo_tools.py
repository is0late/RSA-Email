
# 将十进制ascii还原成字符
# 格式为RetoA('073 068 126')
def RetoA():
    steps = int(input("信息转码输入：1 | 文件转码输入：2 ："))
    if steps == 1:
        m = input("请输入需要转码的ASCII值（格式：001003104084）：")
        i = 0
        c = 0
        buffer = ''
        output = ''
        while i < len(m):
            c = 0
            while c < 3:
                buffer = buffer + m[i+c]
                c += 1
            try:
                output = output + chr(int(buffer))
            except:
                print ('Not valid ASCII number')
                break
            buffer = ''
            i+=3
        print("答案：{}".format(output))
    elif steps == 2:
        fname = input("input filename:")
        if len(fname) == 0:
            fname = "orgchr.txt"
            print("由于您为输入文件名，默认文件名为{}".format(fname))
        rname = input("input resultfile name:")
        if len(rname) == 0:
            rname = "toASCII.txt"
            print("由于您为输入文件名，默认文件名为{}".format(rname))


# 将普通字符转换成Ascii
# 格式为：ContoA('sadasd')
def ContoA():
    steps = int(input("信息转码输入：1 | 文件转码输入：2 ："))
    if steps == 1:
        m = input("请输入需要转码的字符：")
        i = 0
        output = ''
        while i < len(m):
            if len(str(ord(m[i])))<3:
                output = output + str('0' + str(ord(m[i])))
            else:
                output = output + str(str(ord(m[i])))
            i+=1
        print ("答案：{}".format(output))
    if steps == 2:
        fname = input("input filename:")
        if len(fname) == 0:
            fname = "orgchr.txt"
            print("由于您为输入文件名，默认文件名为{}".format(fname))
        rname = input("input resultfile name:")
        if len(rname) == 0:
            rname = "toASCII.txt"
            print("由于您为输入文件名，默认文件名为{}".format(rname))
        with open("{}".format(fname)) as f:
            for m in f.readlines():
                i = 0
                output = ''
                while i < len(m):
                    if len(str(ord(m[i]))) < 3:
                        output = output + str('0' + str(ord(m[i])))
                    else:
                        output = output + str(str(ord(m[i])))
                    i += 1
                with open("{}".format(rname),'at',encoding='utf-8') as fo:
                    fo.write(output + '\n')
        print("转码完成")

# 分解质数 n 获得 p和q
def decom(n):
    n = int(n)
    f = 2
    res = []
    while n!=1:
        if n%f ==0:
            n = n/f
            res.append(f)
        else:
            f+=1
    print(res)
    print("分解质数结果为：{}*{}".format(res[0],res[1]))
    return res



# 获得私钥 D
def getD(p,q,e):
    print("RSA--Get Privite key: D")
    l = (p-1)*(q-1)         # n的欧拉函数φ(n)=l
    i = 0
    while True:
        if (1+l*i) % e == 0:
            break
        i+=1
    print("倍数：{}".format(i))
    print('私钥d='+'%d'% ((1+l*i)/e))
    return (1+l*i)/e

# 通过密钥解密密文
def rsacdn():

    steps = int(input("加密信息请输入：1 | 解密信息请输入：2:"))

    output = ''
    if steps == 1:
        print("加密信息↓")
        n = int(input("input n:"))
        e = int(input("input e:"))
        fom = int(input("信息加密请输入：1 | 文件加密请输入: 2 ："))
        if fom == 1:
            m = input("Please enter unencrypted information：")
            output = str(pow(int(m),e,n))
            print("The result is :" + output)
        if fom == 2:
            fname = input("input filename:")
            if len(fname) == 0:
                fname = "RSAROLL.txt"
                print("由于您为输入文件名，默认文件名为{}".format(fname))
            rname = input("input resultfile name:")
            if len(rname) == 0:
                rname = "res.txt"
                print("由于您为输入文件名，默认文件名为{}".format(rname))
            with open("{}".format(fname)) as f:
                for line in f.readlines():
                    with open("./{}".format(rname),'at',encoding='utf-8') as fo:
                        fo.write(str(pow(int(line), e, n)) + "\n")
                    output = output + str(pow(int(line), e, n)) + "\n"
                    # output = output + chr(pow(int(line), d, n))
            print("The result is :{}".format(output))

    if steps == 2:
        print("解密信息↓")
        get = int(input("私钥解码输入：1 | 公钥解码输入：2 ："))
        if get == 1:
            n = int(input("input n:"))
            d = int(input("input d:"))
        elif get == 2:
            n = int(input("input n:"))
            res = decom(n)
            p,q = res[0],res[1]
            e = int(input("input e:"))
            d = int(getD(p,q,e))
        else:
            return "error input!"

        fom = int(input("信息解密请输入：1 | 文件解密请输入: 2 ："))
        if fom == 1:
            m = input("Please enter decryption information：")
            output = str(pow(int(m), d, n))
            ##output = chr((pow(int(m), d, p * q)))
            print("The result is :" + output)
        if fom == 2:
            fname = input("input filename:")
            if len(fname) == 0:
                fname = "RSAROLL.txt"
                print("由于您为输入文件名，默认文件名为{}".format(fname))
            with open("{}".format(fname)) as f:
                for line in f.readlines():
                    # output = str(pow(int(line),d,p*q))
                    # print(int(line)+'->'+output)
                    output =chr(pow(int(line), d, n))   # 将各个ASCII编码转变成原来符号
                    print(line.strip() + '->' + output)
                    # output = output + chr(pow(int(line), d, n))   # 将各个ASCII编码转变成原来符号
            # print("The result is :" + output)
    return output


if __name__ == '__main__':

    msg1 = '''
     _   _       ____    _____   _____          
    | \ | |     |  _ \  |  __ \ / ____|  /\     
    |  \| |_   _| |_) | | |__) | (___   /  \    
    | . ` | | | |  _ <  |  _  / \___ \ / /\ \   
    | |\  | |_| | |_) | | | \ \ ____) / ____ \  
    |_| \_|\__,_|____/  |_|  \_\_____/_/    \_\
    '''
    msg2='''
    一些小功能！！继续完善
    1.加解密RSA
    2.获得私钥
    3.字符编码成ASCII
    4.ASCII还原成字符
    5.分解质数
    0.退出
    '''
    print(msg1)
    while True:
        print(msg2)
        case = int(input("请输入需要启动的功能（数字）："))
        if case == 1:
            print("进入加解密RSA隧道")
            rsacdn()
        if case == 2:
            print("进入解RSA私钥隧道")
            n = int(input("input n:"))
            res = decom(n)
            p, q = res[0], res[1]
            e = int(input("input e:"))
            getD(p,q,e)
        if case == 3:
            print("进入转码隧道 字符->ASCII")
            ContoA()
        if case == 4:
            print("进入转码隧道 ASCII->字符")
            RetoA()
        if case == 5:
            print("进入质数分解隧道：")
            m = int(input("请输入一个质数："))
            get = decom(m)
        if case == 0:
            print("再见")
            break
    # getD()
    # print(RetoA('104 101 108 108 111 032 119 111 114 108 100'))
    # print(ContoA('flag{13212je2ue28fy71w8u87y31r78eu1e2}='))
    # print(rsacdn())
    # decom(899)