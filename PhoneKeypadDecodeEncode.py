def decode(text, seperator, space):
    list_item = list(text.upper().split(seperator))
    decoded_text = ""

    for group in list_item:
        if group == "2":
            decoded_text += "A"
        elif group == "22":
            decoded_text += "B"
        elif group == "222":
            decoded_text += "C"
        elif group == "3":
            decoded_text += "D"
        elif group == "33":
            decoded_text += "E"
        elif group == "333":
            decoded_text += "F"
        elif group == "4":
            decoded_text += "G"
        elif group == "44":
            decoded_text += "H"
        elif group == "444":
            decoded_text += "I"
        elif group == "5":
            decoded_text += "J"
        elif group == "55":
            decoded_text += "K"
        elif group == "555":
            decoded_text += "L"
        elif group == "6":
            decoded_text += "M"
        elif group == "66":
            decoded_text += "N"
        elif group == "666":
            decoded_text += "O"
        elif group == "7":
            decoded_text += "P"
        elif group == "77":
            decoded_text += "Q"
        elif group == "777":
            decoded_text += "R"
        elif group == "7777":
            decoded_text += "S"
        elif group == "8":
            decoded_text += "T"
        elif group == "88":
            decoded_text += "U"
        elif group == "888":
            decoded_text += "V"
        elif group == "9":
            decoded_text += "W"
        elif group == "99":
            decoded_text += "X"
        elif group == "999":
            decoded_text += "Y"
        elif group == "9999":
            decoded_text += "Z"
        elif group == space:
            decoded_text += " "

    return decoded_text

def encode(text, seperator, space):
    list_of_text = list(text.upper())
    encoded_text = ""

    for char in list_of_text:
        if char == "A":
            encoded_text += "2" + seperator
        elif char == "B":
            encoded_text += "22" + seperator
        elif char == "C":
            encoded_text += "222" + seperator
        elif char == "D":
            encoded_text += "3" + seperator
        elif char == "E":
            encoded_text += "33" + seperator
        elif char == "F":
            encoded_text += "333" + seperator
        elif char == "G":
            encoded_text += "4" + seperator
        elif char == "H":
            encoded_text += "44" + seperator
        elif char == "I":
            encoded_text += "444" + seperator
        elif char == "J":
            encoded_text += "5" + seperator
        elif char == "K":
            encoded_text += "55" + seperator
        elif char == "L":
            encoded_text += "555" + seperator
        elif char == "M":
            encoded_text += "6" + seperator
        elif char == "N":
            encoded_text += "66" + seperator
        elif char == "O":
            encoded_text += "666" + seperator
        elif char == "P":
            encoded_text += "7" + seperator
        elif char == "Q":
            encoded_text += "77" + seperator
        elif char == "R":
            encoded_text += "777" + seperator
        elif char == "S":
            encoded_text += "7777" + seperator
        elif char == "T":
            encoded_text += "8" + seperator
        elif char == "U":
            encoded_text += "88" + seperator
        elif char == "V":
            encoded_text += "888" + seperator
        elif char == "W":
            encoded_text += "9" + seperator
        elif char == "X":
            encoded_text += "99" + seperator
        elif char == "Y":
            encoded_text += "999" + seperator
        elif char == "Z":
            encoded_text += "9999" + seperator
        elif char == " ":
            encoded_text += space + seperator
        else:
            encoded_text += char

    return encoded_text


# Example use for encode
text_code = "THIS LITTLE SCRIPT MIGHT COME IN HANDY AT CTF"
encoded_text = encode(text_code, "&", "?")
print(encoded_text)

#Example use for decode
text_decode = "8/44/444/7777/+/555/444/8/8/555/33/+/7777/222/777/444/7/8/+/6/444/4/44/8/+/222/666/6/33/+/444/66/+/44/2/66/3/999/+/2/8/+/222/8/333/"
decoded_text = decode(text_decode, "/", "+")
print(decoded_text)

