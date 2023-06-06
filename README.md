# RotatedStomataNet
A software of RotadetStomataNet:A deep rotated object detection network for directional stomata phenotype analysis.

[](C:\Users\Administrator\Desktop\figures\graphical_abstract.tif)

## Introduction

We innovatively treat stomatal detection as rotating target detection and built RotatedStomataNet, which aims to provide an end-to-end, real-time, intelligent phenotyping system for plant stomata and apertures size. It can realize one-stop automatic collection of phenotypic information such as the position, density, length and width of plant stomata without step-by-step operation.

## Prepare 
1.Download [Supplementary information](Link https://pan.baidu.com/s/1x1SLycFYy9_XDhmT8cxWOQ?pwd=a3pv   Extract code：a3pv)

2.Download code above;

3.Download Dicotyledons - destructive weights [r3det_wiouv2_r50_fpn_2x_20200616ninanjie](Link：https://pan.baidu.com/s/1jBTemqsFSlvo5CAVXFbpUQ?pwd=opjx  Extract code：opjx) then put it in the 'newpths' folder; 

4.Download Monocots - destructive weights [r3det_wiouv2_r50_fpn_2x_20200616yumi](Link：https://pan.baidu.com/s/1CQRb3K_BKS-YLKrhy1x8gg?pwd=sqe4  Extract code：sqe4) then put it in the 'newpths' folder; 

5.Download Monocots - nondestructive weights [r3det_wiouv2_r50_fpn_2x_20200616yumiwusun](Link：https://pan.baidu.com/s/1MeFtDGBXmrOjfs4RMlOccA?pwd=vk80  Extract code：vk80) then put it in the 'newpths' folder; 

6.Download [Configuration text](Link：https://pan.baidu.com/s/1dz-17ZGrDrEkCH0CJIatdw?pwd=3aqz  Extract code：3aqz) then put it in the 'RotatedStomataNet' folder;

7.Download [Configuration text-torch](Link：https://pan.baidu.com/s/1lT4rkPBw1vv4pMj_ayYaOw?pwd=xnre  Extract code： xnre  ) then put it in the 'RotatedStomataNet/torch/Lib' folder;

8.Download [RotatedStomataNet System](Link：https://pan.baidu.com/s/1VIVvRcBdcSI5YGW8xs4sug?pwd=h1m2  Extract code：h1m2)then put it in the 'RotatedStomataNet' folder;

9.Download [Data](Link：https://pan.baidu.com/s/1FEphzoMhkw9wwApC8pg6Wg?pwd=95rs  Extract code：95rs) ;

## Usage of RotatedStomataNet

1.Run the RotatedStomataNet.exe file to start.

2.RotatedStomataNet has two detected modes: monocotyledon mode and dicotyledon mode,  which can be used for two dataset formats, destructive images and non-destructive images (this mode for dicots is not currently detectable), and the user can choose according to their needs.

3.To start detection: First, first select Single Image(Image) or Directory Detection(Directory). Second, drag a PNG image or folders (Directory) to the left image. Third, set parameters (Set Congfig), such as the position where the test results are saved and the scale of the predicted image. Finally, click "Start".

4.Users can adjust Confidence based on the initial test results to get better results.

5.By default, RotatedStomataNet automatically stores detected iamges. In addition, users can select whether to store single stomatal picture and phenotype data according to their needs. If you choose to store phenotype data, RotatedStomataNet will generate an excel file.

