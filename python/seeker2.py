import ev3, struct, time

my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host='00:16:53:43:1b:92')
print("start")
my_ev3.verbosity = 1

ops_read = b''.join([
    ev3.opInput_Device,
    ev3.READY_RAW,
    ev3.LCX(0),    # LAYER
    ev3.LCX(1),    # NO
    ev3.LCX(33),   # TYPE - IR
    ev3.LCX(1),    # MODE - Seeker
    ev3.LCX(2),    # VALUES
    ev3.GVX(0),    # VALUE1 - heading   channel 1
    ev3.GVX(4)     # VALUE2 - proximity channel 1
])
speed_ctrl = ev3.PID(0, 2, half_life=0.1, gain_der=0.2)
while True:
    reply = my_ev3.send_direct_cmd(ops_read, global_mem=8)
    (heading, proximity) = struct.unpack('2i', reply[5:])
    print("Distance (in CM) =",heading)
#    print(proximity)
    time.sleep(0.250)
#    if proximity == -2147483648:
#        print("**** lost connection ****")
#        break

