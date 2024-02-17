# EriCoin Cryptocurrency - Blockchain Application
Blockchain Codebase for EriCoin, a simple blockchain currency

This is a codebase for a basic blockchain currency.

** This is for development purposes only, and not currently an active cryptocurrency. **

In order to use this app, you need to have the following packages installed locally, or in a virtual environment
- I suggest using Anaconda to install the necessary packages in a virtual environment, and activate that virtual enviornment in the appropriate CLI instances for running each server

Necessary packages for running this code (I am running Python 3.11.7)
- flask
- flask-cors
- pycryptodome


For development purposes, in lieu of hosting Nodes EC2 or other Cloud-based VM instances, I just ran multiple terminal instances of the code, each on a different port.
- Spin up the server by running command ~ python node.py
  - This will spin up a server on the default port of 5000
  - To run another instance of the server (on port 5001 for example), you can run command ~ python node.py -p 5001
 
By running these commands:
  python node.py
  python node.py -p 5001

You will have spun up two instances of this app, each of which are accessible by going to each respective port on localhost

For instance, go to localhost:5000 or localhost:5001 to access these frontends.




