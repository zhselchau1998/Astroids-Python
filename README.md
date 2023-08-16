# Astroids-Python

### Dependencies
- Python (developed with 3.11.4)
- pip
- Pynput through pip
- PIL through pip

### Usage
To start the game you will need to execute Driver.py using the following commands on the command line:
```bash
py Driver.py
```
or
```bash
python Driver.py
```
### Description
I set out to create the classic game astroids using Python. 
I wanted to keep this game as lightweight as possible and whenever realistically possible I only used the default libraries.
As a direct result of that lightweight goal I decided not to utilize the pygame engine as it is far too bloated for a project as small as this.
This lead to the decision to utilize canvas objects with tkinter to draw the gameboard.
Tkinter does show some performance issues when many gameobjects are on-screen, however given the relatively low number of game objects this becomes a non-issue.
The decision to use PIL comes naturally after deciding to use tkinter as utilizing the image object then converting it to a tkimage allows for easy rotation of the images.
Finally, the decision to use Pynput was to create a sort of keyboard listener very similar to the KeyListener found in the default Java libraries.

### Gameplay
The game is meant to play as intuitive as possible.
To that end you can either move with WASD or the Arrow Keys.
In addition you use the spacebar is used to shoot.
