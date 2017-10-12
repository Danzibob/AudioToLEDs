FFMPEG_BIN = "ffmpeg" # on Linux
import subprocess as sp
import struct

cmd = "ffmpeg -i https://ury.org.uk/audio/jukebox -f s16le -acodec pcm_s16le -ar 44100 -ac 2 -listen 1 -loglevel quiet 2>/dev/null -"
p = sp.Popen(cmd,
			 shell=True,
			 bufsize=64,
			 stdin=sp.PIPE,
			 stderr=sp.PIPE,
			 stdout=sp.PIPE)
mainList = []
while 1:
	try:
		data = p.stdout.readline()
		if len(data) != 0:
			L = []
			data_len = len(data)
			for i in range(0,data_len,2):
				if(data[i:i+2] not in [b'\n',b'\r']):
					#print(data[i:i+2])
					L.append(int((struct.unpack('<h', data[i:i+2]))[0]))
			mainList.extend(L)
			if len(mainList) > 44100:
				mainList = mainList[44100:]
		

	except KeyboardInterrupt:
		p.kill()
		break
	finally:
		p.kill()


