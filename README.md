# PROJECT ON LANE LINE DETECTION USING OpenCV.



I have done a project to detect lane line in real-time by using the concepts of computer vision using OpenCV library.

The purpose and concept of lane -line detection is to describe the path for self-driving cars and to avoid the risk of getting in another line. It is a critical component for computer vision in general and for self-driving cars.

There are multiple ways to perform lane detection, such as training a deep learning model or using a pre-trained model. However, I have done it without using any deep learning model and instead used the popular OpenCV library in Python


Firstly, I've  collected a set of images and put them in a folder named FRAMES which will be used in the code later.

 Then I have imported all the necessary libray which we will be using
such as matplotlib, Numpy , os , re.
Now, in the next step I have accessed the downloaded folder named FRAMES.

These are the futher steps which I've done in the programme to get an output in the form of line detection in a single frame
1. Loading the required Frames 
2. Frame Masking 
3. Formulating the problems
   For example: Instead of working with the entire frame, I've worked with only a part of the frame and apart from the lane markings, everything else has been hidden in the frame. So, as the vehicle would move, the lane markings would fall in this area only.
4. Image Processing 
5. Image thresholding 
6. Hough line transformation 


#this is not the code which would run a video of lane detection for every frame ,its just an example of how it has been done. 
 In this programme, an user can select a particular img no between  0-1800, wherein the selected frame will be given as an output.

THANK YOU!





