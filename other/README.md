## Diary Log

**Date：** 2022/6/4

**Members：** LIN,ZHONG-BIN

**Content：**

After reading the rule of the competition, we figured out some materials and electromachanical components that were needed when constructing the outline of the car and the its structure design. We also got to think about how to use only one piece of Dc Gear Motor to drive the vehicle and to assemble the fundamental model of the turning section.

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

Confirming the car's shape, we started off to choose the motors. For now we have GA25-370 in hand, and while checking some datasheets one the internet, we bought some JGA16-050 because it's much lighter and was not as large the GA25-370. But in spite of the advantages of JGS16-050, we still ultilized GA25-370 for driving the vehicle after practical comparasions due to the efficiency they provided.

<img src= "https://user-images.githubusercontent.com/106851896/176989086-27531ee9-5cdb-40cb-8e0b-7d376ba59e3e.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176989089-816688a2-115c-4d20-a689-e17af9d53a5a.jpg" width="400" height="300"><br/>

*****
**Date:** 2022/6/11

**Members：** LIN,ZHONG-BIN

**Content：**

Condering that the GA25-370 needs a total 12 of operating voltage, we set up a L298n Dc Motor Drive to control the movement of the GA25-370 Dc Gear Motor. On the other hand, L298n needs a external power supply. So we design a route that connects the L298n Dc Motor Drive to a 12-volt lithium polymer.

<img src= "https://user-images.githubusercontent.com/106851896/176989980-82d65ada-de48-4de4-8b35-44c4a550eb33.jpg" width="400" height="300">


*****
**Date：** 2022/6/13 - 2022/6/14

**Members：** LIN,ZHONG-BIN

**Content：**

At first, we chose to use the MG996R servo motor to drive the steering mechanism. Though the MG996R servo motor we installed on the steering mechanism had a large torque, with the heavy weight it got, its rotation speed was too slow, so that the vehicle would rather crush into the wall than turn into the correct position. In the end, we chose the SG90S servo motor in view of the lighter weight and  the faster rotate speed which make it easier for the car to pass through the curve.


<img src= "https://user-images.githubusercontent.com/106851896/178086536-d1ad5c58-ee7f-4514-9b3d-6e2d4f79cfdf.jpg" width="400" height="300"> <img src= "https://user-images.githubusercontent.com/106851896/178086538-f11aecf4-af52-4141-a643-7ee231f0d225.jpg" width="400" height="300">

*****
**Date：** 2022/6/17 - 2022/6/18

**Members：**  LIN,ZHONG-BIN

**Content：**

Based on the displacement of the servo motor on the steering mechanism of our vehicle, we had to redesign the mechanism so that the SG90S servo motor could be mounted onto it. We put the SG960S servo motor on the second layer of the vehicle, being more convenient to connect to the steering mechanism. What's more, the steering mechanism operates more smoothly as we did so.


<img src= "https://user-images.githubusercontent.com/106851896/178087399-1efc9875-dcfc-4141-bd51-6f2f8170cec8.PNG" width="550" height="300">

*****
**Date：** 2022/6/20

**Members：** LIN,ZHONG-BIN

**Content：**

We integrated those three layer of boards together, measured the height of it and the components. Selecting the insulating columns that're suitable for those abovementioned things, we used them to fix the layers together longitudinally for the purpose of forming the basic prototype of the vehicle.


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

With only the Dc motor and servo motor installed in the vehicle, the controller is not yet finished. We chose to use the Raspberry Pi 4, and for the reason, owing to the high program computing efficiency and small size it provides, it makes the function of image recognizing far superior. We installed Raspberry Pi 4 on the third (the lowest) layer, and then fixed it onto the layer with plastic screws.

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

在完成架設電池的部分之後，我們就開始車輛的電路配置與Donkey car軟體設置，在使用Donkey car過程中時得知Donkey Car是一項開源專案，車輛的硬體配置可以自由開發與創造的軟體。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E7%B7%9A%E8%B7%AF.jpg.png" width="400" height="300">

*****
**Date：** 2022/7/16 - 2022/7/20

***Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


We set up virtual environment for the Raspberry Pi and  Donkey Car. After completing, we adjust the rudder direction of the machine's turning. After the adjustment, we started to train the vehicle by remote control and filming the site . No sooner had we finished training, the model can run clockwise and opposite automatically. 

我們將樹莓派與Donker軟體環境架設，在架設完成以後調整機器轉彎的舵向，調整過後就直接開始進行遙控機型拍攝場地照片訓練，經過訓練後機型可以自主跑完順時針逆時針的題目。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220811_081727.jpg"  width="600" height="300">

*****
**Date：** 2022/7/24

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


During training, the machine always paused while running. At first, we thought it was caused by insufficient battery power or the motor, so we decided to change the battery, it was no good. At length, we happened to find the over-length of Dupont line caused the stuck of the wheel.

在訓練的時候機器總是會頓一下頓一下的行始，一開始我們以為電池電量不足或是馬達導致，之後換過電池以後也是一樣，最後發現是杜邦線太長導致卡到輪胎。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220919_191252.jpg" width="500" height="400">

*****
**Date：** 2022/7/26

**Members：**  LIN,ZHONG-BIN

**Content：**


Since the Dupont line in our model is too messy, we cut it all off and replace them with a much tidier form so that they wouldn't trap the vehicle while running.

由於我們機型上面的杜邦線過於混亂，所以我們今天訓練完以後在回家之前把杜邦線都換掉重新剪線整理，避免機型在行駛過程中杜邦線太長勾到場地導致失誤。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220810_102902.jpg" width="600" height="300">

*****
**Date：** 2022/7/28

**Members：**  LIN,ZHONG-BIN

**Content：**


We are going to compete in the Mid-Taiwan competition tomorrow, with an eye on preventing us from the misdectect during the competition causes the disqualification, we had a simulate contest to predict the problems we may come across when contesting.

由於我們明天就要比中區賽了，為了避免我們在比賽過程中不知道該怎麼錄影出現錯誤，導致失去資格，所以我們今天進行了一場小型的模擬賽，訓練我們如何避免比賽中可能會遇到的問題。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/S__6086661.jpg" width="500" height="400">

*****
**Date：** 2022/7/29 - 2022/7/30

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


It's the very day of the mid-Taiwan competition. The schedule starts from 12 p.m. and ends in 12p.m. next day. Unlike last year, there're few easy-to-run tests to complete. 

今天是中區賽，跟去年中區賽一樣從中午12點比到隔天中午的12點為止，今年很可惜的是跟去年相比，今年較好的題目比去年的還要少。我們自從比賽開始就一直在等最短路徑，直到隔天的早上6點才出現最短路徑。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/2022-08-15%20142636.png" width="700" height="400">

*****
**Date：** 2022/8/2 - 2022/8/7

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**


When the mid-Taiwan competition is over, we began to prepare the detecting and dodging blocks for the national competition. In the past few days, we randomly placed the blocks from far, middle, and near to take 70 photos each, then imported them into the computer to carry out the border marqueeing and color identifying.

中區賽結束以後，我們就開始準備全國賽閃避積木的偵測，這幾天我們將積木由遠、中、近分別隨機擺放各拍70張照片，在匯出到電腦中框選進行圖型顏色的辨識。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/156.jpg" width="500" height="300">

*****
**Date：** 2022/8/9

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

After a series of tests, it is a little difficult to identify because our technology is not yet mature, so we have decided to switch to HLS to detect the hue, saturation, and brightness of the building blocks, so that the probability of false detection is relatively low.

經過一系列的測試過後，由於我們的技術尚未成熟所以用來辨識有點困難，所以我們目前決定要改用HLS偵測積木的色相、飽和度、亮度，這樣誤測的機率比較低。


<img src =  "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E6%93%B7%E5%8F%96.PNG"  width="500" height="300">

*****
**Date：** 2022/8/12

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

Because we bought the wrong lens, we should have used a lens with an infrared filter but no night vision function. As a result, we bought a lens with no infrared filter and night vision function, so we could not filter out the sunlight during the normal running process, so Not ideal to run.

由於我們鏡頭買錯，我們原本該用有紅外線濾鏡無夜視功能的鏡頭，結果我們買到無紅外線濾鏡有夜視功能的鏡頭，所以我們平常跑的過程中無法把太陽光濾掉所以跑起來不是很理想。

<img src ="https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220815_103756.jpg" width="600" height="300">

*****
**Date：** 2022/8/15

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

Today, we have almost completed the identification of all the official obstacle combinations. In addition, we have re-arranged the questions. However, during the test, there will still be the problem of lens misdetection, which needs to be fine-tuned.

今天我們近乎把官方出的所有障礙物組合辨識完畢，另外我們還有重新編排出題，但是在測試過程中還是會出現鏡頭誤測的問題，需要再進行微調。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/0.1.png" width="400" height="500">

*****
**Date：** 2022/8/18

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

In the process of running the model, the camera always misdetected or did not detect the building blocks and went around directly, so we added ultrasonic detection to detect whether there are obstacles. The reaction is not as fast, so there is no dodge.

在機型跑的過程中鏡頭總是誤測或是沒有測到積木直接繞過去，所以我們加入了超音波偵測是否有障礙物，在測試了一段時間才知道鏡頭有偵測到障礙物只是反應不及所以沒有閃避。


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220903_100640.jpg" width="450" height="300">

*****
**Date：** 2022/8/20

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Goofle翻譯)

Today, we found that the misdetection of the lens is mostly due to the installation method of the model, so we installed the lens backward, and changed the position of the sensor on the model, and then rewound the lens. Much improved.

今天我們發現鏡頭會誤測多半是機型裝法的問題，所以我們就把鏡頭往後裝，順便把機型上的感測器換過位置後，再把線重繞以後鏡頭誤測的問題改善了很多。


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220903_100536.jpg" width="600" height="300">

*****
**Date：** 2022/8/24

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

After changing the position of the lens, there are basically no other major mistakes, but there are still some models that are turned too large and cause obstacles. After solving the problem, we will start to prepare spare parts for Taipei.

鏡頭換過位置以後基本上已經沒有其他太大的失誤，但還是會有機型轉太大導致差到障礙物，在解決問題以後我們就要開始準備去台北的備用零件。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/113502.png" width="400" height="500">

*****
**Date：** 2022/8/26

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

***Content：**

(Google翻譯)

Today is the day of the WRO National Finals. The competition time is the qualifying rounds in the morning and the finals in the afternoon. Before the finals start, we have to compete in the qualifying rounds before the finals in the afternoon. After the two qualifying rounds, the results are not very satisfactory. But we still made it to the finals. We ran very smoothly in the first race and got a full score, but in the second race, the machine did not turn enough when the red obstacle was flashing, and the red was knocked out, resulting in no second race. Full marks, but we still managed to win the first place and advance to the World Championship.

今天是WRO全國總決賽的日子，比賽時間上午為資格賽則下午比決賽，在比決賽開始之前我們要先比資格賽才能比下午的決賽，在兩趟資格賽跑完以後雖然成績不是很理想，但還是有進入決賽，我們第一場跑得很順利跑出了滿分的成績，但是在跑第二場時機器在閃紅色障礙物時轉彎轉的不夠大把紅色撞出來了導致第二場沒有滿分，但我們還是有驚無險的拿下第一名晉級世界賽。
<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/0910.png" width="1000" height="120">

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/82627.jpg" width="400" height="300"> <img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/S__69804048.jpg" width="400" height="300">

*****
**Date：** 2022/9/3 - 2022/9/4

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


In order to get a good ranking in the World Championship, we decided to increase the speed of the model, so we re-soldered the circuit board to a smaller size to save unnecessary space. Afterwards, we shortened the length of the vehicle so that it can be More flexible turning and dodging obstacles.

為了能夠在世界賽中拿到好的名次，所以我們決定要將機型的速度提升，所以我們把電路板重新焊小一點節省不必要的空間，再把機型的長度縮短這樣機型就能夠更靈活的轉彎與閃避障礙物。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_20220904_111012.jpg" width="600" height="400">

*****
**Date：** 2022/9/7 - 2022/9/8

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After we zoomed the vehicle out, the sensors and the Raspberry pi on the model needed to be rearranged. Since the previous model was larger,and the line was longer, changing those overlength wires are necessary. If the wires are too long, they will hook the wheel and block the lens, so we cut the wires and rewound them.

我們將機構改小以後，機型上的感測器與樹梅派都要重新擺放，由於之前的機型比較大所以線比較長，把之前的線換到小台的機型上會因為線太長會勾到輪子擋到鏡頭，所以我們重新剪線繞線。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_6426.JPG" width="400" height="300">

*****
**Date：** 2022/9/10

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


When we practiced today, we didn't have the faintest clue why the Raspberry pi keep restarting, but who to blame? We first thought it was the Dupont lines were broken, so we made every endeavor to check the Dupont wires one by one. When all the Dupont lines were checked, nothing was wrong, so we started off to examine the whole vehicle, only to find that the servo motor was burned out, and everything went normal after we change a good one instead.

今天我們練習時不知為何樹梅派一直重新開機，我們懷疑是杜邦線的問題，所以就把杜邦線一條一條的拆下來重新檢查，當我們已經把所有的杜邦線都檢查過一遍了都沒有損壞，卻始終找不到問題出在哪，之後又重新檢查了一遍，才發現是伺服馬達燒掉了，我們重新換過一顆伺服馬達以後就正常了。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/other/Diary%20photos/IMG_6422.JPG" width="450" height="300">

*****
**Date：** 2022/9/11

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**


After the broken servo motor was replaced, there was no further error during the test. After several days of revisions, the model was finally capable to run the entire process flawlessly.

將壞掉的伺服馬達換掉了以後，在測試時也沒有再發生過任何一個失誤，經過這幾天的修改以後終於能夠完整的讓機型完美無誤跑完全程。

