import cv2

# Open the video file
cap = cv2.VideoCapture('C:\\Users\\Windows 10\\Desktop\\project_gouri\\ReverseVideoProject\\video1.mp4')


# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Get the frame size and FPS from the video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (frame_width, frame_height)

# Read the video frames and store them in a list
frame_list = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_list.append(frame)

# Release the video capture object
cap.release()

# Check if frames were read
if not frame_list:
    print("No frames were read from the video file.")
    exit()

# Reverse the frame list
frame_list.reverse()

# Create a video writer object for .mp4 file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, frame_size)

# Write the reversed frames to a new video file
for frame in frame_list:
    out.write(frame)

# Release the video writer object
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Video processing completed successfully.")
