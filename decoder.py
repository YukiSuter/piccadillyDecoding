with open("copy file_truncated.pcc", "rb") as f:
    content = f.read().hex()

thehex = content[0x0041b200*2:0x0041b2FF*2]

print(len(thehex))
print(bytearray.fromhex(thehex).decode())