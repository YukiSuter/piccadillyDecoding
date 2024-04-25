import wave

data = open("alarm.pcc", "rb").read()
rawout = open("alarmraw.pcc", "wb")
out = wave.open(open("alarm.wav", "wb"))

out.setnchannels(1)
out.setsampwidth(1)
out.setframerate(4000)

out.writeframes(bytes([
    (data[i]&0x40)<<1 for i in range(1, len(data), 2)
]))


rawout.write(bytes([
    (data[i]&0x40)<<1 for i in range(1, len(data), 2)
]))