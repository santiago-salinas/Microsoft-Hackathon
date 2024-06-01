import re
import cv2
import simplelpr
import matplotlib.colors as mcolors
from api import findPlateState

video_stream_id = 0
plateRegex = r'[A-Za-z]{3}\s+[\d]{4}'

# Engine setup for simplelpr
setupP = simplelpr.EngineSetupParms()
eng = simplelpr.SimpleLPR(setupP)

proc = eng.createProcessor()
proc.plateRegionDetectionEnabled = True
proc.cropToPlateRegionEnabled = True

# Array to store detected texts
detected_texts = []

def get_color_from_string(color_name):
    # Get the RGB values using matplotlib
    rgb = mcolors.to_rgb(color_name)
    # Convert the RGB values from [0, 1] range to [0, 255] range and to integer
    rgb = tuple(int(c * 255) for c in rgb)
    # OpenCV uses BGR format, so convert the RGB to BGR
    bgr = (rgb[2], rgb[1], rgb[0])
    return bgr

# Function to handle mouse click events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for text, (left, top, width, height) in detected_texts:
            if left < x < left + width and top < y < top + height:
                print(f"Clicked on plate: {text}")

# Function to process each video frame
def process_frame(frame):
    # global detected_texts
    
    # Convert the OpenCV image (BGR) to simplelpr compatible format (RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cds = proc.analyze(rgb_frame)

    # detected_texts = []  # Clear the detected texts array

    # Process detected plates
    for cd in cds:
        for m in cd.matches:
            if re.match(plateRegex, m.text):
                # Get bounding box coordinates
                left = m.boundingBox.left
                top = m.boundingBox.top
                width = m.boundingBox.width
                height = m.boundingBox.height

                normalized_code = m.text.replace(' ', '')

                findResult = findPlateState(normalized_code)
                color = (0, 0, 255)
                if findResult is not None:
                    color = findResult["color"]

                print(color)
                # Overlay a rectangle around the plate
                cv2.rectangle(frame, (left, top), (left + width, top + height), color, 2)

                # Overlay plate text
                cv2.putText(frame, f"Plate: {m.text}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                # Store the detected text and its bounding box
                # detected_texts.append((m.text, (left, top, width, height)))

    # Display the processed frame
    cv2.imshow("Video", frame)
    cv2.waitKey(1)


# Capture video from the notebook camera
cap = cv2.VideoCapture(video_stream_id)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process the video frame
    process_frame(frame)

    # Set mouse callback function
    cv2.setMouseCallback("Video", click_event)

    # Exit the loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
