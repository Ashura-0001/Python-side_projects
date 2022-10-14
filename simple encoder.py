d = ((input("enter your string (only alphanumeric values without floats ):- \n\n")))
print ("")
dic = {    
"A"	:	1000001,
"B"	:	1000010,
"C"	:	1000011,
"D"	:	1000100,
"E"	:	1000101,
"F"	:	1000110,
"G"	:	1000111,
"H"	:	1001000,
"I"	:	1001001,
"J"	:   1001010,
"K"	:   1001011,
"L"	:   1001100,
"M"	:   1001101,
"N"	:   1001110,
"O"	:   1001111,
"P"	:   1010000,
"Q"	:   1010001,
"R"	:   1010010,
"S"	:   1010011,
"T"	:   1010100,
"U"	:   1010101,
"V"	:   1010110,
"W"	:   1010111,
"X"	:   1011000,
"Y"	:   1011001,
"Z"	:   1011010,
"a"	:   1100001,
"b"	:   1100010,
"c"	:   1100011,
"d"	:	1100100,
"e"	:	1100101,
"f"	:	1100110,
"g"	:	1100111,
"h"	:	1101000,
"i"	:	1101001,
"j"	:	1101010,
"k"	:	1101011,
"l"	:	1101100,
"m"	:	1101101,
"n"	:	1101110,
"o"	:	1101111,
"p"	:	1110000,
"q"	:	1110001,
"r"	:	1110010,
"s"	:	1110011,
"t"	:	1110100,
"u"	:	1110101,
"v"	:	1110110,
"w"	:	1110111,
"x"	:	1111000,
"y"	:	1111001,
"z"	:	1111010,
"0" :  "0110000",	 	
"1" :  "0110001",	 	
"2" :  "0110010",	 	
"3" :  "0110011",	 	
"4" :  "0110100",	 	
"5" :  "0110101",	 	
"6" :  "0110110",	 	
"7" :  "0110111",	 	
"8" :  "0111000",	 	
"9" :  "0111001",
"ashura" : "0001"
}
r = d.split(" ") 
a = len(r) 
b = 0 
while (b<a): 
    c = r[b] 
    e = (type(c))
    if (c == "ashura"):
        print (dic.get(c), end=" ")
    elif (e == str):
        f = list(c) 
        g = len(f)
        for i in range (g):
            h = f[i]
            print (dic.get(h), end = " ")
    elif (e == int):
        f = list(str(c)) 
        g = len(f)
        for i in range (g):
            h = f[i]
            print (dic.get(h), end = " ")
    else:
        print ("ERROR AN UNIDENTIFIED VALUE HAS BEEN GIVEN (only string and intergral values are identified)")
    print (end = "abc ") 
    
    b = b+1