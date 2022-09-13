# Fire-On-All-Cylinders

## Team lntroduction

**LIN,BO-SHENG**

Taichung Industrial Senior High School

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6410.JPG" width="300" height="400">

**LI,DING-WEI**

Ming-Dao High School

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6403.JPG" width="300" height="400">

**LIN,ZHONG-BIN**

Taiping Junior High School

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6404.JPG" width="300" height="400">

**Team Photos**

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1738.JPG" width="400" height="300">


**A Funny One**

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1740.JPG" width="400" height="300">

**Official Photo**

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/82627.jpg" width="650" height="500">

## YouTube URL

https://reurl.cc/W18Wl9

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/sddefault.jpg" width="400" height="300">

## Vehicle Introduction

We use 3mm planks which were cut by the laser beam cutting machine as the chassis of our vehicle and design the turning section along with LEGO blocks with the intention of shrinking the dimension and stabilizing it. On top of that, considering that the Raspberry Pi 4 isn't only quick in operating but is suitable for image identifying, we chose it as the main controller of our vehicle.

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/car.png" width="400" height="300">

## Introduces of Electromechanical Components

GA25-371 Dc Gear Motor：Drives the rear wheels of the vehicle in order to control it move forward and backward.  

MG90S-Metal Gear Micro Servo Motor：Force the mechanical structure to let the vehicle turn.  

Lithium Polymer：Provides electricities for the Raspberry and other electromechanical components.  

L293D Motor Driver: Controls GA25-371 Dc Gear Motor to turn clockwise, conterclockwise, and alter the direction of it.  

ADIO-DC36V5A Switching Power Adapter：Stable the electricity that the lithium polymer provides  

jmdo.96c OLED display：To show some specific numerical data of the Raspberry.  

Tcs34725 RGB Color Sensor：To dectect lines and calculate the laps the vehicle had passed.   

Raspberry pi Camera (G)：Images collecting and identifying.  

Arduino Ultrasonic Sensor : Calculate the length between the wall and the vehicle.  

Raspberry Pi 4：In charge of all the models of vehicle controllers. 

# Vehicle Structure Introduction
## Differential

In order to solve the problem that the path taken by the outer wheels is larger than the path taken by the inner wheels when turning, we install a differential.

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1749.JPG" width="400" height="300">


## The Turing Section

In order to have better steering, we design the steering rudder as Ackerman steering structure, and use the servo motor to control the steering of the steering rudder.

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1748.png" width="400" height="300">

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
考慮到GA25-370需要12v的工作電壓，我們安裝L298n直流馬達控制板控制GA25-370直流馬達的動作。因為L298n直流馬達控制板需外接電源，所以我們製作了一個12v的鋰電池連接到L298n直流馬達控制板的線。

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

(Google翻譯)

Since our vehicle replaced the servo motor on the steering mechanism, we had to redesign the mechanism so that the SG90S servo motor could be mounted on the vehicle. We put the SG960S servo motor in the second layer of the vehicle, which is more convenient to connect the steering mechanism, and the steering mechanism operates more smoothly.

由於我們車輛更換轉向機構上的伺服馬達，我們必須重新設計機構讓SG90S伺服馬達可以安裝於車輛上。我們將SG960S伺服馬達共訂在車輛的第二層中，更方便讓轉向機構連接，轉向機構運作起來更順暢。

<img src= "https://user-images.githubusercontent.com/106851896/178087399-1efc9875-dcfc-4141-bd51-6f2f8170cec8.PNG" width="550" height="300">

*****
**Date：** 2022/6/20

**Members：** LIN,ZHONG-BIN

**Content：**

(google翻譯)

We integrate the three-layer boards together, measure the height of each layer of boards and components, select insulating columns with appropriate height, and use insulating columns to fix the three-layer boards together longitudinally to form the basic prototype of the vehicle.

我們將三層板子整合在一起，測量每層板子和元件的高度，選用高度合適的絕緣柱，並利用絕緣柱將三層板子縱向的固定在一起，形成車輛的基本雛形。

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6428.JPG" width="400" height="300">

*****
**Date：** 2022/6/23 - 2022/6/25

**Members：**  LIN,ZHONG-BIN

**Content：**

(Google翻譯)

If the controller has an environment capable of setting up image recognition AI, the controller is bound to be a microcomputer. Considering these conditions, we choose the Raspberry Pi as the controller of our vehicle, and the Raspberry Pi has GPIO pins to control the pad components.

若控制器有能架設影像辨識AI的環境，那控制器勢必會是微電腦。考慮到這些條件，我們選擇樹梅派作為我們的車輛的控制器，且樹梅派有GPIO的腳位可以控制墊子元件。

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220911_122648.jpg" width="400" height="300">

*****
**Date：** 2022/6/27 - 2022/6/28

**Members：**  LIN,ZHONG-BIN

**Content：**
(Google翻譯)

After the DC motor and servo motor are installed in the vehicle, the controller is not yet installed in the vehicle, and we choose to use the Raspberry Pi 4. The reason why we choose to use the Raspberry Pi 4 is that the Raspberry Pi 4 has high program computing efficiency and small size. , more suitable for image recognition function. We installed Plum Pie 4 on the third layer, and fixed the Plum Pie and the 3mm wooden board of the third energy with bare wire.

車輛安裝完直流馬達與伺服馬達後，車輛剩下控制器尚未安裝，而控制器我們選擇使用樹梅派4，之所以選擇使用樹梅派4是因為，樹梅派4程式運算效能高體積小，更適合用來ˊ做影像辨識功能。我們將樹梅派4安裝於第三層位置，將樹梅派與第三能的3mm木板用裸絲固定起來。

*****
**Date：** 2022/6/29

**Members：**  LIN,ZHONG-BIN

**Content：**

(Google翻譯)

After completing the basic prototype of the vehicle, we select the controller that meets our requirements. After discussion, our requirements for the controller are as follows:

1. There are signals to control GPIO

2. Free use of electronic components

3. There is an environment where image recognition AI can be built

在完成了車輛的基本雛形後，我們挑選符合我們要求的控制器，經過討論我們對控制器的要求有以下：

1.有控制GPIO的訊號

2.能自由使用電子元件

3.有能架設影像辨識AI的環境

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220911_120738.jpg" width="400" height="300">

*****
**Date：** 2022/6/30

**Members：** LIN,ZHONG-BIN

**Content：**

(Google翻譯)

Today we installed the 12V battery on the vehicle and adjusted the output voltage of the step-down circuit board to 5V. After the installation of the battery, we will test the rotation function and drive motor function of the vehicle. After testing, it is found that the battery will be thrown out of the vehicle during the driving process, which may cause danger. So we thought that we can use a devil felt to fix the battery in the vehicle. On the vehicle, the devil felt can not only fix the battery but also unplug the battery for charging at any time.

今天我們將12V電池安裝上車輛，並將降壓電路板的輸出電壓調整為5V。完成電池的安裝後接著測試車輛的轉功能與驅動馬達功能，經過測試後發現，車輛在行駛過程中電池會被甩出車輛外，導致可能發生危險，於是我們想到可以用魔鬼氈將電池固定在車輛上，魔鬼氈不僅可以固定電池也可以隨時將電池拔下來充電。

<img src= "https://user-images.githubusercontent.com/106851896/176991414-0866b49d-fd78-4443-be90-2231f7c6d430.jpg" width="400" height="300">

*****
**Date：** 2022/7/1 - 2022/7/10

**Members：**  LIN,ZHONG-BIN

**Content：**

(Google翻譯)

After completing the battery installation, we started the circuit configuration of the vehicle and the hardware settings of the Donkey car. During the process of using the Donkey car, we learned that the Donkey Car is an open source project, and the hardware configuration of the vehicle can be freely developed and created. software.

在完成架設電池的部分之後，我們就開始車輛的電路配置與Donkey car硬體設置，在使用Donkey car過程中時得知Donkey Car是一項開源專案，車輛的硬體配置可以自由開發與創造的軟體。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E7%B7%9A%E8%B7%AF.jpg.png" width="400" height="300">

*****
**Date：** 2022/7/16 - 2022/7/20

***Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

(Google翻譯)

We set up the Raspberry Pi and the Donker software environment. After the installation is completed, we adjust the rudder direction of the machine's turning. After the adjustment, we directly start the remote control model shooting site photo training. After the training, the model can run clockwise and counterclockwise independently. topic.

我們將樹莓派與Donker軟體環境架設，在架設完成以後調整機器轉彎的舵向，調整過後就直接開始進行遙控機型拍攝場地照片訓練，經過訓練後機型可以自主跑完順時針逆時針的題目。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220811_081727.jpg"  width="600" height="300">

*****
**Date：** 2022/7/24

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

(Google翻譯)

During training, the machine always paused for a while. At first, we thought it was caused by insufficient battery power or the motor. After changing the battery, it was the same. In the end, it was found that the Dupont line was too often causing the tire to get stuck.

在訓練的時候機器總是會頓一下頓一下的行始，一開始我們以為電池電量不足或是馬達導致，之後換過電池以後也是一樣，最後發現是杜邦線太常導致卡到輪胎。

*****
**Date：** 2022/7/26

**Members：**  LIN,ZHONG-BIN

**Content：**

(Google翻譯)

Since the Dupont line on our model is too chaotic, we will replace the Dupont line before going home after training today and re-cut the line to avoid damage to the model when the machine is running.

由於我們機型上面的杜邦線過於混亂，所以我們今天訓練完以後在回家之前把杜邦線都換掉重新剪線整理，避免機型在行駛過程中杜邦線太長勾到其他物品導致損毀。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220810_102902.jpg" width="600" height="300">

*****
**Date：** 2022/7/28

**Members：**  LIN,ZHONG-BIN

**Content：**

(Google翻譯)

Since we are going to compete in the Central Division tomorrow, in order to prevent us from making mistakes during the game, we do not know how to record the video and cause disqualification, so we conducted a small simulation game today to train us how to avoid the possible encounters in the game. The problem.

由於我們明天就要比中區賽了，為了避免我們在比賽過程中不知道該怎麼錄影出現錯誤，導致失格，所以我們今天進行了一場小型的模擬賽，訓練我們如何避免比賽中可能會遇到的問題。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/S__6086661.jpg" width="500" height="400">

*****
**Date：** 2022/7/29 - 2022/7/30

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

(Google翻譯)

Today is the Central Division Competition. Like last year's Central Division Competition, the competition starts from 12:00 noon to 12:00 noon the next day. It is a pity that this year, compared with last year, there are fewer good topics this year than last year's. We've been waiting for the shortest path since the race started, and it didn't appear until 6am the next morning.

今天是中區賽，跟去年中區賽一樣從中午12點比到隔天中午的12點為止，今年很可惜的是跟去年相比，今年較好的題目比去年的還要少。我們自從比賽開始就一直在等最短路徑，直到隔天的早上6點才出現最短路徑。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/2022-08-15%20142636.png" width="700" height="400">

*****
**Date：** 2022/8/2 - 2022/8/7

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

(Google翻譯)

After the end of the central competition, we began to prepare for the detection of dodging blocks in the national competition. In the past few days, we randomly placed the blocks from far, middle, and near to take 70 photos each, and then exported them to the computer. Type color identification.

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


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220903_100640.jpg" width="450" height="300">

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

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/113502.png" width="400" height="500">

*****
**Date：** 2022/8/26

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

***Content：**

(Google翻譯)

Today is the day of the WRO National Finals. The competition time is the qualifying rounds in the morning and the finals in the afternoon. Before the finals start, we have to compete in the qualifying rounds before the finals in the afternoon. After the two qualifying rounds, the results are not very satisfactory. But we still made it to the finals. We ran very smoothly in the first race and got a full score, but in the second race, the machine did not turn enough when the red obstacle was flashing, and the red was knocked out, resulting in no second race. Full marks, but we still managed to win the first place and advance to the World Championship.

今天是WRO全國總決賽的日子，比賽時間上午為資格賽則下午比決賽，在比決賽開始之前我們要先比資格賽才能比下午的決賽，在兩趟資格賽跑完以後雖然成績不是很理想，但還是有進入決賽，我們第一場跑得很順利跑出了滿分的成績，但是在跑第二場時機器在閃紅色障礙物時轉彎轉的不夠大把紅色撞出來了導致第二場沒有滿分，但我們還是有驚無險的拿下第一名晉級世界賽。
<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/0910.png" width="1000" height="120">

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/82627.jpg" width="400" height="300"> <img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/S__69804048.jpg" width="400" height="300">

*****
**Date：** 2022/9/3 - 2022/9/4

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

In order to get a good ranking in the World Championship, we decided to increase the speed of the model, so we re-soldered the circuit board to a smaller size to save unnecessary space, and then shortened the length of the model so that the model can be More flexible turning and dodging obstacles.

為了能夠在世界賽中拿到好的名次，所以我們決定要將機型的速度提升，所以我們把電路板重新焊小一點節省不必要的空間，再把機型的長度縮短這樣機型就能夠更靈活的轉彎與閃避障礙物。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220904_111012.jpg" width="600" height="400">

*****
**Date：** 2022/9/7 - 2022/9/8

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

After we changed the mechanism to a smaller size, the sensors and prune pie on the model have to be rearranged. Since the previous model was larger, the line was longer. Changing the previous line to the model with a small table would cause problems. If the wire is too long, it will hook the wheel and block the lens, so we cut the wire and rewind it.

我們將機構改小以後，機型上的感測器與樹梅派都要重新擺放，由於之前的機型比較大所以線比較長，把之前的線換到小台的機型上會因為線太長會勾到輪子擋到鏡頭，所以我們重新剪線繞線。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6426.JPG" width="400" height="300">

*****
**Date：** 2022/9/10

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

When we practiced today, I don't know why the prune pie keeps restarting. We suspected the problem with the Dupont wires, so we removed the Dupont wires one by one and re-checked them. When we have checked all the Dupont wires, they are not damaged. , but still couldn't find the problem, and then checked it again, only to find that the servo motor was burned out, and it was normal after we replaced a servo motor.

今天我們練習時不知為何樹梅派一直重新開機，我們懷疑是杜邦線的問題，所以就把杜邦線一條一條的拆下來重新檢查，當我們已經把所有的杜邦線都檢查過一遍了都沒有損壞，卻始終找不到問題出在哪，之後又重新檢查了一遍，才發現是伺服馬達燒掉了，我們重新換過一顆伺服馬達以後就正常了。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6422.JPG" width="450" height="300">

*****
**Date：** 2022/9/11

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

(Google翻譯)

After the broken servo motor was replaced, there was no further error during the test. After several days of revisions, the model was finally able to run the entire process flawlessly.

將壞掉的伺服馬達換掉了以後，在測試時也沒有再發生過任何一個失誤，經過這幾天的修改以後終於能夠完整的讓機型完美無誤跑完全程。
