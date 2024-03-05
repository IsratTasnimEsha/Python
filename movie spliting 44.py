import cv
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

capture = cv.CaptureFromFile('F:\1.2\MATH 1207\MATH 1207 HABIB SIR\Recordings\Lec 13-14 d7ef520f-7df2-4be9-9eb5-ff8a29919519.mp4')
while Condition1:
    # Need a frame to get the output video dimensions
    frame = cv.RetrieveFrame(capture) # Will return None if there are no frames
    # New video file
    video_out = cv.CreateVideoWriter(output_filenameX, CV_FOURCC('M','J','P','G'), capture.fps, frame.size(), 1)
    # Write the frames
    cv.WriteFrame(video_out, frame)
    while Condition2:
        frame = cv.RetrieveFrame(capture) # Will return None if there are no frames
        cv.WriteFrame(video_out, frame)