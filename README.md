# 为什么要做这个
某天在B站使用各种关键词搜索频谱图的时候突然发现了这个视频：

https://www.bilibili.com/video/av22527845

第一遍看完觉得很有道理。之后一想感觉不对啊，既然信息都是对具体事物的抽象，那么任何信息都是可以相互转换的。

所以只要用点标记出没有声音的部分就可以了，就像这样：

https://www.bilibili.com/video/av39185094

比如A的电码是·-，用点标记间隔就可以写成·· ·

还可以用··表示-

以此类推：

| 字母 | morse code | tap code |tap code 2 |
| ------ | ------ | ------ | ------ |
| A|  ·－  |    ·· ·| · ·· |
| B|  －···  |    · ···· | ·· · · · |
| C|  －·－·  |    · ·· ·· | ·· · ·· · |
| D|  －··  |    · ···| ·· · · |
| E|  ·   |   ··| · |
| F|  ··－·  |    ··· ··  | · · ·· · |
| G|  －－·  |    · · ··| ·· ·· · |
| H|  ····  |    ·····| · · · · |
| I|  ··   |   ···| · · |
| J|  ·－－－ |     ·· · · · | · ·· ·· ·· |
| K|  －·－  |    · ·· ·| ·· · ·· |
| L|  ·－··  |    ·· ···| · ·· · · |
| M|  －－ |     · · ·| ·· ·· |
| N|  －·  |    · ··| ·· · |
| O|  －－－  |    · · · ·| ·· ·· ·· |
| P|  ·－－·  |    ·· · ··| · ·· ·· · |
| Q|  －－·－  |    · · ·· ·| ·· ·· · ·· |
| R|  ·－·   |   ·· ··| · ·· · |
| S|  ···   |   ····| · · · |
| T|  －  |    · ·| ·· |
| U|  ··－  |    ··· ·|· · ··  |
| V|  ···－  |    ···· ·| · · · ·· |
| W|  ·－－  |    ·· · ·| · ·· ·· |
| X|  －··－  |    · ··· ·| ·· · · ·· |
| Y|  －·－－  |    · ·· · ·| ·· · ·· ·· |
| Z|  －－··  |    · · ···| ·· ·· · · |
| 0|  －－－－－  |    · · · · · ·| ·· ·· ·· ·· ·· ·· |
| 1|  ·－－－－ |     ·· · · · ·| · ·· ·· ·· ·· |
| 2|  ··－－－ |     ··· · · ·| · · ·· ·· ·· |
| 3|  ···－－ |     ···· · ·| · · · ·· ·· |
| 4|  ····－ |     ····· ·| · · · · ·· |
| 5|  ·····  |    ······| · · · · · |
| 6|  －···· |     · ·····| ·· · · · · |
| 7| －－···  |    · · ····| ·· ·· · · · |
| 8| －－－··  |    · · · ···| ·· ·· ·· · · |
| 9| －－－－· |     · · · · ··| ·· ·· ·· ·· · |


tapcode这个名字来自这里：

http://gadgetzz.com/2016/01/01/part-two-of-the-creepy-puzzle-11b-3-1369/

"The tapping sound that can be heard has also been identified as ‘tap code’. It has been used as a way for prisoners to communicate between cells."

在B站找频谱图的时候不小心发现了关键词“11B-X-1371”，一顿Google之后又发现了关键词“tap code”。既然都是用点传递信息那就借用一下吧。

# How To Use
### tapcode.py
If you want translate words, input:  
python3 tapcode.py nyanya~  
The Terminal will return:  
<p>· ··/· ·· · ·/·· ·/· ··/· ·· · ·/·· ·/~</p>    

Or translate sentence, input:  
python3 tapcode.py "author by firedom"  
The Terminal will return:  
<p>·· ·/··· ·/· ·/·····/· · · ·/·· ··/ /· ····/· ·· · ·/ /··· ··/···/·· ··/··/· ···/· · · ·/· · ·/</p>  

### IR.py
If you want translate words, input:  
python3 IR.py "· ··/· ·· · ·/·· ·/· ··/· ·· · ·/·· ·/~" 
The Terminal will return:  
<p>nyanya~</p>    

Or translate sentence, input:  
python3 IR.py "·· ·/··· ·/· ·/·····/· · · ·/·· ··/ /· ····/· ·· · ·/ /··· ··/···/·· ··/··/· ···/· · · ·/· · ·/"  
The Terminal will return:  
<p>author by firedom</p>  

oooolu
