# **DevJams22-SAPS**

## Introduction

<br>

## Objectives

- To make a robust system that enables digital accessibility amoung differently abled persons.
- To connect with emergency contacts and provide immediate help.
- To provide our bussiness with our API, so as to help them use our tools to make their products more user friendly to the disabled community.

<br>

## Our Proposed Solution

- We propsed to create an app, which caters to the objectives stated above.

<br>

## Features

- To toggle between light, dark and low vision(Color Blindness) modes to see the perfect fit.
- To use already existing technolgy with ML and AI to provide a way for the mute to communicate with ease, even with those that don't know about the 'Indin Sign Language'.
- To provide TTS (Text to Speech) and STT (Speech to Text) to the mute and deaf, as well as to people with motor impairment.
- To provide medicare facilities to all our users, such as to track their medical appointments, schedule their regular appointments, pill alert notification, and etc.
- We took inspiration from Stream deck to make a ISL keyboard.

<br>

## Potential Upcoming Features

- To provide elderly with screen magnifactions options as well as a narrator.
- To enable voice commands, which can access everything in the application, with the users having a physical connection.
- To provide a API to other apps/softwares to use our tools, to make their apps/softwares more user friendly towards the disabled peoples.

<br>

## What are the disabilities are we tackling?

### Color Blindness

- We are using a python module called ["colorBlind"](https://pypi.org/project/colorblind/).
- This module helps us convert and image to a color blind friendly output, which a color blind a can see, and differentiat the deatils much clearly.
- At the current stage we are only supporting 3 varients of color blindness:
    - Deuteranopia (Red - Green weakness, particularly green)
    - Protanopia (Red - Green weakness, particulary red)
    - Trianopia (Blue weakness)

<br>

### Mute/Dumb

- We are using a python module called ["pyttsx3"](https://pypi.org/project/pyttsx3/).
- This module helps us to convert text to a speech format, so that it will be a more easier form of conversation.
- As well, as it can be use in a situation where the receiver doesn't know the sign language.
- We are also providing the ablity to use a gestures keyboard to communicate thier message.
- With the help of their actions our model can interpret it and frame the message accordingly to being about a more fluent type of conversation (Image processing using OpenCV and Tensorflow).

<br>

### Deaf/Motor Impairment

- We are using a python module called ["SpeechRecognition"](https://pypi.org/project/SpeechRecognition/).
- This module helps us convert speech to text, 

<br>

## UI/UX

- [UI/UX Demo Video](https://www.loom.com/share/c37ed5d54b6142d7873c238715318dc3)

<br>

<!-- - Along with this, we would require ["opencv-python"](https://pypi.org/project/opencv-python/), ["numpy"](https://pypi.org/project/numpy/), and ["matplotlib"](https://pypi.org/project/matplotlib/).
-  -->