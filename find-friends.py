def check_connection(network, first, second):
    networks = [set(())]
    for node in network:
        nodes = node.split('-')
        node1 = nodes[0]
        node2 = nodes[1]

        for net in networks:
            if node1 in net or node2 in net:
                net.add(node1)
                net.add(node2)
                networks.append(net)

            if node1 not in net and node2 not in net:
                print networks
                print node1
                print node2
                net = set((node1, node2))
                networks.append(net)

    for net in networks:
        if first in net and second in net:
            return True
    return False

print check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99")
