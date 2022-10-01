# **DevJams22-SAPS**

## **Introduction**

We are making a software, that will help the disable community all over the globe. Our application provides all the necessary tools for one to communicate without and issues.

<br>

## **Objectives**

- To make a robust system that enables digital accessibility among differently abled persons.
- To connect with emergency contacts and provide immediate help.
- To provide our business with our API, so as to help them use our tools to make their products more user friendly to the disabled community.

<br>

## **Our Proposed Solution**

- We propsed to create an app, which caters to the objectives stated above.

<br>

## **Features**

- To toggle between light, dark and low vision(Color Blindness) modes to see the perfect fit.
- To use already existing technolgy with ML and AI to provide a way for the mute to communicate with ease, even with those that don't know about the 'Indin Sign Language'.
- To provide TTS (Text to Speech) and STT (Speech to Text) to the mute and deaf, as well as to people with motor impairment.
- To provide medicare facilities to all our users, such as to track their medical appointments, schedule their regular appointments, pill alert notification, and etc.
- We took inspiration from Stream deck to make a ISL keyboard.

<br>

## **Potential Upcoming Features**

- To provide elderly with screen magnifactions options as well as a narrator.
- To enable voice commands, which can access everything in the application, with the users having a physical connection.
- To provide a API to other apps/softwares to use our tools, to make their apps/softwares more user friendly towards the disabled peoples.

<br>

## **What are the disabilities are we tackling?**

We are currently tackling color blindness, mute/dumb, deaf and motor impairment.

Before we go further into detail, let's see a few problems that these people face in their day - day life.

- Fewer educational and job opportunities due to impaired communication.
- Social withdrawal due to reduced access to services and difficulties in communicating with other, etc.

<br>

### **Color Blindness**

- We are using a python module called ["colorBlind"](https://pypi.org/project/colorblind/).
- This module helps us convert the image to a color blind friendly output, which a color blind a can see, and differentiat the deatils much clearly.
- At the current stage we are only supporting 3 varients of color blindness:
    - Deuteranopia (Red - Green weakness, particularly green)
    - Protanopia (Red - Green weakness, particulary red)
    - Trianopia (Blue weakness)

<br>

### **Mute/Dumb**

- We are using a python module called ["pyttsx3"](https://pypi.org/project/pyttsx3/).
- This module helps us to convert text to a speech format, so that it will be a more easier form of conversation.
- As well, as it can be use in a situation where the receiver doesn't know the sign language.
- We are also providing the ablity to use a gestures keyboard to communicate thier message.
- With the help of their actions our model can interpret it and frame the message accordingly to being about a more fluent type of conversation (Image processing using OpenCV and Tensorflow).

<br>

### **Deaf and Motor Impairment**

- We are using a python module called ["SpeechRecognition"](https://pypi.org/project/SpeechRecognition/).
- This module helps us convert speech to text,
- We can also help people with motor impairment, as they face the difficulty of using their hands. Hence, by using this, they would be able to enjoy texting, typing notes, etc.

<br>

---

## **Market Research (India)**

- According to the 2011 Indian census, out of a total population of 121 billion, 2.68 billion people were counted as disabled, representing 2.21 percent of the population. 56% of the disabled population was male, while 44% was female. 69% of disabled people live in rural areas, compared to 31% in urban areas.

- The percentage of disabled individuals by social group in India during 2011. The percentage of disabled men and women is 2.41 percent and 2.0 percent, respectively. At both the all-India level and the level disaggregated by various social groups, the proportion of disabled women is greater than that of disabled men.

![Stats1](/Images/Readme%20Image/Stats%202.png)

- The Census 2011 revealed that, in India, 20% of the disabled persons are having disability  in  movement,  19%  are  with  disability  in  seeing,  19  %  are  with  disability  in hearing and 8% has multiple disabilities.

![Stats2](/Images/Readme%20Image/Stats%201.png)


---

## **UI/UX**

-  

- [UI/UX Demo Video for APP](https://www.loom.com/share/c37ed5d54b6142d7873c238715318dc3)

<br>

## **Web App**

<br>

## **Python Modules**

### Colorblind Module

-  Colorblind is a computer vision library that transforms images into colorblind-friendly versions based on the type of colorblindness.
- It uses 3 types of algorithm to correct the image:
    - Daltonization: Original method for generating color - friendly images.
    - HSV Hue Shift: Shifts hue based on green to red ratio(depending on colorblindness type).
    - LAB Shift: Previous studies for this had to tune hyperparameters to get good result.

### Pyttsx3 Module

- It's a text to speech conversion libary, it's added benifit is that it works offline.

### SpeechRecognition

- It's a speech to text conversion libary, it supports multiple API's. But for our case we will be using the Google Speech Recognition.

<br>

---

## **Installation**

Before running the python scripts, please make sure to install the following pip modules given below.

You also are required to have python version 3.7+

```
pip install opencv-python
pip install numpy
pip install malplotlib
pip install pyttsx3
pip install SpeechRecognition
pip install colorblind
```

<br>

---

## **Our Team**

- Swarab Raul [@linkedin](https://www.linkedin.com/in/swarab-raul-186106235/)
- Anjali Kedia [@linkedin](https://www.linkedin.com/in/anjali-kedia-10896320a/)
- Pritika Kannapiran [@linkedin](https://www.linkedin.com/in/pritika-kannapiran-388557223/)
- Shakti Nayak [@linkedin](https://www.linkedin.com/in/shakti-nayak-b486b4238/)

<br>