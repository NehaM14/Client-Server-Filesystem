'''
THIS MODULE INTERACTS WITH THE MEMORY
''' 
import time, client_stub

#HANDLE FOR MEMORY OPERATIONS
#filesystem = Memory.Operations()
from typing import Any

client_stub = client_stub.client_stub()

active_servers=[]
active_ports=[]
map_list=[]                        #stores all mapping objects
count=0
wait_time=0
strt_port=[]
Virtual_BK=[]

class Mapping_table():
    server = 0
    filename = ""
    portno = 0
    dir_path = ""
    read_flag = 0

class Configure_server():
    @staticmethod
    def get_active_servers(port1):

        proxy1 = xmlrpclib.ServerProxy("http://localhost:" + str(port1) + "/", allow_none=True)
        proxy2 = xmlrpclib.ServerProxy("http://localhost:" + str(port1 + 1) + "/", allow_none=True)
        proxy3 = xmlrpclib.ServerProxy("http://localhost:" + str(port1 + 2) + "/", allow_none=True)
        proxy4 = xmlrpclib.ServerProxy("http://localhost:" + str(port1 + 3) + "/", allow_none=True)

        active_servers = []
        active_ports = []

        return1 = ""
        return2 = ""
        return3 = ""
        return4 = ""
        try:
            return1 = client_stub.check_status()
        except:
            pass
        if return1 == "Alive":
            active_servers.append("server01")
            active_ports.append(port1)

        try:
            return2 = proxy2.check_status()
        except:
            pass
        if return2 == "Alive":
            active_servers.append("server02")
            active_ports.append(port1 + 1)

        try:
            return3 = proxy3.check_status()
        except:
            pass
        if return3 == "Alive":
            active_servers.append("server03")
            active_ports.append(port1 + 2)

        try:
            return4 = proxy4.check_status()
        except:
            pass
        if return4 == "Alive":
            active_servers.append("server04")
            active_ports.append(port1 + 3)

        return active_servers, active_ports

def store_wait_time(t):
    global wait_time
    wait_time = t

def config_server(start_port):								# Added in final project
    global active_servers, strt_port, active_ports
    strt_port = start_port  # stores start port
    active_servers, active_ports = Configure_server.get_active_servers(start_port)  # returns currently active server names and ports

def print_acknowledgments():								# Added in final project
    global active_servers
    for each in active_servers:
        print "Connection established from " + each + ".py"

def Initialize_My_FileSystem():
    global active_ports
    for i in range(len(active_servers)):
        print "In "+active_servers[i]+".py"
        client_stub.Server.server_in_use=active_ports[i]
        MemoryInterface.Initialize_My_FileSystem()

# Create matrix with zero value - returns i and j
def check_mapping():
    global active_servers
    Mapping = []
    for i in [client_stub.configure.TOTAL_NO_OF_BLOCKS]:
        for j in [active_servers]:
            Mapping[i].append(j)
            Mapping[i][j]=0
            return i,j

# Use above matrix with input virtual block number - returns physical block number and server number
def addr_translate(Virtual_BK):
    global active_servers
    for i in [client_stub.configure.TOTAL_NO_OF_BLOCKS]:
        for j in [active_servers]:
            check_mapping.Mapping[i][j] = Virtual_BK
            i = i +12
            return i,j


#REQUEST TO FETCH THE INODE FROM INODE NUMBER FROM SERVER
def inode_number_to_inode(inode_number):
    retVal = client_stub.inode_number_to_inode(inode_number, server_number)
    print('inode_number_to_inode')
    print(retVal)
    return retVal

#REQUESTS THE VALID BLOCK NUMBER FROM THE SERVER 
def get_valid_data_block():
	global Virtual_BK, global active_servers , global server_number
    for i in range(len(active_servers)):
        (block_number, active_servers[i]) = check_mapping()
        active_servers[i] = server_number
        check_block_number = client_stub.get_valid_data_block(server_number)
        Virtual_BK = check_mapping.Mapping[active_servers[i]][block_number]
        Virtual_BK += 12
        return Virtual_BK

#REQUEST THE DATA FROM THE SERVER
def get_data_block(Virtual_BK):
    global server_number, global active_servers
    server_number, block_number = addr_translate(Virtual_BK)
    retVal =  ''.join(client_stub.get_data_block(block_number,server_number))
    print('get_data_block')
    print(retVal)
    return retVal

#REQUEST TO MAKE BLOCKS RESUABLE AGAIN FROM SERVER
def free_data_block(Virtual_BK):
    global server_number,
    global active_servers
    server_number, block_number = addr_translate(Virtual_BK)
    retVal =  client_stub.free_data_block((block_number, server_number))
    print('free_data_block')
    print(retVal)
    return retVal

# Giving location of parity in matrix
def parity_map():
    for i in range(client_stub.configure.TOTAL_NO_OF_BLOCKS):
        check_mapping.Mapping[i][i%4] = "Parity"

#REQUEST TO WRITE DATA ON THE THE SERVER
def update_data_block(Virtual_BK, block_data):
    global server_number, global active_servers
	server_number, block_number = addr_translate(Virtual_BK)
	print server_number
    client_stub.update_data_block(block_number, block_data, server_number)
    for i in range[len(active_servers)]:
		if check_mapping.Mapping[block_number][j] == "Parity":
			XOR(j,block_data,block_number)

def XOR(active_server,block_data, block_number):





#REQUEST TO UPDATE THE UPDATED INODE IN THE INODE TABLE FROM SERVER
def update_inode_table(inode, inode_number):
    retVal =  client_stub.update_inode_table(inode, inode_number)
    print('update_inode_table')
    print(retVal)
    return retVal


#REQUEST FOR THE STATUS OF FILE SYSTEM FROM SERVER
def status():
    retVal =  client_stub.status()
    print('status')
    print(retVal)
    return retVal

# This is used to assign active port
class Server():
def Server_function():
    return client_stub.Server.server_in_use


