finalsplitted = ""

if __name__ == "__main__":
    hexdec= "AEDE0273C4C0DA3477F919018A05DA71A2530F5A0020E4E0ACA80FF2DE"
    hexdec2 = "A8C80426C2DEC16D31F90D1497129475A45447561D74EEF1B8BF0FFCDC"
    hexdec3 = "A9D30426D3C7CB202EB8050E9717C734A5484A13126CE0FDABA212FBDF"
    hexdec4 = "B49B166FDAC58E2A25F90A159914D134B84E0F551677A7FFB6A512FBC1"
    hexdec5 = "B49B126ED7C5C26D20EA07149D40C771B2555D565373E8F4ADBC07E1D7"
    hexdec6 = "B3DE1763C489DC2822EB0B40970ED134A54942565370E6F6F9A003EAC1"


    def XORHEX(str1, str2):
        result = int(str1, 16) ^ int(str2, 16)
        return '{:x}'.format(result)



    print 'ARRAAAAAAAAAAAAAY'
    string = (XORHEX(hexdec, hexdec2))
    print(' BEFORE SPLITTING')

    print string



    def splitfunction (str,x) :
        counter = 0
        z = ""
        for i in range(0,len(str)):
            z = z + str[i]
            counter = counter + 1
            if counter == x :
                z = z + ' '
                counter = 0
        print('Spaced!')
        print z

        final = z.split()
        print('Splitted!')
        print final
        return final

    splitfunction(hexdec,2)
    splitfunction(hexdec2,2)
    splitfunction(hexdec3,2)
    splitfunction(hexdec4,2)
    splitfunction(hexdec5,2)
    splitfunction(hexdec6,2)
    string1 =splitfunction(string,2)
    print 'STRING STRING'
    print string1
    string1bin = bin(int(string,16))
    str1bin = string1bin.replace("b","")
    print len(str1bin)
    print str1bin

    XORXOR = ((XORHEX(str1bin,"00100000")))
    #binary = bin(int(XORXOR,16))
    #binary = binary.replace("0b","")
    print('XORXOR')
    print XORXOR
    binarysp = splitfunction(XORXOR,8)
    print binarysp

    def XOR (str1,str2):
        j = 0
        final = ""
        for i in range(0,len(str1)):
            XOR = int(str1[i],16) ^ int(str2[j],16)
            XORBin = str(XOR)
            final = final + XORBin

            #print ('Merna <3 <3')
            #print XORBin
            j = j + 1

        print final
        global finalsplitted
        finalsplitted = splitfunction(final,2)
        print 'A5eeran'
        print (finalsplitted)
        #print len(finalsplitted)
        #print len(final)
        #finalsplitted = bin(int(finalsplitted))


    XOR(hexdec,hexdec2)
    #XOR(finalsplitted,"20")















