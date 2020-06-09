import pyttsx3
import speech_recognition

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you"
    elif "hello" in you:
        robot_brain = "hello Phong"
    elif "bye" in you:
        robot_brain = "bye phong"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break


    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    
