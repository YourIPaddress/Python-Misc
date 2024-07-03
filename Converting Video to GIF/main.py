from moviepy.editor import VideoFileClip

clip = VideoFileClip("Converting Video to GIF\\video.mp4")
clip.write_gif("Converting Video to GIF\\mygif.gif", fps=5)
