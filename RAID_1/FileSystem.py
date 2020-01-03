import MemoryInterface, AbsolutePathNameLayer,datetime,time
import Mapping
active_servers=[]
active_ports=[]
map_list=[]                        #stores all mapping objects
count=0
wait_time=0
strt_port=[]

def Initialize_My_FileSystem():
    global active_ports
    for i in range(len(active_servers)):
        print "In "+active_servers[i]+".py"
        Mapping.Server.server_in_use=active_ports[i]
        MemoryInterface.Initialize_My_FileSystem()
        AbsolutePathNameLayer.AbsolutePathNameLayer().new_entry('/', 1)                                     #??????????

def config_server(start_port):
    global active_servers,strt_port,active_ports
    strt_port=start_port  # stores start port
    active_servers,active_ports=Mapping.Configure_server.get_active_servers(start_port)   		#returns currently active server names and ports
    
def print_acknowledgments():
    global active_servers
    for each in active_servers:
        print "Connection established from "+each+".py" 
    
def store_wait_time(t):
    global wait_time
    wait_time=t

def check_server_status():
    return MemoryInterface.check_server_status()

#HANDLE TO ABSOLUTE PATH NAME LAYER
interface = AbsolutePathNameLayer.AbsolutePathNameLayer()

class FileSystemOperations():
   
    
    #MAKES NEW DIRECTORY
    def mkdir(self, path):
        global active_servers,active_ports
        global strt_port
        config_server(strt_port)
        
        for each in active_ports:
            Mapping.Server.server_in_use=each
            interface.new_entry(path, 1)

        

    #CREATE FILE
    def create(self, path):
        global active_servers
        global strt_port
        config_server(strt_port)
        return_value=-1
        global map_list,count
        for each in map_list:
            if each.filename==path:
                print "Error: File name already exists"
                return
        for i in range(len(active_servers)):
            init=0
            if active_servers[i]=="server01" and count%2==0:
                Mapping.Server.server_in_use=active_ports[i]
                init=1
                
                
            elif active_servers[i]=="server02" and count%2==0:
                Mapping.Server.server_in_use=active_ports[i]
                init=1
            
            elif active_servers[i]=="server03" and count%2!=0:
                Mapping.Server.server_in_use=active_ports[i]
                init=1
            
            elif active_servers[i]=="server04" and count%2!=0:
                Mapping.Server.server_in_use=active_ports[i]
                init=1
                
            if init==1:
                return_value=interface.new_entry(path, 0)
                if return_value!=-1:
                    mapping_table_obj=Mapping.Mapping_table()
                    mapping_table_obj.server=active_servers[i]
                    mapping_table_obj.filename=path
                    mapping_table_obj.portno=active_ports[i]
                    path_list=path.split("/")
                
                    path_list.remove(path_list[-1])
                    path_list.remove(path_list[0])
        
                    dir_path=""
                    
                    for each in path_list:
                        
                        dir_path+="/"+each
                    mapping_table_obj.dir_path=dir_path
                    map_list.append(mapping_table_obj)
                    
        if return_value!=-1:
            count+=1
        

    #WRITE TO FILE
    def write(self, path, data, offset=0):
        global wait_time
        servers=[]
        server_ports=[]
        init=0
        for each in map_list:
            if each.filename==path:
                #Server_port.Server.server_in_use=each.portno
                servers.append(each.server)
                server_ports.append(each.portno)
                #interface.write(path, offset, data)
                init=1
        if init==1:
            print "write will be performed on"
        for j in servers:
            print j+".py"
        msg="waiting to write in another replica"
        for i in range(len(servers)):
            if i==1 and msg!="":
                print msg
            time.sleep(wait_time)
            Mapping.Server.server_in_use=server_ports[i]
            value=check_server_status()
            if value==-1:
                msg=""
                continue
            
            
            print "Writing on "+servers[i]+".py"
            
            
            return_value=interface.write(path,offset,data)
            if return_value!=-1:
                print ("Written successfully on ")+servers[i]+".py"
            

        if init!=1:
            print ("Error: File not exists")
      

    #READ
    def read(self, path, offset=0, size=-1):
        data_read=""
        servers=[]
        server_ports=[]
        read_flags=[]
        flag=0
        for each in map_list:
            if each.filename==path:
                servers.append(each.server)
                server_ports.append(each.portno)
                read_flags.append(each.read_flag)
                flag=1
        if flag==1:
            print "data resides on"
        for j in servers:
            print j+".py"
        all_1=[1,1]
        if read_flags==all_1:
            read_flags=[0,0]
        for each in map_list:
            if each.filename==path:
                each.read_flag=0
        time.sleep(wait_time)
        ignore=0
        for i in range(len(servers)):
            Mapping.Server.server_in_use=server_ports[i]
            value=check_server_status()
            if value==-1:
                ignore=1
                continue
            if read_flags[i]==1 and ignore==0:
                continue
            print "reading from "+servers[i]+".py"
            
            read_buffer = interface.read(path, offset, size)
            if read_buffer != -1:
                print(path + " : " + read_buffer)
            for each in map_list:
                if each.filename==path and each.server==servers[i]:
                    each.read_flag=1
            data_read="done"
            break
        if data_read=="":
            for i in range(len(servers)):
                Mapping.Server.server_in_use=server_ports[i]
                value=check_server_status()
                if value==-1:
                    continue
                
                print "reading from "+servers[i]+".py"
                
                read_buffer = interface.read(path, offset, size)
                if read_buffer != -1:
                    print(path + " : " + read_buffer)
                for each in map_list:
                    if each.filename==path and each.server==servers[i]:
                        each.read_flag=1
                
                break

        
            

        if flag!=1:
            print ("Error: File not exists")
        

    
    #DELETE
    def rm(self, path):
        file_p=0
        remove_list=[]
        global map_list,active_servers
        #
        global strt_port
        config_server(strt_port)
        for each in map_list:
            if each.dir_path==path:
                print "Error: Directory is non empty in some/all servers"
                return
        
        for each in map_list:
            if each.filename==path:
                file_p=1
                Mapping.Server.server_in_use=each.portno
                return_value=interface.unlink(path)
                remove_list.append(each)
        for each in remove_list:
            map_list.remove(each)
        
        if file_p!=1:           #directory
            for each in active_ports:
                Mapping.Server.server_in_use=each
                interface.unlink(path)

    


    #MOVING FILE
    def mv(self, old_path, new_path):
        move_done=0
        move_attempt=0
        remove_list=old_path.split("/")
        global map_list
        new_full_path=new_path+"/"+remove_list[-1]
        for each in map_list:
            if each.filename==new_full_path:
                print("Error: Move unsuccessful because file exists in destination")
                return
        for each in map_list:
            if each.filename==old_path:
                Mapping.Server.server_in_use=each.portno
                return_value=interface.mv(old_path, new_path)
                if return_value!=-1:
                    each.filename=new_full_path
                    each.dir_path=new_path
                move_attempt=1
        if move_attempt!=1:
            print "Error: Move unsuccessful because file doesn't exist"
        
        
        


    #CHECK STATUS
    def status(self):
        
        global active_servers,active_ports
        global strt_port
        config_server(strt_port)
        for i in range(len(active_servers)):
            print("Status of "+active_servers[i]+".py")
            Mapping.Server.server_in_use=active_ports[i]
            print(MemoryInterface.status())

  


#if __name__ == '__main__':
    
