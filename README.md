# Source repo for eegDataAnalysis
This software repository contains some code to allow anyone to process an electroencephalography signal (_process_data.ipynb_). To interact with this processing pipeline easily, refer to the [eegDataAnalysis Binder](https://mybinder.org/v2/gh/NicholasCHowlett/eegDataAnalysis/HEAD?labpath=process_data.ipynb). This repo also contains code to acquire this signal from OpenBCI hardware (_get_data.py_).

## Setup of Python
Python 3 is used for both acquiring and processing data. Acquiring data is conducted by using Python directly in a Windows environment, while data processing is conducted in a Linux environment (installed via Windows Subsystem for Linux).

### Python on Windows
Windows 10's security level needed to be reduced to allow activating of a Python-based virtual environment:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`.
Within this virtual environment, IPython was installed and used as the development environment for acquiring data from the brain-computer interface.

### Python on Linux
Ubuntu 20.04 LTS was used as the Linux distro on which Python packages for processing were used. JupyterLab was used as the development environment. The packages needed for processing (installed via Python's package manager) were installed within a virtual environment:
`pip3 install jupyterlab brainflow matplotlib mne`.
