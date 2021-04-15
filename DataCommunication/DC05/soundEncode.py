import numpy as np
import pyaudio ### delete when submitting to githumb classroom
from reedsolo import RSCodec

HANDSHAKE_START_HZ = 8192 # select start hz
HANDSHAKE_END_HZ = 8704 # select start hz (higher than start hz)

START_HZ = 1024
STEP_HZ = 256
BITS = 4

FEC_BYTES = 4

### def sound_generate(freq): ## github classroom
def sound_generate(stream, freq):
    sampling_rate=44100
    
    t = np.linspace(0, 1, int(sampling_rate))
    sample = np.sin(2 * np.pi * freq * t).astype(np.float32)
        
    stream.write(sample)
	
	
def divide_by_tone(each_data):
    l = hex(each_data)
    l = l[2:]
    ret = list()
    if len(l) == 1:
            ret.append(bin(int('0', 16)))
            ret.append(bin(int(l[0], 16)))
    else:
        for i in range(len(l)):
            ret.append(bin(int(l[i], 16)))
    return ret
    

def to_freq(start_flag, step, end_flag):
    if start_flag == False:
        return HANDSHAKE_START_HZ
    if end_flag == True:
        return HANDSHAKE_END_HZ
    return START_HZ + step * STEP_HZ
    

def sound_code(fec_payload):
    ### delete when submitting to githumb classroom ###
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output = True)
    ###################################################

    start_flag = True
    end_flag = False
    sound_generate(stream, HANDSHAKE_START_HZ)
    
    for i in fec_payload:
        t = divide_by_tone(i)
        for j in t:
            s = to_freq(start_flag,int(j,2),end_flag)
            print(s)
            sound_generate(stream, s)
    
    sound_generate(stream, HANDSHAKE_END_HZ)


def play_sound(msg):
    byte_array = msg
    #rs = RSCodec(FEC_BYTES)
    #fec_payload = bytearray(rs.encode(byte_array))
    fec_payload = bytearray(byte_array.encode())
    
    sound_code(fec_payload)

if __name__ == '__main__':
    input_msg = input()

    play_sound(input_msg)
