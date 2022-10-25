# GuitarTuner

# Versions
* Python  2.7.16
* matplotlib         3.5.1
* numpy              1.22.3
* pydub              0.25.1
* python-Levenshtein 0.12.0
* sounddevice        0.4.4
* scipy              1.8.0



# Dependencies
## NoteDedect

* Usb sound card need alsa configuration.
```
sudo nano /etc/asound.conf

pcm.!default  {
 type hw card 1
}
ctl.!default {
 type hw card 1
}
```
* pip install numpy
* pip install scipy
* pip install --upgrade numpy 
* pip install sounddevice
* sudo apt-get install python-dev libatlas-base-dev
* sudo apt-get install libportaudio2

Run command
```
python3 noteDedect_12String.py
```

## voiceRecorder
* pip3 install sounddevice
* pip3 install wavio
* pip3 install scipy
 
## wavToText
* pip install numpy
* pip install scipy
* sudo apt-get install python3-scipy
* pip install matplotlib
* pip install python-Levenshtein==0.12.0

# Reference
* Reference 1: https://github.com/not-chciken/guitar_tuner
* Reference 2: https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/
* Reference 3: https://guitargearfinder.com/guides/how-to-tune-a-12-string-guitar/
* Reference 4: https://github.com/ianvonseggern1/note-prediction
* Reference 5: https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config
* Reference 6: https://pypi.org/project/noisereduce/
