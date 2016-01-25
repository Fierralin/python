import os


def get_mac_vnet_map():
    buff = os.popen("ifconfig | grep -E 'vnet|ether' | gawk '{printf (\"%s\\n%s\\n\", $1, $2)}'").readlines()
    mac_vnet = {}  # mac to vnet dict
    for i in range(0, len(buff)):
        if buff[i][0] == 'v':
            mac_vnet[buff[i + 3][11:(len(buff[i + 3]) - 1)]] = buff[i][0:(len(buff[i]) - 2)]
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
    mac_port = get_mac_port_map(mac_vnet)
    vnet_port = get_vnet_port_map(mac_port, mac_vnet)

    print mac_vnet
    print mac_port
    print vnet_port


