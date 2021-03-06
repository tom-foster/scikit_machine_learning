# Machine learning in python using scikit-learn

## In brief
Getting you up and running with machine learning using scikit-learn. On a windows machine but making using of the Windows Linux Subsystem. You should be on Windows 10, and it assumes the Windows Linux Subsystem is already installed.

This takes advantages of using Windows, and Linux. We'll be installing python3.6 and everything will be making use of the latest version as of writing python3.6.

The version of Linux is the Ubuntu 16.04 flavour that is available in Windows Fall Creator 1709.

## Installation

Ubuntu runs python 3.5.2, but we'll be running 3.6 therefore so we want to install that version instead.

Open an ubuntu terminal and type.

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```
Python 3.6 will now sit on the WLS system, we then need to create a file that attaches to windows system.

**Do not remove the other version of Python.**

We don't really want to leave the documents to the linux subsytem, so we'll switch to the windows file structure. (Additionally this could be a failed attempt at getting colleagues to use linux, when they want Windows).

```bash
cd /mnt/c/Users/Tom/Documents/
mkdir scikit_machine_learning
```

When entering the above, mnt stands for mounted and references the hardrive.

We then want to create a virtual environment so we move into that directory

```bash
cd /scikit_machine_learning
python3.6 -m venv venv
```

We call:
* `python3.6` because it's the version we specifically want to use.
* `-m ` calls a module
* `venv ` is a module being called
* `venv ` (2) is the name we're giving to venv, it stands for virtual environment, you may wish to call it venv or virtualenv.

We now want to activate our virtual environment (venv).

```bash
source venv/bin/activate
[Console]: (venv) tfos1@scikit_machine_learning$
```

Once it's activated you'll see (venv) at the beginning of your Bash terminal.

The reason for using a virtual environment is that you may run multiple projects but need different versions, of software for instance python itself.

As an example. With the (venv) active type.

```bash 
python --version
[Console]: Python 3.6.4
```

Your version of python is now installed (note that you don't have to run it as python3.6 now).

Deactivate your virtual environment and run the above command.

```bash
deactivate
python --version
[Console]: The program 'python' can be found in the following packages:
 * python-minimal
 * python3
Try: sudo apt install <selected package>
```

Note it won't run the command now, if you did want to check your version outside of the virtual environment. Run.

```bash
python3 --version
[Console]: Python 3.5.2
```

Reactivate your virtual environment again.

```bash
source venv/bin/activate
```

### Installing requirements.txt
You'll want to download the requirements.txt if nothing else to install the right components.

The requirements.txt contains the list of all modules you'll want to install that will be required for scikit learn.

With the virtual environment active run:

```bash
pip install -r requirements.txt
```

This will install the modules (pip) is package manager with python.

### Checking your installs

We want to check that the installs are in there so a couple of test files have been included. in the tests folder. I should stress these aren't unit or functional tests. Just simply testing that the installs have worked.

To run the numpy_test.py with your virtual environment active.

```bash
python tests/numpy_test.py
```

You should see in the console

```bash
(venv) tfos1@scikit_machine_learning$python tests/numpy_test.py
A numpy array :
[[1 2 3]
 [4 5 6]]
```

You may wish to run the other tests if you like as there are little snippets in them which provide useful.

## Running Jupyter Notebook

Alot of the work will now take place in jupyter notebook

To run jupyter notebook with your virtual environment active.

```bash
jupyter notebook
```

This will launch a local server and give you a token copy that and you'll see your juptyer notebook open.

If you want to look at explanations/sprase_matrices.ipynb you'll see the graph showing the advantages of sparse matrices.

Jupyter is a useful tool and will be used going forward.

Check out the demos in the file jupyter_demos folder to see a couple of examples using matplotlib and pandas.
