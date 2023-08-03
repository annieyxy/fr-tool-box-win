# fr-tool-box-win

This is a PyQt6 based tool box for basic automotive calculation and graph plotting. 

## Windows 10 / Linux-based OS

### Prerequisites:

* Python3

* PyQt6

* pyqtgraph

* Qt Creator (For developers to design layouts)

### Installation:

* To install PyQt6 and pyqtgraph modules, run command `pip install pyqt6` and `pip install pyqtgraph` in Terminal
   
* Download & install Qt Designer from [here](https://www.qt.io/download) to edit UI

## Running the Tool Box in Python:

* Run command `python main.py` to view the Tool Box app

## Editing Tool Box UI:

* Open `tool-box-interface.ui` in Qt Creator to view and modify UI

* Run `pyuic6 -x tool_box_interface.ui -o tool_box_interface.py` to generate corresponding Python file

## Deploying to an executable file

* The pyinstaller tool is used for packaging our app. Run `pip install pyinstaller` in Terminal to install this module.

* Run `pyinstaller --add-data 'image;image' -n ‘Tool-Box’ -wF main.py` in Windows
  or `pyinstaller --add-data 'image:image' -n ‘Tool-Box’ -wF main.py` in Linux to package the app into a single executable.

* After packaging is done, the executable file can be found in the `dist` folder. 
