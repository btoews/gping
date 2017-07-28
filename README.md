# GPing #

An asynchronous, event-driven, pure-python ping implementation using raw sockets based on gevent.
This is a fork of the python-ping project replacing its internal machinery with gevent.
The point is to have an event driven ping utility for doing a huge number of concurrent pings efficiently.


## Usage ##

### Run on the commandline ###

    # Ping some hostnames
    gping --hostnames=gnu.org,fsf.org,google.com,microsoft.com,googleusercontent.com,live.com,stackoverflow.com,141.1.1.1,8.8.8.8,192.168.123.1,192.168.999.1

    # Bind to a specific IP address
    gping --bind=192.168.111.2 --hostnames=google.com,stackoverflow.com,8.8.8.8

### Demo with 100 concurrent pings ###

    # Ping the top 100 domains
    time python gping.py

### Use as library ###

    from gping import GPing

    gp = GPing()
    gp.send("127.0.0.1", test_callback)
    gp.join()

## Install ##

### From Python Package Index ###
This *should* be easy on your average \*nix box, just type:

    sudo pip install gping


### From GitHub ###
This way of installing gping is suitable for hacking on it:

    git clone https://github.com/mastahyeti/gping.git
    cd gping
    virtualenv .venv27
    source .venv27/bin/activate
    python setup.py develop

## License and Credits ##

The python-ping project was started by Matthew Dixon Cowles.

    - copyleft 1989-2016 by the python-ping team, see AUTHORS for more details.
    - license: GNU GPL v2, see LICENSE for more details.

It was forked and ported to `gevent` by Ben Toews. Since then, this program is now called appropriately *GPing*.

He says:
> I have left the license and authors information intact, but this project seems to have a long history or forks and such
> so I am probably somehow pissing someone off or violating some license. Let me know if this is the case and I will be better.
