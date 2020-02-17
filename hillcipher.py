"""hill cipher encryption and decryption"""
import sys
import numpy as np


def encryption():
    """encryption"""
    msg = input("enter single message:").upper()
    msg = msg.replace(" ", " ")
    space = [ ]
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)
    itr_1 = 0
    itr_2 = 0
    for i in range(len(msg)) or i in space:
        if i % 2 == 0:
            msg2d[0][itr_1] = int(ord(msg[i])-65)
            itr_1 += 1
        else:
            msg2d[1][itr_2] = int(ord(msg[i])-65)
            itr_2 += 1
    key = input("enter 4 LETTER  key:").upper()
    key = key.replace(" ", " ")
    key2d = np.zeros((2, 2), dtype=int)
    itr_3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr_3])-65
            itr_3 += 1
            deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
            deter = deter % 26
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    if mul_inv == -1:
        print("invalid key")
        sys.exit()

    encryp_text = ""
    i_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(i_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i]*key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
    else:
    	for i in range(i_count-1):
    		temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i]*key2d[0][1]
    		encryp_text += chr((temp1 % 26)+65)
    		temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
    		encryp_text += chr((temp2 % 26)+65)
    print("encrypted_text is:{}".format(encryp_text))


def cipher_decryption():
    """decryption"""
    msg = input("enter encrypted message:").upper()
    msg = msg.replace(" ", " ")
    space = []
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)
    itr_1 = 0
    itr_2 = 0
    for i in range(len(msg)) or i in space:
        if i % 2 == 0:
            msg2d[0][itr_1] = int(ord(msg[i])-65)
            itr_1 += 1
        else:
            msg2d[1][itr_2] = int(ord(msg[i])-65)
            itr_2 += 1
    key = input("enter 4 LETTER key:").upper()
    key = key.replace(" ", " ")
    key2d = np.zeros((2, 2), dtype=int)
    itr_3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr_3])-65
            itr_3 += 1
            deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
            deter = deter % 26
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
        	continue
        if mul_inv == -1:
        	print("invalid key")
        	sys.exit()
    """adjugate matrix/ swapping"""
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]
    """changing sign"""
    key2d[0][1] *= -1
    key2d[1][0] *= -1
    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26
    """multiplying multiplicative inverse with adjugate matrix"""
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv
            """modulo"""
        for i in range(2):
            for j in range(2):
                key2d[i][j] = key2d[i][j] % 26
    decryp_text = ""
    i_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(i_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i]*key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
    else:
    	for i in range(i_count-1):
    		temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i]*key2d[0][1]
    		decryp_text += chr((temp1 % 26)+65)
    		temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
    		decryp_text += chr((temp2 % 26)+65)
    print("\ndecrypted_text is:{}".format(decryp_text))


def main():
    """main function"""
    choice = int(input("1.encryption\n2.decrypt\nCHOOSE[1/2]: "))
    if choice == 1:
        print("-------------------encryption------------------------")
        encryption()
    elif choice == 2:
        print("---------------------decryption-----------------------")
        cipher_decryption()
    else:
        print("invalid choice").upper()
        sys.exit()


if __name__ == "__main__":
    main()