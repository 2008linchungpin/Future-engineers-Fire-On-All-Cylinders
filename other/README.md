## Diary Log

**Date：** 2022/6/4

**Members：** LIN,ZHONG-BIN

**Content：**

After reading the rules of the competition, we figured out some materials and electromachanical components that were needed when constructing the outline of the car and the its structure design. We also got to think about how to use only one piece of Dc Gear Motor to drive the vehicle and to assemble the fundamental model of the turning section.

<img src= "https://user-images.githubusercontent.com/106851896/176984877-f74ac4e4-97b1-49e1-bfa5-84112426c236.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176984586-d9094acf-c13c-4dc4-bf20-022f951bf5ed.jpg" width="400" height="300"><br/>

*****
**Date：** 2022/6/5 - 2022/6/7

**Members：** LIN,ZHONG-BIN

**Content：**

During these days, we started to design the construction of the vehicle. Dividing it into three straight layers, we put the necessary components onto it. With the help of Onshape and the laser beam cutting machine, we can easily draw the outline of the automobile and then cut the plank into the shape we needed so as to build the carbody structural member. 

<img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220807_102434.jpg" width="600" height="300"><img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E4%B8%8B.png" width="250" height="300">


*****
**Date:** 2022/6/8 - 2022/6/10 

**Members：** LIN,ZHONG-BIN

**Content：**

Confirming the car's shape, we started off to choose the motors. For now we have GA25-370 in hand, and while checking some datasheets on the internet, we bought the JGA16-050 because it's much lighter and was not as large as the GA25-370. But in spite of the advantages of JGS16-050, we still ultilized GA25-370 to drive the vehicle after practical comparasions due to the efficiency they provided.

<img src= "https://user-images.githubusercontent.com/106851896/176989086-27531ee9-5cdb-40cb-8e0b-7d376ba59e3e.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176989089-816688a2-115c-4d20-a689-e17af9d53a5a.jpg" width="400" height="300"><br/>

*****
**Date:** 2022/6/11

**Members：** LIN,ZHONG-BIN

**Content：**

Considering that the GA25-370 needed a total of 12 operating voltage, we set up a L298n Dc Motor Drive to control the movement of the GA25-370 Dc Gear Motor. On the other hand, L298n needs a external power supply. So we design a route that connects the L298n Dc Motor Drive to a 12-volt lithium polymer.

<img src= "https://user-images.githubusercontent.com/106851896/176989980-82d65ada-de48-4de4-8b35-44c4a550eb33.jpg" width="400" height="300">


*****
**Date：** 2022/6/13 - 2022/6/14

**Members：** LIN,ZHONG-BIN

**Content：**

At first, we chose to use the MG996R servo motor to drive the steering mechanism. Though the MG996R servo motor we installed on the steering mechanism had a large torque, with the heavy weight it got, its rotation speed was so slow that the vehicle would rather crush into the wall than turn into the correct position. In the end, we chose the SG90S servo motor in view of the lighter weight and  the faster rotate speed which make it easier for the car to pass through the .


<img src= "https://user-images.githubusercontent.com/106851896/178086536-d1ad5c58-ee7f-4514-9b3d-6e2d4f79cfdf.jpg" width="400" height="300"> <img src= "https://user-images.githubusercontent.com/106851896/178086538-f11aecf4-af52-4141-a643-7ee231f0d225.jpg" width="400" height="300">

*****
**Date：** 2022/6/17 - 2022/6/18

**Members：**  LIN,ZHONG-BIN

**Content：**

Based on the displacement of the servo motor on the steering mechanism of our vehicle, we had to redesign the mechanism with the intention that the SG90S servo motor could be mounted on it. We put the SG960S servo motor on the second layer of the vehicle, being more convenient to connect to the steering mechanism. Appropriately, the steering mechanism operates more smoothly.


<img src= "https://user-images.githubusercontent.com/106851896/178087399-1efc9875-dcfc-4141-bd51-6f2f8170cec8.PNG" width="550" height="300">

*****
**Date：** 2022/6/20

**Members：** LIN,ZHONG-BIN

**Content：**

We integrated those three layer of boards together, measured the height of it and the components. Selecting the insulating columns that were suitable for those abovementioned objects, we used them to fix the layers together longitudinally for the purpose of forming the basic prototype of the vehicle.


<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_6428.JPG" width="400" height="300">

*****
**Date：** 2022/6/23 - 2022/6/25

**Members：**  LIN,ZHONG-BIN

**Content：**

If the controller has an environment capable of setting up AI image recognitions, the controller is bound to be a microcomputer. Considering this condition, we chose the Raspberry Pi 4 with GPIO pins to control the pad components as the controller of our vehicle.


<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220911_122648.jpg" width="400" height="300">

*****
**Date：** 2022/6/27 - 2022/6/28

**Members：**  LIN,ZHONG-BIN

**Content：**

With only the Dc motor and servo motor installed in the vehicle, the controller is not yet finished. We chose to use the Raspberry Pi 4, and for the reason, owing to the high program computing efficiency and the small size it provides, it makes the function of image recognizing far superior. We installed Raspberry Pi 4 on the third (the lowest) layer, and then fixed it onto the layer with plastic screws.

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220918_103912.jpg" width="400" height="300">

*****
**Date：** 2022/6/29

**Members：**  LIN,ZHONG-BIN

**Content：**


After completing the basic prototype of the vehicle, we select the controller that meets our requirements. The requirements unfolded down below.

1. Can sends signals to control GPIO

2. Can employ the electronic components without restriction

3. With a capability to build a environment to recognize AI images


<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220911_120738.jpg" width="400" height="300">

*****
**Date：** 2022/6/30

**Members：** LIN,ZHONG-BIN

**Content：**


Today we installed the 12V battery on the vehicle and adjusted the output voltage of the switching power adapter to 5V. Shortly after the installation, we then tested the vehicle's turning function and driving motor function. No sooner had the vehicle started to turn than we found that  the battery would be thrown out, causing the model rolling over. With an eye on the resolution, we thought that we could use a hook and loop fastener to embed the battery. On the other hand, it can not only stable the battery but also allow us to unplug and charge it at any wish.


<img src= "https://user-images.githubusercontent.com/106851896/176991414-0866b49d-fd78-4443-be90-2231f7c6d430.jpg" width="400" height="300">

*****
**Date：** 2022/7/1 - 2022/7/10

**Members：**  LIN,ZHONG-BIN

**Content：**


After completing the battery installation, we started the circuit configuration of the vehicle and the hardware settings of Donkey Car, an open source project which gives us a humongous room for developing and creating the hardware configuration.


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E7%B7%9A%E8%B7%AF.jpg.png" width="400" height="300">

*****
**Date：** 2022/7/16 - 2022/7/20

***Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


We set up virtual environment for the Raspberry Pi and  Donkey Car. After completing, we adjust the rudder direction. After the adjustment, we started to train the vehicle by remote controlling and filming the site . No sooner had we finished training, the model can run clockwise and opposite automatically. 


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220811_081727.jpg"  width="600" height="300">

*****
**Date：** 2022/7/24

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


During training, the machine always paused while running. At first, we thought it was caused by insufficient battery power or the motor, so we decided to change the battery, it was no good. At length, we found out that the over-length of Dupont line caused the stuck of the wheel.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220919_191252.jpg" width="500" height="400">

*****
**Date：** 2022/7/26

**Members：**  LIN,ZHONG-BIN

**Content：**


Since the Dupont line in our model is too messy, we cut it all off and replace them with a much tidier form so that they wouldn't trap the vehicle while running.

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220810_102902.jpg" width="600" height="300">

*****
**Date：** 2022/7/28

**Members：**  LIN,ZHONG-BIN

**Content：**


We are going to compete in the Mid-Taiwan competition tomorrow, with an eye on preventing us from the misdectect during the competition causes the disqualification, we had a simulate contest to predict the problems we may come across when contesting.


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/S__6086661.jpg" width="500" height="400">

*****
**Date：** 2022/7/29 - 2022/7/30

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


It's the very day of the mid-Taiwan competition. The schedule starts from 12 p.m. and ends in 12p.m. next day. Unlike last year, there're few easy-to-run tests to complete. 

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/2022-08-15%20142636.png" width="700" height="400">

*****
**Date：** 2022/8/2 - 2022/8/7

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


When the mid-Taiwan competition is over, we began to prepare the detecting and dodging blocks for the national competition. In the past few days, we randomly placed the blocks from far, middle, and near to take 70 photos each, then imported them into the computer to carry out the border marqueeing and color identifying.


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/156.jpg" width="500" height="300">

*****
**Date：** 2022/8/9

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After a series of tests, we found out that our technology is not mature enough to identify the blocks, so we decided to use HLS to detect the hue, saturation, and brightness of the blocks, so that the probability of misdetection is relatively low.




<img src =  "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E6%93%B7%E5%8F%96.PNG"  width="500" height="300">

*****
**Date：** 2022/8/12

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


An stupid incident happended is that we had bought the wrong lens, we should have used a lens with an infrared filter but no night vision function but we bought a lens with no infrared filter and night vision function. It's made us hard to proceed 'cause we can't filter the sunlight out.


<img src ="https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220815_103756.jpg" width="600" height="300">

*****
**Date：** 2022/8/15

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


We had almost completed the identification of all the official obstacle combinations. In addition, we have re-arranged the tests. However, during the test, there were still some problems of lens misdetection, which needs to be fine-tuned.


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/0.1.png" width="400" height="500">

*****
**Date：** 2022/8/18

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


In the process of running the vehicle, the camera often misdetected or did not detect the blocks and went pass it, so we added a ultrasonic sensor to detect whether there are obstacles. But it turned out that it was only because there was no enough time for it to react and dodge the blocks.



<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220903_100640.jpg" width="450" height="300">

*****
**Date：** 2022/8/20

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

We found out that the misdetection of the lens is mostly due to the wrong installation of the vehicle, so we fixed the lens backward, changed the position of the sensor, and rewound the lens. There were not much to be desired after that.



<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220903_100536.jpg" width="600" height="300">

*****
**Date：** 2022/8/24

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After changing the position of the lens, there were no other major mistakes basically. But there were some chances that the turning angle is so wide that fender bender
occurred. Nevertheless, we came through it within a short period of time. Afterwards, we started to prepare the spare components for the national competition.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/113502.png" width="400" height="500">

*****
**Date：** 2022/8/26

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


It was the day of the WRO National Finals. The schedule was Qualification in the morning and the Finals in the afternoon. Before the Finals start, we had to take part  in the Qualification because we didn't use matrixmini into our vehicle. After two rounds of Qualification, the results are not very satisfactory. But we still made it to the Finals. We ran very smoothly in the first round and got full marks. But in the second round, the vehicle did not turn enough when detecting the red block, and the red was knocked. Though we didn't get full score in the second round, we still managed to win first place and advance to the World Championship.

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/0910.png" width="1000" height="120">

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/82627.jpg" width="400" height="300"> <img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/S__69804048.jpg" width="400" height="300">

*****
**Date：** 2022/9/3 - 2022/9/4

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


In order to gain first place in the World Championship, we decided to increase the speed of our vehicle, so we re-soldered the circuit board to a smaller size to save some space. Afterwards, we shortened the length of the vehicle so that it can be more flexible turning and dodging the blocks.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220904_111012.jpg" width="600" height="400">

*****
**Date：** 2022/9/7 - 2022/9/8

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After we zoomed the vehicle out, the sensors and the Raspberry pi on the model needed to be rearranged. Since the previous model was larger,and the line was longer, changing those overlength wires are necessary. If the wires are too long, they will hook the wheel and block the lens, so we cut the wires and rewound them.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_6426.JPG" width="400" height="300">

*****
**Date：** 2022/9/10

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


When we practiced today, we didn't have the faintest clue why the Raspberry pi keep restarting, but who to blame? We first thought it was the Dupont lines were broken, so we made every endeavor to check the Dupont wires one by one. When all the Dupont lines were checked, nothing was wrong, so we started off to examine the whole vehicle, only to find that the servo motor was burned out, and everything went normal after we change a good one instead.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_6422.JPG" width="450" height="300">

*****
**Date：** 2022/9/11

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After the broken servo motor was replaced, there was no further error during the test. After several days of revisions, the model was finally capable to run the entire process flawlessly.


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/2022-09-22%20220906.png" width="450" height="300">
