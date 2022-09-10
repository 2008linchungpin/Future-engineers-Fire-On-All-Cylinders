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

**Team Photo**

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1738.JPG" width="400" height="300">


**Team Funny Photo**

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_1740.JPG" width="400" height="300">

**YouTube URL**

https://reurl.cc/W18Wl9

<img src= "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/sddefault.jpg" width="400" height="300">


## Introduces of Electromechanical Components

GA25-371 Dc Gear Motor：Drives the rear wheels of the vehicle in order to control it move forward and backward.

MG90S-Metal Gear Micro Servo Motor：Force the mechanical structure to let the vehicle turn.

Lithium Polymer：Provides electricities for the Raspberry and other electromechanical components.

L293D Motor Driver: Controls GA25-371 Dc Gear Motor to turn clockwise, conterclockwise, and alter the direction of it.

ADIO-DC36V5A Switching Power Adapter：Stable the electricity that the lithium polymer provides

jmdo.96c OLED display：To show some specific numerical data of the Raspberry.

Tcs34725 RGB Color Sensor：To dectect lines and calculate the laps the vehicle had passed.

Raspberry pi Camera (G)：Images collecting and identifying.

Raspberry Pi 4：In charge of all the models of vehicle controllers.

## Diary Log

**Date：** 2022/6/4

**Members：** 林仲斌

**Content：**

After reading the rule of the competition, we figured out some materials and electromachanical components that were needed when constructing the outline of the car and the its structure design. We also got to think about how to use only one piece of Dc Gear Motor to drive the vehicle and to assemble the fundamental model of the turning section.

<img src= "https://user-images.githubusercontent.com/106851896/176984877-f74ac4e4-97b1-49e1-bfa5-84112426c236.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176984586-d9094acf-c13c-4dc4-bf20-022f951bf5ed.jpg" width="400" height="300"><br/>

*****
**紀錄日期：** 2022/6/5 - 2022/6/7

**活動成員：** 林仲斌 

**工作內容：**

During these days, we started to design the construction of the vehicle. Dividing it into three straight layers, we put the necessary components onto it. With the help of Onshape and the laser beam cutting machine, we can easily draw the outline of the automobile and then cut the plank into the shape we needed so as to build the carbody structural member. 

<img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220807_102434.jpg" width="600" height="300"><img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E4%B8%8B.png" width="250" height="300">


*****
**紀錄日期:** 2022/6/8 - 2022/6/10 

**活動成員：** 林仲斌

**工作內容：**

Confirming the car's shape, we started off to choose the motors. For now we have GA25-370 in hand, and while checking some datasheets one the internet, we bought some JGA16-050 because it's much lighter and was not as large the GA25-370. But in spite of the advantages of JGS16-050, we still ultilized GA25-370 for driving the vehicle after practical comparasions due to the efficiency they provided.

<img src= "https://user-images.githubusercontent.com/106851896/176989086-27531ee9-5cdb-40cb-8e0b-7d376ba59e3e.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176989089-816688a2-115c-4d20-a689-e17af9d53a5a.jpg" width="400" height="300"><br/>

*****
**紀錄日期:** 2022/6/11

**活動成員：** 林仲斌

**工作內容：**

Condering that the GA25-370 needs a total 12 of operating voltage, we 
考慮到GA25-370需要12v的工作電壓，我們安裝L298n直流馬達控制板控制GA25-370直流馬達的動作。因為L298n直流馬達控制板需外接電源，所以我們製作了一個12v的鋰電池連接到L298n直流馬達控制板的線。

<img src= "https://user-images.githubusercontent.com/106851896/176989980-82d65ada-de48-4de4-8b35-44c4a550eb33.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/6/12

**活動成員：** 林仲斌

**工作內容：**

今天我們在車輛中層找了一個用於放置鋰電池位置，那個位置的大小正好可以放一個鋰電池在裡面。雖然我們所準備的位置與鋰電池的大小是符合的，但是在我們模擬車輛行駛的過程中，我們發現鋰電池很容易從車輛上滑落，所以我們用魔鬼氈束帶把鋰電池綑綁在車輛上。

<img src= "https://user-images.githubusercontent.com/106851896/176991414-0866b49d-fd78-4443-be90-2231f7c6d430.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/6/16 - 2022/6/17

**活動成員：** 林仲斌

**工作內容：**

我們開始選擇控制車輛轉向的伺服馬達，考慮到車輛的轉向需要較大的力量，我們選用扭力較大的MG996R為控制車輛轉向的伺服馬達。MG996R的重量太重和尺寸大導致影響到車輛的結構。因MG996R存在這些問題，我們將MG996R替換成重量較輕尺寸較小的MG90S。

<img src= "https://user-images.githubusercontent.com/106851896/178086536-d1ad5c58-ee7f-4514-9b3d-6e2d4f79cfdf.jpg" width="400" height="300"> <img src= "https://user-images.githubusercontent.com/106851896/178086538-f11aecf4-af52-4141-a643-7ee231f0d225.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/6/18 - 2022/6/19

**活動成員：** 林仲斌

**工作內容：**

在選定伺服馬達後，我們開始在設計MG90S在車輛上的固定，因為當MG90S固定在車體第二層時高度正好符合MG90S控制轉向機構所需的高度，因此我們將第二層的設計圖改為可以固定MG90S的設計。

<img src= "https://user-images.githubusercontent.com/106851896/178087399-1efc9875-dcfc-4141-bd51-6f2f8170cec8.PNG" width="550" height="300">

*****
**紀錄日期:** 2022/6/22

**活動成員：** 林仲斌

**工作內容：**

完成了GA25-370和MG90S的安裝後，我們的車輛結構就已經差不多定型了，也就可以知道我們的車輛大概是長什麼樣子。第一層板子安裝GA25-370驅動的後輪驅動結構和前輪轉向機構；第二層板子安裝鋰電池和控制前輪轉向機構的MG90S；第三層板子我們計畫我們將會安裝車輛的主要控制器。

<img src= "https://user-images.githubusercontent.com/106851896/178095123-246d669c-eba8-4565-8163-6c9fec77631e.jpg" width="400" height="300"> <img src= "https://user-images.githubusercontent.com/106851896/178095288-702f8c3b-1e6e-4c7c-b58e-0acd271287a4.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/6/24 - 2022/6/26

**活動成員：** 林仲斌

**工作內容：**

我們將三層板子整合在一起，測量每層板子和元件的高度，選用高度合適的絕緣柱，並利用絕緣柱將三層板子縱向的固定在一起，形成車輛的基本雛形。

*****
**紀錄日期:** 2022/6/28 - 2022/6/29

**活動成員：** 林仲斌

**工作內容：**

在完成了車輛的基本雛形後，我們挑選符合我們要求的控制器，經過討論我們對控制器的要求有以下：

1.有控制GPIO的訊號

2.能自由使用電子元件

3.有能架設影像辨識AI的環境

*****
**紀錄日期:** 2022/6/30

**活動成員：** 林仲斌

**工作內容：**

若控制器有能架設影像辨識AI的環境，那控制器勢必會是微電腦。考慮到這些條件，我們選擇樹梅派作為我們的車輛的控制器，且樹梅派有GPIO的腳位可以控制墊子元件。

*****
**紀錄日期:** 2022/7/1 - 2022/7/10

**活動成員：** 林仲斌

**工作內容：**

在完成架設電池的部分之後，我們就開始車輛的電路配置與Donkey car硬體設置，在使用Donkey car過程中時得知Donkey Car是一項開源專案，車輛的硬體配置可以自由開發與創造的軟體。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E7%B7%9A%E8%B7%AF.jpg.png" width="400" height="300">

*****
**紀錄日期:** 2022/7/16 - 2022/7/20

**活動成員：** 林仲斌、林柏盛

**工作內容：**

我們將樹莓派與Docker軟體環境架設，在架設完成以後調整機器轉彎的舵向，調整過後就直接開始進行遙控機型拍攝場地照片訓練，經過訓練後機型可以自主跑完順時針逆時針的題目。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220811_081727.jpg"  width="600" height="300">

*****
**紀錄日期:** 2022/7/26

**活動成員：** 林仲斌

**工作內容：**
由於我們機型上面的杜邦線過於混亂，所以我們今天訓練完以後在回家之前把杜邦線都換掉重新剪線整理，避免機型在行駛過程中杜邦線太長勾到其他物品導致損毀。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220810_102902.jpg" width="600" height="300">

*****
**紀錄日期:** 2022/7/28

**活動成員：** 林仲斌

**工作內容：**
  
由於我們明天就要比中區賽了，為了避免我們在比賽過程中不知道該怎麼錄影出現錯誤，導致失格，所以我們今天進行了一場小型的模擬賽，訓練我們如何避免比賽中可能會遇到的問題。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/S__6086661.jpg" width="500" height="400">

*****
**紀錄日期:** 2022/7/29 - 2022/7/30

**活動成員：** 林仲斌、林柏盛

**工作內容：**

今天是中區賽，跟去年中區賽一樣從中午12點比到隔天中午的12點為止，今年很可惜的是跟去年相比，今年較好的題目比去年的還要少。我們自從比賽開始就一直在等最短路徑，直到隔天的早上6點才出現最短路徑。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/2022-08-15%20142636.png" width="700" height="400">

*****
**紀錄日期:** 2022/8/2 - 2022/8/7

**活動成員：** 林仲斌、林柏盛

**工作內容：**

中區賽結束以後，我們就開始準備全國賽閃避積木的偵測，這幾天我們將積木由遠、中、近分別隨機擺放各拍70張照片，在匯出到電腦中框選進行圖型顏色的辨識。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/156.jpg" width="500" height="300">

*****
**紀錄日期:** 2022/8/9

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

經過一系列的測試過後，由於我們的技術尚未成熟所以用來辨識有點困難，所以我們目前決定要改用HLS偵測積木的色相、飽和度、亮度，這樣誤測的機率比較低。


<img src =  "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E6%93%B7%E5%8F%96.PNG"  width="500" height="300">

*****
**紀錄日期:** 2022/8/12

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

由於我們鏡頭買錯，我們原本該用有紅外線濾鏡無夜視功能的鏡頭，結果我們買到無紅外線濾鏡有夜視功能的鏡頭，所以我們平常跑的過程中無法把太陽光濾掉所以跑起來不是很理想。

<img src ="https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220815_103756.jpg" width="600" height="300">

*****
**紀錄日期:** 2022/8/15

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

今天我們近乎把官方出的所有障礙物組合辨識完畢，另外我們還有重新編排出題，但是在測試過程中還是會出現鏡頭誤測的問題，需要再進行微調。

<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/0.1.png" width="400" height="500">

*****
**紀錄日期:** 2022/8/20

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

今天我們發現鏡頭會誤測多半是機型裝法的問題，所以我們就把鏡頭往後裝，順便把機型上的感測器換過位置後，再把線重繞以後鏡頭誤測的問題改善了很多。


<img src = "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220903_100536.jpg" width="600" height="300">


*****
**紀錄日期:** 2022/8/26

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

今天是WRO全國總決賽的日子，比賽時間上午為資格賽則下午比決賽，在比決賽開始之前我們要先比資格賽才能比下午的決賽，在兩趟資格賽跑完以後雖然成績不是很理想，但還是有進入決賽，我們第一場跑得很順利跑出了滿分的成績，但是在跑第二場時機器在閃紅色障礙物時轉彎轉的不夠大把紅色撞出來了導致第二場沒有滿分，但我們還是有驚無險的拿下第一名晉級世界賽。
<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/0910.png" width="1000" height="120">

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/82627.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/9/3 - 2022/9/4

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

為了能夠在世界賽中拿到好的名次，所以我們決定要將機型的速度提升，所以我們把電路板重新焊小一點節省不必要的空間，再把機型的長度縮短這樣機型就能夠更靈活的轉彎與閃避障礙物。

<img src = "https://github.com/2008linchungpin/Future-engineers-Fire-On-All-Cylinders/blob/main/photo/IMG_6426.JPG" width="400" height="300">
