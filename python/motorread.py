
import ev3, struct

my_ev3 = ev3.EV3(protocol=ev3.BLUETOOTH, host='00:16:53:43:1b:92')
my_ev3.verbosity = 1

ops = b''.join([
    ev3.opInput_Device,
    ev3.READY_SI,
    ev3.LCX(0),                   # LAYER
    ev3.port_motor_input(ev3.PORT_B), # NO
    ev3.LCX(7),                   # TYPE
    ev3.LCX(0),                   # MODE
    ev3.LCX(1),                   # VALUES
    ev3.GVX(0),                   # VALUE1
    ev3.opInput_Device,
    ev3.READY_RAW,
    ev3.LCX(0),                   # LAYER
    ev3.port_motor_input(ev3.PORT_C), # NO
    ev3.LCX(7),                   # TYPE
    ev3.LCX(0),                   # MODE
    ev3.LCX(1),                   # VALUES
    ev3.GVX(4)                    # VALUE1
])
reply = my_ev3.send_direct_cmd(ops, global_mem=8)
(pos_a, pos_d) = struct.unpack('<fi', reply[5:])
print("positions in degrees (ports B and C): {} and {}".format(pos_a, pos_d))
