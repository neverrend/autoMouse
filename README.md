# autoMouse

_Tool for refreshing pages during tests because I am incredibly lazy._

## Installation

```sh
# Fetch sources from GitHub
git clone https://github.com/neverrend/autoMouse.git

# Navigate to source directory
cd autoMouse

# Install dependencies
pip install -r requirements.txt

# Install autoMouse
python setup.py install
```

Then run with:

```sh
automouse
```

### Sample output

```sh
$ python3 mouse_automation.py
#############################################
## This program lets you automate mouse    ##
## clicks for things like refreshing pages ##
## still in progess and things todo.       ##
#############################################

Do you want to capture your mouse location?(Y\n): y
Enter seconds to wait before captue: 0

Your mouse location was: Point(x=-229, y=1117)

Is this the location you want to automate?(Y\n): y
What is the interval between clicks?(sec): 10

Press CTRL-C to end.

Click #1
Click Automation paused. Press Enter to Continue, and CTRL-C to exit.
```
