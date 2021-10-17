# PROJECT ON LANE LINE DETECTION USING OpenCV.



I have done a project to detect lane line in real-time by using the concepts of computer vision using OpenCV library.

The purpose and concept of lane -line detection is to describe the path for self-driving cars and to avoid the risk of getting in another line. It is a critical component for computer vision in general and for self-driving cars.

There are multiple ways to perform lane detection, such as training a deep learning model or use a pre-trained model. However, i have done it without using any deep learning model. But used the popular OpenCV library in Python


In this i have first colected a set of images and put them in folder named FRAMES which i will use in the code,

first i have impoted all the necessary libray which we will be using
such as matplotlib, Numpy , os , re.
Now, in the next step i have accessed the downloaded folder named FRAMES.

Thses are futher steps which i done in the programe to get a output in form of line dection on a single frame
1. Loading the required Frames 
2. Frame Masking 
3. For mulating the problems like,
Instead of working with the entire frame, i worked with only a part of the frame. apart from the lane markings, everything else has been hidden in the frame. As the vehicle would move, the lane markings would fall in this area only.
4. Image Processing 
5. Image thresholding 
6. Hough line transformation 


#this is not the code which would run a video of lane detection for ever frame ,its just an example of how it is been done here a user can select a particular img no between  0-1800. Where the selected frame is given as an output.

THANK YOU!





