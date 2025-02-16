import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Spotify API (replace with your credentials)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="c7c05e9a2e914d00b4b10e31e8f1508f",
                                               client_secret="fb367f79662d451b971ce1ee7fda1535",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-modify-playback-state,user-read-playback-state"))

def recognize_speech():
    """Recognizes speech and returns the detected command as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # Debugging output
        try:
            audio = recognizer.listen(source)
            print("Processing audio...")  # Debugging output
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")  # Debugging output
            return command
        except sr.UnknownValueError:
            return "Could not understand."
        except sr.RequestError:
            return "API Error."

def control_spotify(command):
    """Processes the command and controls Spotify accordingly."""
    if "play" in command:
        sp.start_playback()
        return "Playing music."
    elif "pause" in command:
        sp.pause_playback()
        return "Paused music."
    elif "next" in command:
        sp.next_track()
        return "Skipping track."
    elif "previous" in command:
        sp.previous_track()
        return "Going back to previous track."
    else:
        return "Command not recognized."