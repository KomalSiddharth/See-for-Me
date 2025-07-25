# See-for-Me 🧠👁️

A smart vision-based assistant for visually impaired users that uses real-time object detection, voice descriptions, and audio alerts for nearby dangers.

## 📌 Overview

**See-for-Me** uses a YOLOv8 object detection model to identify and describe objects around you in real-time. If any object is detected too close (within 3 feet), the system raises a warning with an alarm sound. It provides direction and distance feedback using voice output so that the user can navigate more safely.

## 🎯 Features

- 🧠 Real-time object detection using YOLOv8
- 🗣️ Voice-based descriptions using pyttsx3
- 🌐 Language translation support (via Google Translate)
- 🚨 Audio alarm for dangerous proximity
- 🎯 Directional feedback like "on your left", "in front of you", etc.
- 🖼️ Live camera feed with bounding boxes and labels

## 🛠️ Technologies Used

- Python
- OpenCV
- YOLOv8 (`ultralytics`)
- pyttsx3 (for TTS)
- playsound
- googletrans
<img width="1920" height="1080" alt="Screenshot (665)" src="https://github.com/user-attachments/assets/094df8d9-6ff1-432c-83e1-24ca69d1553a" />
