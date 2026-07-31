import speech_recognition as sr
from deepmultilingualpunctuation import PunctuationModel

class AudioTranscriber():

    #initialize Recognizer and interval seconds
    def __init__(self):
        #recognizer instance
        self.recognizer = sr.Recognizer()
        self.punct_model = PunctuationModel()

    #restore punctuation to transcribed text
    def restore_punctuation(self, text):
         return self.punct_model.restore_punctuation(text)
    
    #transcribe audio file to text using Google Web Speech, then output to text file
    def transcribe_file(self, f_output="transcript.txt"):
        
        print("Copy full file path: ")
        filepath = input()

        with sr.AudioFile(filepath) as source:
            audio_data = self.recognizer.record(source)

        #send audio to Google speech API for text transcription, restore punctuation
        text = self.recognizer.recognize_google(audio_data)
        text = self.restore_punctuation(text)

        #write output to .txt file
        with open(f_output, "w") as f:
            f.write(text)
        return text

    #transcribe audio captured by microphone
    def transcribe_speech(self, f_output="transcript.txt"):
        #capture audio from microphone
        with sr.Microphone() as source:
            #Reduce ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio_data = self.recognizer.listen(source, timeout=8)
            
        #send audio data to Google speech API
        text = self.recognizer.recognize_google(audio_data)
        text = self.restore_punctuation(text)

        #write output to .txt file
        with open(f_output, "w") as f:
                    f.write(text)
        return text

if __name__ == "__main__":

    tr = AudioTranscriber()
    mode = input("Enter 1 to transcribe a file, 2 to record and transcribe from the microphone: ")

    match mode:
        case "1":
            result = tr.transcribe_file()
            print(result)
        case "2":
            result = tr.transcribe_speech()
            print(result)
        case _:
            print("Invalid input.")
            exit()
