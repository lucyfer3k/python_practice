#!/usr/bin/env python3

import psutil as ps
import socket

def gather():
    '''Returns a list of resource monitoring data
    [0] - free cpu   
    [1] - free memory
    [2] - free disk
    [3] - localhost resolution'''
        
    try:
        cpu_free = 100.0 - ps.cpu_percent(interval=1)    
        memory_free = 100.0 - ps.virtual_memory().percent
        disk_free = 100.0 - ps.disk_usage('/').percent
        host_resolution = socket.gethostbyname('localhost')
        return [cpu_free, memory_free, disk_free, host_resolution]
    except Exception as e:
        raise e
 
 
def evaluate(cpu, memory, disk, localhost_ip):
    '''Rates if data provided should trigger an alert. Returns 0 if everything
    is fine, 1 if data provided is faulty or a string with what is wrong'''
    try: 
        if cpu < 20.0:
            return "CPU is overwhelmed"
        elif memory < 20.0:
            return "Low free RAM"
        elif disk < 15.0:
            return "Disk space is low"   
        elif localhost_ip != "127.0.0.1":
            return "Incorrect localhost resolving"
        else:
            return 0
    except:
        return 1
