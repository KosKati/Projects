from moviepy import VideoFileClip, CompositeVideoClip, concatenate_videoclips

# loading video gfg

timestamps = [23, 29, 50, 69, 78, 119, 145, 165, 345, 596]
clips = []

for timestamp in timestamps:
    clips.append(VideoFileClip("Bad_Soden.mp4").subclipped(timestamp - 5,timestamp + 5))



resultSoden = concatenate_videoclips(clips)

resultSoden.write_videofile("./resultSoden.mp4")


