import moviepy.editor as moviepy
clip = moviepy.VideoFileClip("input.avi")
clip.write_videofile("output.mp4")