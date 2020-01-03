import FileSystem,time



if __name__ == '__main__':
    #DO NOT MODIFY THIS
    #t1= int(round(time.time() * 1000))
    print "Number of servers:4"
    while(1):
        t=raw_input('give waiting time t')
        if t.isdigit():
            t=int(t)
            break
     
    FileSystem.store_wait_time(t)
    while(1):
        start_port=raw_input("enter 4 digit starting port number")        if start_port.isdigit():
            start_port=int(start_port)
            break
    #print t
    

    while(1):
        enter=raw_input("waiting to start the servers..press enter after starting the servers")
        if enter=="":
            break

    
    FileSystem.config_server(start_port)
    FileSystem.print_acknowledgments()
    FileSystem.Initialize_My_FileSystem()
    
    
    obj=FileSystem.FileSystemOperations()
    
   


    while(1):
    
        cmd=raw_input("$ ")
        cmd=cmd.split(" ")
        if(cmd[0]=="exit"):
            
            
            exit(0)
        if(cmd[0]=="mkdir"):
            if len(cmd)<3 and len(cmd)>1:
        
                obj.mkdir(cmd[1])
            else:
                print("Usage:mkdir path")

        elif cmd[0]=="status" :
            if len(cmd)<2:
                obj.status()
            else:
                print("Usage:status")

        elif cmd[0]=="create" :
            if len(cmd)<3 and len(cmd)>1:
                obj.create(cmd[1])
            else:
                print("Usage:create path")

        elif cmd[0]=="rm" :
            if len(cmd)<3 and len(cmd)>1:
                obj.rm(cmd[1])
            else:
                print("Usage:remove path")

        elif cmd[0]=="mv"  :
            if len(cmd)<4 and len(cmd)>1:
                obj.mv(cmd[1],cmd[2])
            else:
                print("Usage:move oldpath newpath")
        
        
        elif cmd[0]=="read" :
            try:
                
                if len(cmd)<5 and len(cmd)>1:
                    if(len(cmd)==2):
                        obj.read(cmd[1])
                    elif(len(cmd)==3):
                        obj.read(cmd[1],int(cmd[2]))
                    elif(len(cmd)==4):
                        obj.read(cmd[1],int(cmd[2]),int(cmd[3]))
                else:
                    print("Usage:read path offset size")
                 
            except:
                print("invalid input:offset,data-int values. Usage:read path offset size")
                pass
        
            
       
        
        elif cmd[0]=="write":
           
            if cmd[-1].isdigit() and len(cmd)>=4:
                    
                data=""
                for i in range(2,len(cmd)-1):
                    data+=cmd[i]+" "
                    
                obj.write(cmd[1],data,int(cmd[-1]))
            elif len(cmd)>=4:
                data=""
                for i in range(2,len(cmd)):
                    data+=cmd[i]+" "
                    
                obj.write(cmd[1],data)
            elif len(cmd)==3:
                obj.write(cmd[1],cmd[2])
            else:
                print("Usage:write path data length")
            
            

        else:
            skip=0
            for each in cmd[0]:
                if each.isupper():
                    print "use small case for command name"
                    skip=1
                    break
            if skip==0:
                print("Command not found")
   
