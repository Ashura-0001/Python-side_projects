inp_str = (input("enter your statement that needs to be decoded:- \n"))
print ("\n")
dic = {
"0110000" : "0",
"0110001" : "1",
"0110010" : "2",
"0110011" : "3",
"0110100" : "4",
"0110101" : "5",
"0110110" : "6",
"0110111" : "7",
"0111000" : "8",
"0111001" : "9",
"1000001" : "A",
"1000010" : "B",
"1000011" : "C",
"1000100" : "D",
"1000101" : "E",
"1000110" : "F",
"1000111" : "G",
"1001000" : "H",
"1001001" : "I",
"1001010" : "J",
"1001011" : "K",
"1001100" : "L",
"1001101" : "M",
"1001110" : "N",
"1001111" : "O",
"1010000" : "P",
"1010001" : "Q",
"1010010" : "R",
"1010011" : "S",
"1010100" : "T",
"1010101" : "U",
"1010110" : "V",
"1010111" : "W",
"1011000" : "X",
"1011001" : "Y",
"1011010" : "Z",
"1100001" : "a",
"1100010" : "b",
"1100011" : "c",
"1100100" : "d",
"1100101" : "e",
"1100110" : "f",
"1100111" : "g",
"1101000" : "h",
"1101001" : "i",
"1101010" : "j",
"1101011" : "k",
"1101100" : "l",
"1101101" : "m",
"1101110" : "n",
"1101111" : "o",
"1110000" : "p",
"1110001" : "q",
"1110010" : "r",
"1110011" : "s",
"1110100" : "t",
"1110101" : "u",
"1110110" : "v",
"1110111" : "w",
"1111000" : "x",
"1111001" : "y",
"1111010" : "z",
"0001" : "ashura",
"abc" : " ", 
}
r = inp_str.split(" abc ")
a = len(r)
b = 0
while (b<a):
    c = r[b]
    d = c.split(" ")
    e = len(d)
    f = 0
    while (f<e):
        g = d[f]
        print (dic.get(g), end="")
        f = f+1
    print (end = " ") 
    b = b+1