import wave

data = open("HT23.raw", "rb").read()
out = wave.open(open("HT23.wav", "wb"))

out.setnchannels(1)
out.setsampwidth(1)
out.setframerate(4000)

out.writeframes(bytes([
    (data[i]&0x40)<<1 for i in range(1, len(data), 2)
]))