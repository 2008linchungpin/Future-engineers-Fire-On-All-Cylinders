# Fire-On-All-Cylinders

## Introduces of Electromechanical Components

GA25-371 Dc Gear Motor：Drives the rear wheels of the vehicle in order to control it move forward and backward.

MG90S-Metal Gear Micro Servo Motor：Force the mechanical structure to let the vehicle turn.

Lithium Polymer：Provides electricities for the Raspberry and other electromechanical components.

L293D Motor Driver: Controls GA25-371 Dc Gear Motor to turn clockwise, conterclockwise, and alter the direction of it.

ADIO-DC36V5A Switching Power Adapter：Stable the electricity that the lithium polymer provides

jmdo.96c OLED display：To show some specific numerical data of the Raspberry.

Tcs34725 RGB Color Sensor：To dectect lines and calcualte the laps the vehicle had passed.

Raspberry pi Camera (G)：Images collecting and identifying.

Raspberry Pi 4：In charge of all the models of vehicle controllers.

## Diary Log

**Date：** 2022/6/4

**Members：** 林仲斌

**Content：**

After reading the rule of the competition, we figure out some materials and electromachanical components that is needed when constructing the outline of the car and 
我們閱讀比賽規則，根據規則對車輛的限制，和會用到的功能，構思製造車輛所需的器材、元件和車輛的結構設計。思考要如何只使用一顆直流馬達驅動車輛以及製作轉向結構基本雛型。

<img src= "https://user-images.githubusercontent.com/106851896/176984877-f74ac4e4-97b1-49e1-bfa5-84112426c236.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176984586-d9094acf-c13c-4dc4-bf20-022f951bf5ed.jpg" width="400" height="300"><br/>

*****
**紀錄日期：** 2022/6/5 - 2022/6/7

**活動成員：** 林仲斌 

**工作內容：**

這幾天我們開始設計車體結構，為了有效的縮小車輛的尺寸，我們將車體分為直向的三層分別安裝所需的原件。我們用onshape繪製車體結構，並使用雷射切割機切割木板將車體結構切割出來組裝。

<img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/IMG_20220807_102434.jpg" width="600" height="300"><img src= "https://github.com/2008linchungpin/Future_Engineer/blob/main/photo/%E4%B8%8B.png" width="250" height="300">


*****
**紀錄日期:** 2022/6/8 - 2022/6/10 

**活動成員：** 林仲斌

**工作內容：**

在確認了車輛大概的形狀後，我們開始選擇驅動車輛的馬達，目前我們有的馬達有GA25-370，而在上網查詢資料後，我們也購入了JGA16-050，因為和GA25-370相比JGA16-050尺寸較小且重量也較輕。但在實際比較GA25-370和JGA16-050驅動車輛的效果後，我們決定選用GA25-370作為車輛的驅動馬達。

<img src= "https://user-images.githubusercontent.com/106851896/176989086-27531ee9-5cdb-40cb-8e0b-7d376ba59e3e.jpg" width="400" height="300">  <img src= "https://user-images.githubusercontent.com/106851896/176989089-816688a2-115c-4d20-a689-e17af9d53a5a.jpg" width="400" height="300"><br/>

*****
**紀錄日期:** 2022/6/11

**活動成員：** 林仲斌

**工作內容：**

考慮到GA25-370需要12v的工作電壓，我們安裝L298n直流馬達控制板控制GA25-370直流馬達的作動。因為L298n直流馬達控制板需外接電源，所以我們製作了一個12v的鋰電池連接到L298n直流馬達控制板的線。

<img src= "https://user-images.githubusercontent.com/106851896/176989980-82d65ada-de48-4de4-8b35-44c4a550eb33.jpg" width="400" height="300">

*****
**紀錄日期:** 2022/6/12

**活動成員：** 林仲斌

**工作內容：**

今天我們在車輛中層找了一個用於放置鋰電池位置，那個位置的大小正好可以放一個鋰電池在裡面。雖然我們所準備的位置與鋰電池的大小是符合的，但是在我們模擬車輛行駛的過程中，我們發現鋰電池很容易從車輛上滑落，所以我們用魔鬼沾束帶把鋰電池綑綁在車輛上。

<img src= "https://user-images.githubusercontent.com/106851896/176991414-0866b49d-fd78-4443-be90-2231f7c6d430.jpg" width="400" height="300">


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


*****
**紀錄日期:** 2022/9/3 - 2022/9/4

**活動成員：** 林仲斌、林柏盛、李鼎為

**工作內容：**

為了能夠在世界賽中拿到好的名次，所以我們決定要將機型的速度提升，所以我們把電路板重新焊小一點節省不必要的空間，再把機型的長度縮短這樣機型就能夠更靈活的轉彎與閃避障礙物。
