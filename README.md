# BMO-Wakeup-

To create a professional GitHub README for your BMO project, we will use Markdown to structure the information and include the path to your BMO image. Since you are a student at Daffodil International University, this is a great addition to your portfolio.

Here is a template you can copy and paste into a file named README.md in your project folder.

BMO Interactive Robot 🤖
BMO is a Python-based interactive robot project designed to run on Ubuntu Linux. It features a voice-activated interface that triggers eye animations and sound responses.

📸 Face Preview
When BMO hears the wake word "Hey BMO", its eyes transition from a sleeping state to an open, alert state.

(Note: Ensure you have an image named bmo_face.png in your repository for this to display.)

✨ Features
Voice Recognition: Uses the SpeechRecognition library with Google Speech API to detect "Hey BMO".

Dynamic GUI: A Tkinter-based fullscreen interface representing BMO’s face.

Random Blinking: BMO blinks at random intervals to appear more "alive" while waiting for commands.

Audio Response: Plays a greeting sound (hey.wav) using native Ubuntu aplay to avoid driver conflicts.

Linux Optimized: Specifically configured to bypass common ALSA and Jack server audio issues on Ubuntu.

🛠️ Requirements
Operating System: Ubuntu (tested on 22.04+).

Environment: Python 3.12 within a virtual environment (bmo_env).

System Libraries:

python3-tk

portaudio19-dev

libsdl2-mixer-2.0-0

alsa-utils (for aplay)

🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/bmo-robot.git
cd bmo-robot
Set up the Virtual Environment:

Bash
python3 -m venv bmo_env
source bmo_env/bin/activate
pip install SpeechRecognition PyAudio
Configure Audio Permissions:
To allow the script to access your hardware, add your user to the audio group and restart your session:

Bash
sudo usermod -a -G audio $USER
Run BMO:

Bash
python3 test_bmo.py
⌨️ Controls
Wake Word: "Hey BMO".

Exit: Press Esc to close the fullscreen interface.
