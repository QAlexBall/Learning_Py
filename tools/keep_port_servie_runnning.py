#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import socket
import asyncio

 

RESTART_COMMAND_DICT = {
    15432: "ssh -Nf -i ~/powerarena-swarm.pem -L 15432:localhost:5432 ubuntu@13.211.149.60",
    58292: "ssh -Nf -L 58292:localhost:8292 -p 2222 support@www.hkdev.motherapp.com",
}


def is_port_open(port):
    is_open = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        is_open = True
        print("Port %d is open" % port)
    else:
        print("Port %d is not open" % port)
    sock.close()
    return is_open


async def is_ports_open(port_list):
    is_open_dict = {}
    for port in port_list:
        is_open_dict[port] = True if is_port_open(port) else False
    await asyncio.sleep(5)
    return is_open_dict


def restart_port_service(port):
    cmd = RESTART_COMMAND_DICT[port]
    if not is_port_open(port):
        print("===> restart port service:", cmd)
        os.system(cmd)
    print("===> check again: ")
    is_port_open(port)


def restart_ports_service(port_list):
    for port in port_list:
        restart_port_service(port)
        print()


def main():
    port_list = [15432, 58292]
    while True:
        restart_ports_service(port_list)
        time.sleep(60 * 10)



if __name__ == "__main__":
    main()
