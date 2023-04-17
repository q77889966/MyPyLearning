def decrypt(encrypt):
    num_e = ''
    for digit in encrypt:
        num_e += str(int(digit) ^ 4)
    num_e = int(num_e)
    return num_e


num = "12345"
print(f"原始数字：{num}")

encrypt_num = ''
for digit in num:
    encrypt_num += str(int(digit) ^ 4)
print(f"加密后的数字：{encrypt_num}")

decrypted_num = decrypt(encrypt_num)
print(f"解密后的数字：{decrypted_num}")
