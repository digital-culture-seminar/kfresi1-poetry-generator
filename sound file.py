
#!/usr/bin/env python

# -*- coding: utf-8 -*-



"""

SCRIPT:  text-to-audio.py

AUTHOR:  Brendan Harmon <brendan.harmon@gmail.com>

PURPOSE: Open educational materials for a seminar on digital culture

LICENSE: GNU General Public License v2

DEPENDENCIES: playsound and gTTs

"""



## import libraries
#
#from playsound import playsound
#
#from gtts import gTTS
#
#
#
## text to speech
#
#tts = gTTS(text="Hello world", lang="en")
#
#
#
## write audio file
#
#tts.save("hello-world.mp3")
#
#
#
## play audio file
#
#playsound("hello-world.mp3")




# import libraries

from playsound import playsound

from gtts import gTTS

import markovify

# get raw text as string
with open ("poe.txt") as textfile: 
    poe = textfile.read()

with open ("the raven.txt") as textfile: 
    raven = textfile.read()
    
#print raven

raven_model = markovify.Text(raven)  
poe_model = markovify.Text(poe) 

synthesized_model = markovify.combine([raven_model, poe_model], [1,1])

markov_poem = synthesized_model.make_sentence()




# text to speech

tts = gTTS(text=markov_poem, lang='en')



# write audio file

tts.save("markovified-poem.mp3")



# play audio file

playsound("markovified-poem.mp3")



!/usr/bin/env python

 -*- coding: utf-8 -*-



#"""
#
#AUTHOR: Matthias Geier
#
#PURPOSE: Create a recording with arbitrary duration
#
#LICENSE: MIT
#
#SOURCE: https://python-sounddevice.readthedocs.io/en/0.3.12/examples.html
#
#DEPENDENCIES: sounddevice and PySoundFile
#
#"""
#
#
#
#import argparse
#
#import tempfile
#
#import queue
#
#import sys
#
#
#
#def int_or_str(text):
#
#    """Helper function for argument parsing."""
#
#    try:
#
#        return int(text)
#
#    except ValueError:
#
#        return text
#
#
#
#parser = argparse.ArgumentParser(description=__doc__)
#
#parser.add_argument(
#
#    '-l', '--list-devices', action='store_true',
#
#    help='show list of audio devices and exit')
#
#parser.add_argument(
#
#    '-d', '--device', type=int_or_str,
#
#    help='input device (numeric ID or substring)')
#
#parser.add_argument(
#
#    '-r', '--samplerate', type=int, help='sampling rate')
#
#parser.add_argument(
#
#    '-c', '--channels', type=int, default=1, help='number of input channels')
#
#parser.add_argument(
#
#    'filename', nargs='?', metavar='FILENAME',
#
#    help='audio file to store recording to')
#
#parser.add_argument(
#
#    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
#
#args = parser.parse_args()
#
#
#
#try:
#
#    import sounddevice as sd
#
#    import soundfile as sf
#
#    import numpy  # Make sure NumPy is loaded before it is used in the callback
#
#    assert numpy  # avoid "imported but unused" message (W0611)
#
#
#
#    if args.list_devices:
#
#        print(sd.query_devices())
#
#        parser.exit(0)
#
#    if args.samplerate is None:
#
#        device_info = sd.query_devices(args.device, 'input')
#
#        # soundfile expects an int, sounddevice provides a float:
#
#        args.samplerate = int(device_info['default_samplerate'])
#
#    if args.filename is None:
#
#        args.filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
#
#                                        suffix='.wav', dir='')
#
#    q = queue.Queue()
#
#
#
#    def callback(indata, frames, time, status):
#
#        """This is called (from a separate thread) for each audio block."""
#
#        if status:
#
#            print status
#
#        q.put(indata.copy())
#
#
#
#    # Make sure the file is opened before recording anything:
#
#    with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
#
#                      channels=args.channels, subtype=args.subtype) as file:
#
#        with sd.InputStream(samplerate=args.samplerate, device=args.device,
#
#                            channels=args.channels, callback=callback):
#
#            print'#' * 80
#
#            print'press Ctrl+C to stop the recording'
#
#            print'#' * 80
#
#            while True:
#
#                file.write(q.get())
#
#
#
#except KeyboardInterrupt:
#
#    print '\nRecording finished: '
#
#    parser.exit(0)
#
#except Exception as e:
#
#    parser.exit(type(e).__name__ + ': ' + str(e))

