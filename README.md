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

## 車輛介紹

我們車輛主體使用3mm的木板經過雷射切割機切割後作成車輛的底盤，並搭配樂高零件設計轉向機構，使機器體積更小更堅固。樹梅派4不僅運算速度快，也適合用來影像辨識，所以選擇樹梅派4作為我們車輛的控制器。

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

# 車輛結構介紹
## 差速器

In order to solve the problem that the path taken by the outer wheels is larger than the path taken by the inner wheels when turning, we install a differential.

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1749.JPG" width="400" height="300">


## 轉向機構

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

Condering that the GA25-370 needs a total 12 of operating voltage, we set up a L298n Dc Motor Drive to control the movement of the GA25-370 Dc Gear Motor. On the other hand, L298n needs a external power supply. So we 
考慮到GA25-370需要12v的工作電壓，我們安裝L298n直流馬達控制板控制GA25-370直流馬達的動作。因為L298n直流馬達控制板需外接電源，所以我們製作了一個12v的鋰電池連接到L298n直流馬達控制板的線。

<img src= "https://user-images.githubusercontent.com/106851896/176989980-82d65ada-de48-4de4-8b35-44c4a550eb33.jpg" width="400" height="300">

*****
**Date：** 2022/6/12

**活動成員：** LIN,ZHONG-BIN

**Content：**

今天我們將12V電池安裝上車輛，並將降壓電路板的輸出電壓調整為5V。完成電池的安裝後接著測試車輛的轉功能與驅動馬達功能，經過測試後發現，車輛在行駛過程中電池會被甩出車輛外，導致可能發生危險，於是我們想到可以用魔鬼氈將電池固定在車輛上，魔鬼氈不僅可以固定電池也可以隨時將電池拔下來充電。

<img src= "https://user-images.githubusercontent.com/106851896/176991414-0866b49d-fd78-4443-be90-2231f7c6d430.jpg" width="400" height="300">

*****
**Date：** 2022/6/16 - 2022/6/17

**Members：** LIN,ZHONG-BIN

**Content：**

起初我們選擇使用MG996R伺服馬達用來驅動轉向機構，我們發現我們安裝於轉向機構上的MG996R伺服馬達雖然扭力大，但重量較重馬達的旋轉速度太慢，導致車輛沒辦法快速轉彎而撞牆，後來我們選擇使用SG90S伺服馬達，SG90S伺服馬達旋轉速度快而且體積也更小，逞車輛可以更容易通過彎道。

<img src= "https://user-images.githubusercontent.com/106851896/178086536-d1ad5c58-ee7f-4514-9b3d-6e2d4f79cfdf.jpg" width="400" height="300"> <img src= "https://user-images.githubusercontent.com/106851896/178086538-f11aecf4-af52-4141-a643-7ee231f0d225.jpg" width="400" height="300">

*****
**Date：** 2022/6/18 - 2022/6/19

**Members：**  LIN,ZHONG-BIN

**Content：**

由於我們車輛更換轉向機構上的伺服馬達，我們必須重新設計機構讓SG90S伺服馬達可以安裝於車輛上。我們將SG960S伺服馬達共訂在車輛的第二層中，更方便讓轉向機構連接，轉向機構運作起來更順暢。

<img src= "https://user-images.githubusercontent.com/106851896/178087399-1efc9875-dcfc-4141-bd51-6f2f8170cec8.PNG" width="550" height="300">

*****
**Date：** 2022/6/22

**Members：** LIN,ZHONG-BIN

**Content：**

車輛安裝完直流馬達與伺服馬達後，車輛剩下控制器尚未安裝，而控制器我們選擇使用樹梅派4，之所以選擇使用樹梅派4是因為，樹梅派4城市運算效能高體積小，更適合用來ˊ做影像辨識功能。我們將樹梅派4安裝於第三層位置，將樹梅派與第三能的3mm木板用裸絲固定起來。

*****
**Date：** 2022/6/24 - 2022/6/26

**Members：**  LIN,ZHONG-BIN

**Content：**

我們將三層板子整合在一起，測量每層板子和元件的高度，選用高度合適的絕緣柱，並利用絕緣柱將三層板子縱向的固定在一起，形成車輛的基本雛形。

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6428.JPG" width="400" height="300">

*****
**Date：** 2022/6/28 - 2022/6/29

**Members：**  LIN,ZHONG-BIN

**Content：**
在完成了車輛的基本雛形後，我們挑選符合我們要求的控制器，經過討論我們對控制器的要求有以下：

1.有控制GPIO的訊號

2.能自由使用電子元件

3.有能架設影像辨識AI的環境

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220911_120738.jpg" width="400" height="300">

*****
**Date：** 2022/6/30

**Members：**  LIN,ZHONG-BIN

**Content：**

若控制器有能架設影像辨識AI的環境，那控制器勢必會是微電腦。考慮到這些條件，我們選擇樹梅派作為我們的車輛的控制器，且樹梅派有GPIO的腳位可以控制墊子元件。

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220911_122648.jpg" width="400" height="300">

*****
**Date：** 2022/7/1 - 2022/7/10

**Members：**  LIN,ZHONG-BIN

**Content：**

在完成架設電池的部分之後，我們就開始車輛的電路配置與Donkey car硬體設置，在使用Donkey car過程中時得知Donkey Car是一項開源專案，車輛的硬體配置可以自由開發與創造的軟體。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E7%B7%9A%E8%B7%AF.jpg.png" width="400" height="300">

*****
**Date：** 2022/7/16 - 2022/7/20

***Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

我們將樹莓派與Donker軟體環境架設，在架設完成以後調整機器轉彎的舵向，調整過後就直接開始進行遙控機型拍攝場地照片訓練，經過訓練後機型可以自主跑完順時針逆時針的題目。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220811_081727.jpg"  width="600" height="300">

*****
**Date：** 2022/7/24

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

在訓練的時候機器總是會頓一下頓一下的行始，一開始我們以為電池電量不足或是馬達導致，之後換過電磁以後也是一樣，最後發現是杜邦線太常導致卡到輪胎。

*****
**Date：** 2022/7/26

**Members：**  LIN,ZHONG-BIN

**Content：**

由於我們機型上面的杜邦線過於混亂，所以我們今天訓練完以後在回家之前把杜邦線都換掉重新剪線整理，避免機型在行駛過程中杜邦線太長勾到其他物品導致損毀。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220810_102902.jpg" width="600" height="300">

*****
**Date：** 2022/7/28

**Members：**  LIN,ZHONG-BIN

**Content：**
  
由於我們明天就要比中區賽了，為了避免我們在比賽過程中不知道該怎麼錄影出現錯誤，導致失格，所以我們今天進行了一場小型的模擬賽，訓練我們如何避免比賽中可能會遇到的問題。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/S__6086661.jpg" width="500" height="400">

*****
**Date：** 2022/7/29 - 2022/7/30

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

今天是中區賽，跟去年中區賽一樣從中午12點比到隔天中午的12點為止，今年很可惜的是跟去年相比，今年較好的題目比去年的還要少。我們自從比賽開始就一直在等最短路徑，直到隔天的早上6點才出現最短路徑。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/2022-08-15%20142636.png" width="700" height="400">

*****
**Date：** 2022/8/2 - 2022/8/7

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG

**Content：**

中區賽結束以後，我們就開始準備全國賽閃避積木的偵測，這幾天我們將積木由遠、中、近分別隨機擺放各拍70張照片，在匯出到電腦中框選進行圖型顏色的辨識。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/156.jpg" width="500" height="300">

*****
**Date：** 2022/8/9

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

經過一系列的測試過後，由於我們的技術尚未成熟所以用來辨識有點困難，所以我們目前決定要改用HLS偵測積木的色相、飽和度、亮度，這樣誤測的機率比較低。


<img src =  "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E6%93%B7%E5%8F%96.PNG"  width="500" height="300">

*****
**Date：** 2022/8/12

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

由於我們鏡頭買錯，我們原本該用有紅外線濾鏡無夜視功能的鏡頭，結果我們買到無紅外線濾鏡有夜視功能的鏡頭，所以我們平常跑的過程中無法把太陽光濾掉所以跑起來不是很理想。

<img src ="https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220815_103756.jpg" width="600" height="300">

*****
**Date：** 2022/8/15

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

今天我們近乎把官方出的所有障礙物組合辨識完畢，另外我們還有重新編排出題，但是在測試過程中還是會出現鏡頭誤測的問題，需要再進行微調。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/0.1.png" width="400" height="500">

*****
**Date：** 2022/8/18

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

在機型跑的過程中鏡頭總是誤測或是沒有測到積木直接繞過去，所以我們加入了超音波偵測是否有障礙物，在測試了一段時間才知道鏡頭有偵測到障礙物只是反應不及所以沒有閃避。


<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220903_100640.jpg" width="450" height="300">

*****
**Date：** 2022/8/20

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

今天我們發現鏡頭會誤測多半是機型裝法的問題，所以我們就把鏡頭往後裝，順便把機型上的感測器換過位置後，再把線重繞以後鏡頭誤測的問題改善了很多。


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220903_100536.jpg" width="600" height="300">

*****
**Date：** 2022/8/24

**Members：** LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

鏡頭換過位置以後基本上已經沒有其他太大的失誤，但還是會有機型轉太大導致差到障礙物，在解決問題以後我們就要開始準備去台北的備用零件。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/113502.png" width="400" height="500">

*****
**Date：** 2022/8/26

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

***Content：**

今天是WRO全國總決賽的日子，比賽時間上午為資格賽則下午比決賽，在比決賽開始之前我們要先比資格賽才能比下午的決賽，在兩趟資格賽跑完以後雖然成績不是很理想，但還是有進入決賽，我們第一場跑得很順利跑出了滿分的成績，但是在跑第二場時機器在閃紅色障礙物時轉彎轉的不夠大把紅色撞出來了導致第二場沒有滿分，但我們還是有驚無險的拿下第一名晉級世界賽。
<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/0910.png" width="1000" height="120">

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/82627.jpg" width="400" height="300"> <img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/S__69804048.jpg" width="400" height="300">

*****
**Date：** 2022/9/3 - 2022/9/4

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**
為了能夠在世界賽中拿到好的名次，所以我們決定要將機型的速度提升，所以我們把電路板重新焊小一點節省不必要的空間，再把機型的長度縮短這樣機型就能夠更靈活的轉彎與閃避障礙物。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_20220904_111012.jpg" width="600" height="400">

*****
**Date：** 2022/9/7 - 2022/9/8

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

我們將機構改小以後，機型上的感測器與樹梅派都要重新擺放，由於之前的機型比較大所以線比較長，把之前的線換到小台的機型上會因為線太長會勾到輪子擋到鏡頭，所以我們重新剪線繞線。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6426.JPG" width="400" height="300">

*****
**Date：** 2022/9/10

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

今天我們練習時不知為何樹梅派一直重新開機，我們懷疑是杜邦線的問題，所以就把杜邦線一條一條的拆下來重新檢查，當我們已經把所有的杜邦線都檢查過一遍了都沒有損壞，卻始終找不到問題出在哪，之後又重新檢查了一遍，才發現是伺服馬達燒掉了，我們重新換過一顆伺服馬達以後就正常了。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6422.JPG" width="450" height="300">

*****
**Date：** 2022/9/11

**Members：**  LIN,ZHONG-BIN、LIN,BO-SHENG、LI,DING-WEI

**Content：**

將壞掉的伺服馬達換掉了以後，在測試時也沒有再發生過任何一個失誤，經過這幾天的修改以後終於能夠完整的讓機型完美無誤跑完全程。
