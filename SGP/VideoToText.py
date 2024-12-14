import imp
import subprocess
from click import command
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

command = 'ffmpeg -i VS2.mp4 -ab 160k -ar 44100 -vn audioFile.wav'
subprocess.call(command, shell=True)