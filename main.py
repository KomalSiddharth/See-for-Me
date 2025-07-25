import streamlit as st
import cv2
import pyttsx3
from ultralytics import YOLO
import numpy as np

st.set_page_config(page_title="See For Me", layout="wide")

model = YOLO('yolov8s.pt')
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

st.title("👁️ See For Me: Smart Object Detection Web App")

st.sidebar.header("Controls")
run_camera = st.sidebar.checkbox("Start Camera")
show_boxes = st.sidebar.checkbox("Show Bounding Boxes", value=True)

frame_placeholder = st.empty()
summary_placeholder = st.empty()

if run_camera:
    cap = cv2.VideoCapture(1)
    object_summary = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        labels = results.names

        for box in results.boxes:
            cls_id = int(box.cls)
            label = labels[cls_id]
            object_summary.add(label)

            if show_boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if object_summary:
        summary = f"I see: {', '.join(object_summary)}"
        summary_placeholder.markdown(f"### 📝 Summary: {summary}")
        speak(summary)
    else:
        summary_placeholder.markdown("### No objects detected.")
