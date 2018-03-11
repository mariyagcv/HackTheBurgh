import pyaudio
import numpy as np

p = pyaudio.PyAudio()

# while True:
volume = 2.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 2.5   # in seconds, may be float
f = 698.46        # sine frequency, Hz, may be float

a = 587.33
b = 523.33
c = 466.16
d = 440.0

pause = 0
pauseDur = 0.5
pauseDur2 = 0.2
pauseDurLong = 2.0
duration2 = 1.0
duration3 = 1.8
duration4 = 1.2
duration5 = 3.2
duration6 = 0.8

# generate samples, note conversion to float32 array
# samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

while True:
# play. May repeat with different volume values (if done interactively)

#note1
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur2)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note2
    samples = (np.sin(2*np.pi*np.arange(fs*duration2)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur2)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note3
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*f/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)
#note4
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note5
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*b/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note6
    samples = (np.sin(2*np.pi*np.arange(fs*duration5)*c/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note7
    samples = (np.sin(2*np.pi*np.arange(fs*duration5)*d/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)



#SECOND PART HEHHEE


#note1
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur2)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note2
    samples = (np.sin(2*np.pi*np.arange(fs*duration2)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur2)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note3
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*f/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)
#note4
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*a/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note5
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*b/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note6
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*c/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)
#note7
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*b/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note 8
    samples = (np.sin(2*np.pi*np.arange(fs*duration6)*c/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

#note7
    samples = (np.sin(2*np.pi*np.arange(fs*duration5)*d/fs)).astype(np.float32)
    stream.write(volume*samples)

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDurLong)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)


#long pause

    samples = (np.sin(2*np.pi*np.arange(fs*pauseDur)*pause/fs)).astype(np.float32)
    stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()
