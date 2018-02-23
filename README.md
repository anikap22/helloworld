## helloworld
repo to upload helloworld cli package

#Installation
Clone the repo using pip to install it

```bash
git clone https://github.com/anikap22/helloworld.git
cd helloworld/
pip install .
```

#CLI Usage
To use the executable helloworld command line program:
```bash
$ helloworld -h
usage: helloworld [-h] [-n NAME] [--howlong] [--countdown] [--cny CNY]
                  [--fortune]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  optional name to say hello to
  --howlong             print days until Darwin's next birthday
  --countdown           print predicted days until end of the world
  --cny CNY             print the chinese year of your bith (enter birth year)
  --fortune             print the number of kids and length of your life
```

#API Usage
To use the helloworld Python API:
```bash
import helloworld
helloworld.helloworld(cny=1991)

hello world
you are a sheep
```
