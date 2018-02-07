# scikit-learn starting with machine learning in python

start a virtual environment, and install packages in requirements.

this is using python3.6

I'm using the windows linux subsystem, so it's defined as python3.6 on the command line, as ubuntu 16.04 is using 3.5.2 by default.

You'll want to install 3.6 separately.

## On WLS
On WLS you'll need to install tkinter for the Ubuntu Windows Linux Subsystem, package 3.6 from deadsnakes.

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3.6-tk
```

Python will now sit on the WLS system, we then need to create a file that attaches to windows system.

We don't really want to documents to the linux subsytem, so we'll switch to the windows file structure.
(mnt stands for mounted)

```bash
cd /mnt/c/Users/Tom/Documents/
mkdir scikit_machine_learning
```

We then want to create a virtual environment so we move into that directory

```bash
cd /scikit_machine_learning
python3.6 -m venv venv
```

Activating your virtual environment (venv). The reason for using a virtual environment is mainly for
when using your computer system, you may upgrade to new editions of software, and a virtual environment
keeps old and new projects protected and only calls the relevant software relevant to the project.



