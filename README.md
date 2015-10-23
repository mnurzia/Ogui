# Ogui v0.2.0

![Python 3.x](https://rawgithub.com/maxmillion18/Ogui/master/images/python-3.x-brightgreen.svg)
![MIT License](https://rawgithub.com/maxmillion18/Ogui/master/images/license-MIT-blue.svg)

Ogui is a simple GUI for [Ogar](http://ogarproject.com/), an open source [Agar.io](http://agar.io) server inplementation built in Node.js. Ogui is written in Python.

![1](https://raw.githubusercontent.com/maxmillion18/Ogui/master/images/1.png)

Ogar can:
- Run every Ogar server command (e.g. ```addbot```, ```mass```, ```board```)
- Check output of commands ```playerlist``` and ```status```, then display them
- Open gameserver.ini and modify it using the Config script (this will be added into the GUI)

## Running

### Unix (Linux, Mac)

1. Install node, ws (for node), and pexpect (for python)
2. Go to your favorite command line, and run: ```git clone https://github.com/maxmillion18/Ogui/; cd Ogui;```
3. Run GUI.py (you may need root privileges)
4. Have fun!

### Windows

1. Install node and npm, then install the npm module ws.
2. Install the python module ```pexpect```
3. Download Ogui's Zip file
4. CD into the zip file
5. Run GUI.py (again, root/administrator privileges may be needed)
