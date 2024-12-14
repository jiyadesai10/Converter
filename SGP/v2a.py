import moviepy.editor

video = moviepy.editor.VideoFileClip('VS2.mp4')

audio = video.audio

audio.write_audiofile('VideoSpeech.wav')