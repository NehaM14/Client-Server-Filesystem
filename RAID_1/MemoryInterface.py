'''
THIS MODULE INTERACTS WITH THE MEMORY
''' 
import time,xmlrpclib,pickle,socket,Mapping

#HANDLE FOR MEMORY OPERATIONS
port1=0
proxy1=xmlrpclib.ServerProxy("http://localhost:"+str(port1)+"/",allow_none=True)


#PORT NUMBERS
def update_server():
    global port1,proxy1
    port1=Mapping.Server.server_in_use
    proxy1=xmlrpclib.ServerProxy("http://localhost:"+str(port1)+"/",allow_none=True)

    
def check_server_status():
    try:
        return_value=""
        update_server()
        return_value=proxy1.check_status()    
    except:
        pass
    if return_value=="Alive":
            return 0
    return -1



    

#REQUEST TO BOOT THE FILE SYSTEM
def Initialize_My_FileSystem():
    
    try:
        print("File System Initializing......")
        time.sleep(2)
        #global port1
        global proxy1
        update_server()
        state=proxy1.Initialize()
        print("File System Initialized!")
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily down.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)
        
    


#REQUEST TO FETCH THE INODE FROM INODE NUMBER FROM SERVER
def inode_number_to_inode(inode_number):
    try:
        update_server()
        return_value=proxy1.inode_number_to_inode(pickle.dumps(inode_number))
        return pickle.loads(return_value)
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily down.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)
        
    
    


#REQUEST THE DATA FROM THE SERVER
def get_data_block(block_number):
    #return ''.join(filesystem.get_data_block(block_number))
    try:
        update_server()
        return_value=proxy1.get_data_block(pickle.dumps(block_number))
        return_value=pickle.loads(return_value)
        
        if len(return_value)!=1:
            print return_value[0]
            return ''.join(return_value[1])
        else:
            return ''.join(return_value[0])
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily down.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)


#REQUESTS THE VALID BLOCK NUMBER FROM THE SERVER 
def get_valid_data_block():
    try:
        update_server()
        return_value= ( pickle.loads(proxy1.get_valid_data_block() ))
        if len(return_value)!=1:
            print return_value[0]
            return return_value[1]
        else:
            return return_value[0]
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily down.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)


#REQUEST TO MAKE BLOCKS RESUABLE AGAIN FROM SERVER
def free_data_block(block_number):
    try:
        update_server()
        proxy1.free_data_block(pickle.dumps(block_number))
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily downnnn.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        else:
            print "Error occured"
        exit(0)
    except:
        print "Error occured"
        exit(0)


#REQUEST TO WRITE DATA ON THE THE SERVER
def update_data_block(block_number, block_data):
    try:
        update_server()
        proxy1.update_data_block(pickle.dumps(block_number), pickle.dumps(block_data))
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily downnnn.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)


#REQUEST TO UPDATE THE UPDATED INODE IN THE INODE TABLE FROM SERVER
def update_inode_table(inode, inode_number):
    try:
        update_server()
        inode=pickle.dumps(inode)
        inode_number=pickle.dumps(inode_number)
        proxy1.update_inode_table(inode, inode_number)
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily downnnn.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)


#REQUEST FOR THE STATUS OF FILE SYSTEM FROM SERVER
def status():
    try:
        update_server()
        return_value=proxy1.status()
        return pickle.loads(return_value)
    except socket.error as error:
        if error.errno==113:
            print "Server may be temporarily downnnn.Try again after some time"
        elif error.errno==111:
            print "Cannot connect to the server.Try again after some time"
        exit(0)
    except:
        print "Error occured"
        exit(0)




   
