# BMO-Wakeup-
<p align="center">
  <img src="bmo_face.png" alt="BMO Face" width="400">
</p>

<h1 align="center">🤖 BMO: The Interactive Robot</h1>

<p align="center">
  <img src="https://img.shields.io/badge/OS-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu Badge">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Wake_Word-BMO-77cfb7?style=for-the-badge" alt="BMO Badge">
</p>

---

### 📝 Overview
BMO is an interactive, voice-activated robot project developed on **Ubuntu Linux**. Designed with a focus on human-robot interaction, BMO uses real-time speech recognition to trigger facial animations and native audio feedback.

[Image of a flowchart showing voice input being captured, processed by SpeechRecognition, and triggering a UI change in Tkinter]

### ✨ Key Features
* **Voice Trigger**: Responds to "Hey BMO" using Google Speech Recognition API.
* **Alive Mode**: Random blinking patterns ensure BMO looks conscious while idling.
* **Ubuntu Optimized**: Uses native `aplay` to bypass common Linux audio driver conflicts.
* **Fluid Animation**: Vertically expanding eyes built with Python's Tkinter.

---

### 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **GUI** | Tkinter |
| **Audio Playback** | ALSA / `aplay` |
| **Speech Engine** | `SpeechRecognition` |

---

### 🚀 Getting Started

1. **Prerequisites**:
   Ensure you have installed the necessary system dependencies on your Ubuntu machine:
   ```bash
   sudo apt-get install python3-tk portaudio19-dev alsa-utils
