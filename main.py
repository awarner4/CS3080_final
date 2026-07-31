import speech_recognition as sr

class AudioTranscriber():

    #initialize Recognizer and interval seconds
    def __init__(self, interval_seconds=10):
        #recognizer instance
        self.recognizer = sr.Recognizer()

    #f: transcribe audio file to text using Google Web Speech, then output to text file
    def transcribe_file(self, filepath, f_output="transcript.txt"):
        with sr.AudioFile(filepath) as source:
            audio_data = self.recognizer.record(source)

        #send audio to Google speech API for text transcription
        text = self.recognizer.recognize_google(audio_data)

        #write output to .txt file
        with open(f_output, "w") as f:
            f.write(text)

        return text

    #f: transcribe audio captured by microphone
    def transcribe_speech(self, f_output="transcript.txt"):
        #capture audio from microphone
        with sr.Microphone() as source:
            #Reduce ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Listening...")
            audio_data = self.recognizer.listen(source, timeout=5)
            
        #send audio data to Google speech API
        text = self.recognizer.recognize_google(audio_data)

        #write output to .txt file
        with open(f_output, "w") as f:
                    f.write(text)
        return text

if __name__ == "__main__":
    tr = AudioTranscriber()
    mode = input("Press 1 to transcribe an audio file, 2 to record and transcribe audio: ")
    match mode:
        case "1":
            input_file = input("Please copy the complete filepath of a .WAV file to transcribe: ")
            result = tr.transcribe_file(input_file)
            print(result)
        case "2":
            result = tr.transcribe_speech()
            print(result)
    
