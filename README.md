Welcome to avatar², the target orchestration framework with focus on dynamic
 analysis of embedded devices' firmware!

Avatar² is developed and maintained by [Eurecom's S3 Group](http://s3.eurecom.fr/).

# Lock version
buat versi lama ini bekerja lagi dengan memperbaiki dependacies
tidak cocok.
```
$ virtualenv -p $(which python2) py2
$ source py2/bin/activate
$ pip2 install pip-tools
$ pip-compile requirements.in
```
then result requirements.txt, we modifed in unicorn==1.0.2rc1
with `pip2 install unicorn==1.0.2rc1` next:
```
$ pip2 install angr==7.7.9.8.post1
$ pip2 install .
```




# Building

Building avatar² is easy!

First, make sure that all the dependencies are present:

```
sudo apt-get install python-pip python-setuptools python-dev cmake
```

Afterwards, the following three commands are enough to install the core.
```
$ git clone https://github.com/avatartwo/avatar2.git
$ cd avatar2
$ sudo pip install .
```
Afterwards, the different target endpoints can be built, such as QEmu or PANDA.
For doing so, we are providing build-scripts for Ubuntu 16.04 - while other
distributions are not officially supported (yet), the scripts are known to
work with slight modifications on other distributions as well.
```
$ cd targets
$ ./build_*.sh
```

# Getting started
For discovering the power of avatar² and getting a feeling of its usage,
we recommend highly checking out the 
[handbook](https://github.com/avatartwo/avatar2/tree/master/handbook) here on
github.
Additionally, a documentation of the API is provided 
[here](https://avatartwo.github.io/avatar2-docs/) and some exemplary
avatar²-scripts can be found 
[here](https://github.com/avatartwo/avatar2-examples).

For further support or follow-up questions, feel free to contact us via IRC
in #avatar2 on freenode, or to send a mail to avatar2 [at] lists.eurecom.fr, 
our public mailing list.

Additionally, you can subscribe to the list 
[here](https://lists.eurecom.fr/sympa/subscribe/avatar2).
