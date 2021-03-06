---
title: 文章：TEX PS PDF DVI 这些都是啥
date: 2020-04-28 16:06:19
tags: 计算机历史 $\LaTeX$
---

# TEX PS PDF DVI 这些都是啥

>碎碎念： <br/>
>啊哈，终于可以写一点关于计算机历史的东西了，我觉得挺开心的。之前也是咕咕咕了好久 233.<br>
>打算写完这一篇之后我去写写关于视频和音频的文章。-->大概要写模拟和数字视频还有模拟和数字音乐以及我喜欢的八比特。<br/>
>这篇文章主要介绍这几种跟打印相关的格式、语言，那么下一篇就介绍跟显示相关的格式和语言 (txt rtf doc html)<br/>

那我我们进入正题

## 0x00 .TEX

说到 $\LaTeX$ 或者 $\TeX$ 我们不得不提起先辈 Knuth 老先生。如果你的学科是物理或是数学，你可以膜拜 Newton 老先生，如果你的学科是化学，你可以膜拜 我也忘了是谁 先生，但是如果你的学科是 “计算机科学” 那么，你有可能会真的见到这个学科的 “神”. 说起来还是挺神奇的的一件事。

Tex 在 1977 年被 Knuth 发明。据说是因为他在写他那套著名的 *计算机程式设计艺术* 的时候觉得排版非常不方便，所以设计了 Tex 排版系统帮助他自己排版。最开始 Latex 只适用于他用的那台电脑和某种特定型号的打印机。早期的软件貌似兼容性都不是很好。

据说 Tex 是图灵完备的语言，所以可以把它作为一个编程语言来使用。我只对 Latex 的数学公式有一点点了解，所以这里不过多介绍了。

这里简单给几个数学公式的例子来看看。

```
\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0} \\
\nabla\cdot\vec{B} = 0 \\
\nabla\times\vec{E} = -\frac{\partial B}{\partial t} \\
\nabla\times\vec{B} = \mu_0\left(\vec{J}+\epsilon_0\frac{\partial E}{\partial t} \right)
```

$$
\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0} \\
\nabla\cdot\vec{B} = 0 \\
\nabla\times\vec{E} = -\frac{\partial B}{\partial t} \\
\nabla\times\vec{B} = \mu_0\left(\vec{J}+\epsilon_0\frac{\partial E}{\partial t} \right)
$$

麦克斯韦方程组，经典。

```
\sum _{1} ^{n} r^{2} = \frac{n(n+1)(2n+1)}{6}
```

$$
\sum _{1} ^{n} r^{2} = \frac{n(n+1)(2n+1)}{6}
$$

求和什么的也可以显示。我在书上能看到的数学符号 Latex 都能打出来。

## 0x01 .DVI

.DVI 是 device independent file. 这是一个最初用来处理打印文件的扩展名。因为一开始的时候，各家的打印机接受的文件格式是不一样的。1984 年通用电气发明了 dvi 格式的文件，之后 1988 年微软购买了这种文件格式。他经常和 latex 配合使用。现在互联网上还是挺难找到 dvi 格式的介绍的，如果找到更多的我会补充在这里。

我在网上看到了这个：DVI is TeX' own DeVice Independent format, it isn't understood outside the TeX world.

---

更新：看了 dvi 的维基百科，看来还是英文资料更全一些。

我觉得上面那个通用电气的 dvi 指的是 dvi 显示接口，这里说的 dvi 是高德纳在 1982 年发明的那个。这个 dvi 只能用来打印 tex 文件，而且他是人类不可读的（二进制文件）.dvi 和 ps、pdf 最大的区别就是 dvi 没有字体选择，但是 ps、pdf 是可以选择字体的。

## 0x02 .PS

.PS 是 Adobe 研发的图形设计语言。但是他和 Apple 的关系也很深。据说是 1985 年推出，最早用于 AppleLaserWriter, 我还看到有说是 1984 年推出的。所以基本上是和 DVI 差不多一样的时间推出的。和 DVI 一样，他的好处就是版面制作的时候不用考虑设备依赖，不用考虑你是啥打印机，也不用专门准备一台电脑来制作 ps 文档。

和 DVI 的背景类似，当时的打印机只能用来打印字符或者打印点阵，画图是用绘图仪实现的。网上很容易找到绘图仪的图片，还是挺酷的。点阵打印的话，问题就是分辨率太低，效果不好。为了打印排版良好的图片和文字，PS 应运而生。PS 可以生成矢量图，用的是类似海龟绘图的方法。而且 ps level2 还增加了对 jpeg 这样的图像以及更多字体的支持 （对亚洲国家很有必要）. 

PS 的好处就是 PS 是明文储存的，所以很容易查看。这里简单粘贴几行代码看：

```
%!PS-Adobe-3.0
%APL_DSC_Encoding: UTF8
%APLProducer: (Version 10.15.4 (Build 19E287) Quartz PS Context)
%%Title: （首发哦 i 围巾哦 i 啊我哈佛 i 啊我和佛教）
%%Creator: (Mail: cgpdftops CUPS filter)
%%CreationDate: (Tuesday, April 28 2020 16:44:42 CST)
.
. "⬆️开头的一些描述"
.
/rs/rectstroke
/f/fill
/f*/eofill
/sf/selectfont
/s/show
%/as/ashow
/xS/xshow
.
. "⬆️应该是定义宏"
.
/FunEval % val1 fundict -> comp1 comp2 ... compN
{
    begin
	% the value passed in is the base index into the table
	nRange mul /val xd	% compute the actual index to the table
				% since there are nRange entries per base index
	0 1 nRange 1 sub
	{
	    dup 2 mul/nDim2 xd % dim
	    val	% base value to use to do our lookup
	    add DataSource exch get %  lookedupval
	    mulRange nDim2 get mul 	% lookedupval*(ymax-ymin)/(xmax-xmin)
	    mulRange nDim2 1 add get % lookedupval*(ymax-ymin)/(xmax-xmin) ymin
	    add % interpolated result
	}for	% comp1 comp2 ... compN
    end
}bd
.
. "⬆️应该是定义函数"
.
/b 4 def
/c 5 def
/d 6 def
/e 7 def
/g 8 def
/h 9 def
/i 10 def
/l 11 def
/m 12 def
/n 13 def
/o 14 def
.
. "⬆️这些应该是描述页面怎么布局的，好像是分很多步骤，我认不出来，所以就随便粘贴一些"
.
h
f
ep
end
%%Trailer
%%Pages: 1
%%BoundingBox: 0 0 595 842
%%EOF
.
. "⬆️尾文件"
.
```

据说 ps 最早跟 Xerox 1976 年的激光打印机有关，不过我也不想研究太深了。

ps 大概是 1990 年左右式微的，有人说这跟当时廉价的喷墨打印机有关。那个时候，Adobe 又发明了 PDF 格式。

## 0x03 .PDF 

pdf 是我挺喜欢的一个格式，因为这个格式是通用的。在哪个设备上都一样。这个格式是 1993 年 Adobe 公司发明的。和 ps 不一样，pdf 是二进制文件和文本文件混合排列的，所以他的内容是人类不可读的。

我没找到很多关于 pdf 的有趣的事，所以这里简单介绍一下 pdf 文件的组成。

```
%PDF-1.3
%���������
4 0 obj
<< /Length 5 0 R /Filter /FlateDecode >>
.
. "⬆️这里是文件头，� 是二进制文件，读不出来。"
.
21 0 obj
<< /Length 22 0 R /Filter /FlateDecode >>
stream
x]��j�0E��
-�E��$N�PR^�A�~�-������,�����)tqG�;�GΎ�s�l��{�tKQ֙@�t	�dOg�D^Hcu����C�]�Hc�IV��2�@d�a��3����ނ��Y���-���i$�u-

h����n$�qt��m\�H���\<IL�D~IO�f�i
�;�����ө�̿R^^�p�Z�u�P�P���
���(�n�n�@�M�tPΖP -Su�<$}��Jnu�(��@�=W{(@���P �VJ���y�d(fap�$��%P��F~?=-=�}����/�O�Vl�?��R�y��
endstream
endobj
22 0 obj
.
. "⬆️中间基本都是一堆这样二进制和文本混合而成的东西。"
.
<< /Type /FontDescriptor /FontName /PSDLIF+CourierNewPSMT /Flags 5 /FontBBox
[-122 -680 622 1021] /ItalicAngle 0 /Ascent 833 /Descent -300 /CapHeight 571
/StemV 0 /XHeight 423 /AvgWidth 600 /MaxWidth 634 /FontFile2 23 0 R >>
.
. "⬆️也有一些这样的可读的部分。
.
xref
0 31
0000000000 65535 f 
0000026313 00000 n 
0000002668 00000 n 
0000005746 00000 n 
0000026292 00000 n 
.
. "⬆️最后是一个交叉引用表，我也没搞懂这是什么个机理"
.
trailer
<< /Size 31 /Root 19 0 R /Info 1 0 R /ID [ <32711aa8c4a468216fc0f60bc03e44ea>
<32711aa8c4a468216fc0f60bc03e44ea> ] >>
startxref
26766
%%EOF
.
. "⬆️最后是一个尾文件"
.
```

## 0x04 转换关系

最后的最后，简单介绍下这几个文件的转换关系。

因为 Tex 最开始只是对单一打印机做了适配，后来添加更好的适配性，可以转化成 dvi 之后转化为打印机可以打印的格式。因为有了 dvi 这个轮子，所以 ps 不能直接从 Tex 获得，需要先转化为 dvi 之后变成 ps. 类似的，pdf 可以从 dvi 直接转化。但是，它也可以从 ps 转化，因为他和 ps 算是继承关系。

![介绍转化关系的图片（网上宕的）](https://www.crifan.com/wp-content/uploads/2012/05/DVIPSPDF-.jpg)

## 0x05 参考文献

https://www.crifan.com/relation_of_dvi_ps_pdf_postscript_and_how_to_convert_among_them/

https://en.wikipedia.org/wiki/Device_independent_file_format

https://tex.stackexchange.com/questions/112268/pdf-vs-dvi-vs-postscript

https://baike.baidu.com/item/PostScript

https://zhuanlan.zhihu.com/p/30597307

## EOF