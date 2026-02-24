import tkinter as tk
import speech_recognition as sr
import threading
import time
import random
import os

class BMORobot:
    def __init__(self, root):
        self.root = root
        self.root.title("BMO Face")
        # Fullscreen mode for the Ubuntu display
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='#77cfb7')
        
        # Emergency exit: Press Escape to close BMO
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        self.canvas = tk.Canvas(root, width=800, height=480, bg='#77cfb7', highlightthickness=0)
        self.canvas.pack(expand=True)

        # Draw eyes as flat lines (Sleeping state)
        self.left_eye = self.canvas.create_rectangle(250, 240, 350, 245, fill="black")
        self.right_eye = self.canvas.create_rectangle(450, 240, 550, 245, fill="black")
        
        self.is_awake = False
        self.start_blinking()

    def play_sound(self):
        """Finds hey.wav in the project folder and plays it via native Ubuntu aplay."""
        # Forces BMO to look in the folder where the script is saved
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, "hey.wav")
        
        if os.path.exists(filename):
            print(f"DEBUG: Found file! Playing from: {filename}")
            # '&' allows sound to play without stopping the eye animation
            os.system(f"aplay '{filename}' &") 
        else:
            print(f"DEBUG ERROR: hey.wav NOT FOUND at {filename}")

    def animate_open(self):
        """Eyes expand vertically while sound plays."""
        self.is_awake = True
        self.play_sound() 
        for i in range(0, 70, 5):
            self.canvas.coords(self.left_eye, 250, 240-i, 350, 245+i)
            self.canvas.coords(self.right_eye, 450, 240-i, 550, 245+i)
            self.root.update()
            time.sleep(0.02)

    def animate_close(self):
        """Eyes shrink back to lines."""
        for i in range(70, 0, -5):
            self.canvas.coords(self.left_eye, 250, 240-i, 350, 245+i)
            self.canvas.coords(self.right_eye, 450, 240-i, 550, 245+i)
            self.root.update()
            time.sleep(0.02)
        self.is_awake = False

    def start_blinking(self):
        """Randomly blinks the eyes to look alive while waiting."""
        if not self.is_awake:
            self.canvas.coords(self.left_eye, 250, 240-2, 350, 245+2)
            self.canvas.coords(self.right_eye, 450, 240-2, 550, 245+2)
            self.root.after(100, lambda: self.canvas.coords(self.left_eye, 250, 240, 350, 245))
            self.root.after(100, lambda: self.canvas.coords(self.right_eye, 450, 240, 550, 245))
        self.root.after(random.randint(3000, 7000), self.start_blinking)

def voice_listener(robot):
    r = sr.Recognizer()
    # Sensitivity adjusted for the DIU dorm room environment
    r.energy_threshold = 250 
    r.dynamic_energy_threshold = False 
    
    with sr.Microphone() as source:
        print("--- READY! Say 'Hey BMO' ---")
        while True:
            try:
                # Listen for voice input
                audio = r.listen(source, timeout=None, phrase_time_limit=3)
                # Use Google Speech API (requires internet)
                text = r.recognize_google(audio).lower()
                print(f"BMO heard: {text}")
                
                # Multi-syllable wake word is more reliable
                if "bmo" in text:
                    print("Wake word detected!")
                    robot.animate_open()
                    time.sleep(4)
                    robot.animate_close()
            except:
                pass

if __name__ == "__main__":
    root = tk.Tk()
    bmo = BMORobot(root)
    # Threading prevents the GUI from freezing while listening
    threading.Thread(target=voice_listener, args=(bmo,), daemon=True).start()
    root.mainloop()