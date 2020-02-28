# 2018-04-Mindstorm
Class #4 is about Controlling and coding a Lego Mindstorm via python with a PI

### Note: To pair the EV3 with a PI you will need to use a command bluetoothctl 1st since EV3 is using a passkey

bluetoothctl ...  creates the secure connection and you can run the python code on the PI ... 
there the sequence
type in a command line bluetoothctl
Agent registered
[bluetooth]# agent on
Agent is already registered
[bluetooth]# scan on
Discovery started
trust 00:16:53:43:1B:92 <<< the EV3 MAC via Brick Info
pair 00:16:53:43:1B:92
Request PIN code
[agent] Enter PIN code: 1234
[CHG] Device 00:16:53:43:1B:92 Connected: yes

# After that you can execute the python code like python3 ev3-1.py
