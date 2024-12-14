# import required libraries
from pydub import AudioSegment 
from pydub.playback import play
import os
  
# importing audio file
a = AudioSegment.from_file("VideoSpeech.wav") 
  
# Split stereo to mono 
mono_audios = a.split_to_mono()
  
  
[0].export(out_f="outNow.wav",format="wav")
os.system("start outNow.wav")