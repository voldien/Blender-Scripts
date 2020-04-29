
## Installing CUDA 8 for GeForce 400/500 Ubuntu
A simple installation guide for installing CUDA for blender 2.79 and below for CUDA 2.1. A later version of _Blender_ has not been tested. Furthermore, it should be notated that this guide is for the none-Desktop version. So if using some desktop 
version is might be required to stop the desktop environment service while installing the CUDA and the NVIDIA drivers.

The first step is to download the CUDA respository for the correct Linux Disturbtion and version. All the CUDA versions and all the installation files can be downloaded on Nvidias' developer site [https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)
For ubuntu once the Debian package is downloaded. Installing the CUDA can be done using the _dpkg_ program, see the following for an example.

`sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo apt update`

Install the cuda-8-0-toolkit rather than _cuda_ since it will attempt to install the latest driver and the latest cuda which is not supported on the 400/500 series. Becausek, if the latest Nvidia driver is installed the GPU won't work at all. Furthermore,
any CUDA above 8 is not supported by the 400/500 graphic series. See more information on the Nvidia website.

`apt install cuda-8-0-toolkit nvidia-driver 390`

A simple test to check if working is by the command as followed. However, some time is can be required to restart the machine before the DKMS will load the NVIDIA drivers properly.

`nvidia-smi`

The CUDA compiler needs GCC 4.8 in order to compile CUDA source code.

`apt install gcc-4.8`

