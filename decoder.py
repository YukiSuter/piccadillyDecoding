import wave

with open("HT23_TRIM.raw", "rb") as f:
    content = f.read().hex()

thehex = content[0x0041b200*2:0x0041b2FF*2]

print(len(thehex))
print(content)
print(bytearray.fromhex(thehex).decode())

out = wave.open(open("HT23_TRIM.wav", "wb"))

out.setnchannels(1)
out.setsampwidth(1)
out.setframerate(4000)

for i in range(1, len(content), 2):
    if content[i-1:i+1] != "24" and content[i-2:i] != "24":
        # print("iffed")
        # print(content[i-1:i+1])
        out.writeframes(bytes([(int("0x"+content[i-1:i+1], 0))&0x40>>1]))
    else:
        out.writeframes(bytes([(0)]))