import os


def get_mac_vnet_map():
    buff = os.popen("ifconfig | grep -E 'vnet|ether' | gawk '{printf (\"%s\\n%s\\n\", $1, $2)}'").readlines()
    mac_vnet = {}  # mac to vnet dict
    for i in range(0, len(buff)):
        if buff[i][0] == 'v':
            mac_vnet[buff[i + 3][8:(len(buff[i + 3]) - 1)]] = buff[i][0:(len(buff[i]) - 2)]
    return mac_vnet


def get_mac_port_map(mac_vnet):
    mac_port = {}  # mac to port dict
    for mac in mac_vnet:
        cmd = "sudo ovs-vsctl get interface " + mac_vnet[mac] + " ofport"
        tmpint = os.popen(cmd).readlines()
        if len(tmpint):  # jundge length of list
            mac_port[mac] = tmpint[0][0:len(tmpint[0]) - 1]
    return mac_port


def get_vnet_port_map(mac_port, mac_vnet):  # maybe no need
    vnet_port = {}  # vnet to port dict
    for mac in mac_port:
        vnet_port[mac_vnet[mac]] = mac_port[mac]
    return vnet_port


if __name__ == "__main__":

    mac_vnet = get_mac_vnet_map()

    # brctl delete some interfaces and add them to ovsbr1
    ovsbrt = 'ovsbr0'

    mactmp = ':99:03:18'
    cmd = "sudo brctl delif virbr0 " + mac_vnet[mactmp]
    os.popen(cmd)
    cmd = "sudo ovs-vsctl add-port ovsbr0 " + mac_vnet[mactmp]
    os.popen(cmd)

    mactmp = ':89:d6:9d'
    cmd = "sudo brctl delif virbr0 " + mac_vnet[mactmp]
    os.popen(cmd)
    cmd = "sudo ovs-vsctl add-port ovsbr0 " + mac_vnet[mactmp]
    os.popen(cmd)

    mactmp = ':23:fa:1b'
    cmd = "sudo brctl delif virbr0 " + mac_vnet[mactmp]
    os.popen(cmd)
    cmd = "sudo ovs-vsctl add-port ovsbr0 " + mac_vnet[mactmp]
    os.popen(cmd)

    mactmp = ':52:2c:af'
    cmd = "sudo brctl delif virbr0 " + mac_vnet[mactmp]
    os.popen(cmd)
    cmd = "sudo ovs-vsctl add-port ovsbr0 " + mac_vnet[mactmp]
    os.popen(cmd)

    mac_port = get_mac_port_map(mac_vnet)
    vnet_port = get_vnet_port_map(mac_port, mac_vnet)

    print(mac_vnet)
    print(mac_port)
    print(vnet_port)

    # add flow entries
#    cmd = "ovs-ofctl add-flow ovsbr1 priority=2,in_port=" + mac_port[':df:87'] + ",actions=output:" + mac_port[':12:77']
#    os.popen(cmd)

