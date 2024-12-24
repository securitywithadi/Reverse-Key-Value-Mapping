# Original dictionary with hostnames as keys and list of ports as values
host_to_ports = {
    "host1": [80, 443],
    "host2": [8080, 8443],
    "host3": [22, 23]
}

# Reversing the mapping: ports become keys, hostnames become values
port_to_hosts = {}
for host, ports in host_to_ports.items():
    for port in ports:
        port_to_hosts[port] = host

# Printing the result
print(port_to_hosts)
