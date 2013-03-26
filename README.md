# gmreader
**current version: v0.1.5**

Listen to your emails with gmreader ( **g**oogle **m**ail reader ). A program that reads your gmail messages right to you.

Simply input you email address and password to run the program (password can be saved as argument). gmreader reads your unseen emails from recent to old. You must have a **Mac OSX, Linux, or Windows(with Cygwin)** machine in order to run gmreader. And if you have linux or windows, espeak must be installed on your computer, but it usually comes with the pre-installed packages(linux).

**Note: Spam emails and emails formatted similarly are often read incompletely or voided as Undefinable**

Tested on: Mac OSX 10.6.8 and Ubuntu 12.10

# Install
To download and install gmreader, you must follow the instructions below.

### Requirements
- Python
- Linux -> Should come with espeak; if not, install via `sudo apt-get install espeak`.
- Windows -> Download espeak command-line tools.
- Mac -> Just a working computer.

### Install via PIP
```
$ pip install gmreader
```

### Install via setup.py
First you need to get a copy of the source. I'm going to use git and clone it to my local computer. 

Clone the repository into a folder
```
git clone https://github.com/jawerty/gmreader.git gmreader
```

Install with setup.py
```
$ cd gmreader
$ python setup.py install
```

# Usage
Run default program
```
$ gmreader
Email Address: jawerty210@gmail.com
Password: 
```

Run with arguments
```
$ gmreader jawerty210@gmail.com mypassword123
```

# License
See the file LICENSE to view the MIT License

# Contact
If you would like to contact me for further information on the project, see the info below.

Email: jawerty210@gmail.com

Github: jawerty

Twitter: @jawerty

Blog: <http://wrightdev.herokuapp.com>
