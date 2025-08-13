# Miniature Engine
A simple 3D visualisation engine using orthographic projection. The positions of each vertex are calculated via matrix multiplication of the position vector with the 3 rotation matrices. 
In order to decide which sides are drawn closest to the "camera", the center of each square is tracked. This way, the cube's faces can be appended to a list in order of their z-value, which 
determines in what order they are rendered on the pygame screen.
## Libraries
* Pygame
* Math
## Preview
![3D-Cube](https://github.com/user-attachments/assets/2d3ef756-5980-405b-bd71-5a0b49b88eb5)
## Set-Up
### To try this code out for yourself, please follow the steps below...
First of all, make sure you have python installed on your system. If not, you can get it here on the [official website](https://www.python.org/downloads/) <br>

Next, copy the code from this repository into your own editor, or alternatively clone the repository into whichever directory your using with the git clone command
```console
git clone https://github.com/elliot-j03/Miniature-Engine.git
```
If you haven't already got a .venv file in your directory, run this command to create a new one
```console
python -m venv .venv
```
Then, install the required modules. To do this you need to activate the python virtual environment
```console
source .venv/Scripts/activate
```
and use pip to download what you need
```console
pip install -r requirement.txt
```
Now you should be set up correctly and able to run the mini engine. To start the program you need to run **main.py**. You can do this by either running it in your editor or using the terminal as shown below
```console
python path/to/main.py
```
Now you should have a working engine :)
