class Base64encoding:

    def __init__(self , txt=''):
        self._txt = txt
    def __str__(self):
        return self.encode_base64(self._txt)

    # source: https://base64.guru/learn/base64-characters
    BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    # method for encoding a string with base64
    # source to understand how does it work: https://base64.guru/learn/base64-algorithm/encode
    def encode_base64(self, string):
        # start string
        print("start string: ", string)

        # convert string to binary representation
        binary_str = ""
        for char in string:  # iterate over each char at the string
            # ord() representing unicode number
            # print("ord: ",ord(char)) # ord() represents unicode number(ASCII)
            binary_str += f"{ord(char):08b}"  # 08b ensures 8 digits and format "b"inary

        print("binary string: ", binary_str)

        # padding binary string to make it a multiple of 6
        while len(binary_str) % 6 != 0:
            binary_str += '0'

        # split this binary string into 6er parts til end of the string
        base64_chars = [binary_str[i:i + 6] for i in range(0, len(binary_str), 6)]

        print("base64 chars: ", base64_chars)

        # convert each 6-bit part to its base64 character using the table over
        encoded_str = ''.join([self.BASE64_TABLE[int(bits, 2)] for bits in base64_chars])

        # pad encoded string to make it a multiple of 4
        while len(encoded_str) % 4 != 0:
            encoded_str += '='

        return encoded_str


if __name__ == "__main__":
    base = Base64encoding("ABCDEFGHIJ")
    s = str(base)
    print("Encoded string:", s)


