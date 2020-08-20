import os
import pyttsx3
import string

print("Hello buddy!")
pyttsx3.speak("Hello buddy!")
pyttsx3.speak("Let me introduce myself")
print("I am a OS based Assistant to help you ease you task")
pyttsx3.speak("I am a OS based Assistant to help you ease you task")
print("\nTell me your name: ",end="")
pyttsx3.speak("Tell me your name")
user_name = input()
print(f"Hello {user_name}")
pyttsx3.speak(f"Hello {user_name}")
pyttsx3.speak("Let me provide you my work menu")
pyttsx3.speak("Here are the following tasks I can perform")
print("-> Open Google Chrome")
print("-> Open Notepad")
print("-> Open Microsoft Edge")
print("-> Open VLC")
print("-> Open VS Code")
print("-> Open Calculator")
print("-> Open Anaconda Navigator")
print("\nTo exit the program, type end/exit/quit")
pyttsx3.speak("Kindly go through the list once")
pyttsx3.speak("Now, tell me which task to perform?")
print("\nNow, tell me which task to perform?")
p=input()
p.lower()

if(("run" in p) or ("begin" in p) or ("launch" in p) or ("open" in p) or ("start"in p)):
    if(("chrome" in p) or ("google chrome" in p) or ("chrome browser" in p) or ("google browser" in p)):
        pyttsx3.speak("Opening Google Chrome Web Browser")
        print("\nOpening Google Chrome Web Browser...")
        os.system(chrome.exe)
    elif("notepad","text editor","editor" in p):
        pyttsx3.speak("Opening Notepad Text Editor")
        print("\nOpening Notepad Text Editor...")
        os.system(notepad.exe)
    elif(("microsoft browser" in p) or ("ms browser" in p) or ("edge" in p) or ("ms edge" in p) or ("ms edge browser" in p) or ("edge browser" in p)):
        pyttsx3.speak("Opening Microsoft Edge")
        print("\nOpening Microsoft Edge...")
        os.system(msedge.exe)
    elif(("vlc" in p) or ("vlc media player" in p) or ("music player" in p) or ("player" in p)):
        pyttsx3.speak("Opening VLC Media Player")
        print("\nOpening VLC Media Player...")
        os.system(vlc.exe)
    elif(("vs code" in p) or ("vsc" in p) or ("vs" in p) or ("visual studio code" in p)):
        pyttsx3.speak("Opening VS Code Editor")
        print("\nOpening VS Code Editor...")
        os.system(Code.exe)
    elif(("calculator" in p) or ("calc" in p)):
        pyttsx3.speak("Opening Calculator")
        print("\nOpening Calculator...")
        os.system(calc.exe)
    elif(("anaconda" in p) or ("anaconda navigator" in p)):
        pyttsx3.speak("Opening Anaconda Navigator")
        print("\nOpening Anaconda Navigator...")
        os.system(pythonw.exe)
    else:
        pyttsx3.speak("No such program defined for me! Sorry")
        print("No such program defined for me! Sorry")
        
elif (("end" in p) or ("exit" in p) or ("quit" in p)):
    pyttsx3.speak(f"Bye {user_name}! Exiting the program")
    print(f"Bye{user_name}! Exiting the program.....")
    pyttsx3.speak("Have a nice day!")
    
else:
    print("OOPS! Not a valid task entered! Can't perform the given task")
    pyttsx3.speak("OOPS! Not a valid task entered! Can't perform the given task")









