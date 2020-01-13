#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import socket
import asyncio

 

RESTART_COMMAND_DICT = {
    9006: "cmd"
    9007: "cmd"
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
    port_list = [9006, 9007]
    while True:
        restart_ports_service(port_list)
        time.sleep(60 * 10)



if __name__ == "__main__":
    main()
