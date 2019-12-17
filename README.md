# DolphinTextureLinker
Python script to pair downscaled textures to original textures (or upscaled textures) by using SSIM to image match


* NOTE OTX/DTX/DFDTX/UTX are NOT in this repo, they are huge collections of files.
* This repo exists as archive of the python script and process to achieve the texture mapping.


* Generates resumable file when complete (a few hours may be required to run the initial matching)
* Run v2 script, then run resumable script to create the output for Dolphin

In theory this can be used for any game to map Dolphin's hash dump to the original texture name for easier sorting.
Provided you have a way to extract the original files with meaningful names via Magic.TXD or some other tool for textures.


Completed POC:
https://youtu.be/YuLxW7KGj0Y

----------
```Key: 
--
OTX = Original Textures extracted via Magic.TXD in PNG format
DTX = Downscaled Textures extracted via Magic.TXD in PNG format
--
DFDTX = Downscaled Textures DUMPED via Dolphin
UTX = Upscaled Textures (From running an upscaler on OTX, and any manual replacements are also done to UTX prior to use)

1a. Create OTX and DTX -> ShadowTXD_Automator need to be modified to extract all textures in PNG format

1b. Create DFDTX -> Every single event, level, texture must be dumped via Dolphin (no organization required)

2a. Create UTX from OTX and make any manual modifications BUT KEEP THE ORIGINAL FILE NAMES!!!!!

3. Python script to use SSIM algorithm and map DFDTX to DTX. When a match is found, take DTX's name and replace with UTX (OR OTX) equivalent (name should be identical)
```
---------