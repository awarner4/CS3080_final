import speech_recognition as sr
from datetime import timedelta

class AudioTranscriber():
    #initialize Recognizer and interval seconds
    def __init__(self, interval_seconds):
        #recognizer instance
        self.recognizer = sr.Recognizer()
        self.interval_seconds = interval_seconds

    #f: generate timestamps from given audio
        

    #f: transcribe audio file to text using Google Web Speech, then output to text file
    def transcribe_file(self, filepath, f_output="transcript.txt"):
        with sr.AudioFile(filepath) as source:
            audio_data = self.recognizer.record(source)
            duration = source.DURATION

        #send audio to Google speech API for text transcription
        text = self.recognizer.recognize_google(audio_data)

        #build timestamped transcript
        
        #write output to .txt file

        return text

    #f: transcribe audio captured by microphone
    def transcribe_speech(self):
        #capture audio from microphone
        with sr.Microphone() as source:
            #Reduce ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio_data = self.recognizer.listen(source)
        #send audio data to Google speech API
        text = self.recognizer.recognize_google(audio_data)

        #build timestamped transcript; no estd duration, so assume 10-second blocks

        #write output to .txt file


        return text

if __name__ == "__main__":
    tr = AudioTranscriber()
    result = tr.transcribe_file("example.wav")
    print(result)