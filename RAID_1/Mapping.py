import time,xmlrpclib,pickle,socket
class Mapping_table():
    server=0
    filename=""
    portno=0
    dir_path=""
    read_flag=0
    

class Server():
    server_in_use=0


class Configure_server():
    @staticmethod
    def get_active_servers(port1):
    
        proxy1=xmlrpclib.ServerProxy("http://localhost:"+str(port1)+"/",allow_none=True)
        proxy2=xmlrpclib.ServerProxy("http://localhost:"+str(port1+1)+"/",allow_none=True)
        proxy3=xmlrpclib.ServerProxy("http://localhost:"+str(port1+2)+"/",allow_none=True)
        proxy4=xmlrpclib.ServerProxy("http://localhost:"+str(port1+3)+"/",allow_none=True)
    
        active_servers=[]
        active_ports=[]
        
        return1=""
        return2=""
        return3=""
        return4=""
        try:
            return1=proxy1.check_status()
        except:
            pass
        if return1=="Alive":
            active_servers.append("server01")
            active_ports.append(port1)
        
        try:
            return2=proxy2.check_status()
        except:
            pass
        if return2=="Alive":
            active_servers.append("server02")
            active_ports.append(port1+1)
    
        try:
            return3=proxy3.check_status()
        except:
            pass
        if return3=="Alive":
            active_servers.append("server03")
            active_ports.append(port1+2)
            
        try:
            return4=proxy4.check_status()
        except:
            pass
        if return4=="Alive":
            active_servers.append("server04")
            active_ports.append(port1+3)
        
        return active_servers,active_ports



