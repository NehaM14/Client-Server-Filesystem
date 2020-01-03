import xmlrpclib, config, pickle,datetime,time,socket
#10.0.2.15

# pass all parameters using pickle.dumps(parameter)
# get all return values using pickle.loads(return value)

#HANDLE FOR MEMORY OPERATIONS
port1=0
proxy1=xmlrpclib.ServerProxy("http://localhost:"+str(port1)+"/",allow_none=True)

class Server():
    server_in_use=0

# PORT NUMBERS
def update_server():
    global port1, proxy1
    port1 = Server.server_in_use
    proxy1 = xmlrpclib.ServerProxy("http://localhost:" + str(port1) + "/", allow_none=True)

def check_server_status():
    try:
        return_value = ""
        update_server()
        return_value = proxy1.status()
    except:
        pass
    if return_value == "Alive":
        return 0
    return -1

class client_stub():

	# REQUEST TO BOOT THE FILE SYSTEM
	def Initialize_My_FileSystem():

		try:
			print("File System Initializing......")
			time.sleep(2)
			# global port1
			global proxy1
			update_server()
			state = proxy1.Initialize()
			print("File System Initialized!")
		except socket.error as error:
			if error.errno == 113:
				print "Server may be temporarily down.Try again after some time"
			elif error.errno == 111:
				print "Cannot connect to the server.Try again after some time"
			exit(0)
		except:
			print "Error occured"
			exit(0)

	def addr_inode_table(self):
			try :
				return self.proxy.addr_inode_table()
			except Exception as err :
				print('connection error')
				return -1

	def get_data_block(block_number,server_number):
		try :
			retVal =  self.proxy.get_data_block(pickle.dumps(block_number))
		except Exception as err :
			print('connection error')
			return -1
			
		retVal =  pickle.loads(retVal)
		return retVal

	def get_valid_data_block(server_number):
		try :
			retVal = self.proxy.get_valid_data_block()
		except Exception as err :
			print('connection error')
			return -1
		retVal = pickle.loads(retVal)
		return retVal

	def free_data_block(self, block_number, server_number):
		try :
			retVal =  self.proxy.free_data_block(pickle.dumps(block_number))
		except Exception as err :
			print('connection error')
			return -1
		retVal =  pickle.loads(retVal)
		return retVal

	def update_data_block(block_number, block_data, server_number):
		try :
			retVal =  self.proxy.update_data_block(pickle.dumps(block_number), pickle.dumps(block_data))
		except Exception as err :
			print('connection error')
			return -1
		retVal =  pickle.loads(retVal)
		return retVal

	def update_inode_table(self, inode, inode_number):
		try :
			retVal =  self.proxy.update_inode_table(pickle.dumps(inode), pickle.dumps(inode_number))
		except Exception as err :
			print('connection error')
			return -1
		retVal =  pickle.loads(retVal)
		return retVal

	def inode_number_to_inode(self, inode_number):
		try :
			retVal = self.proxy.inode_number_to_inode(pickle.dumps(inode_number))
		except Exception as err :
			print('connection error')
			return -1
		retVal = pickle.loads(retVal)
		return retVal

	def status(self):
		try :
			retVal = self.proxy.status()
		except Exception as err :
			print('connection error')
			return -1
		retVal = pickle.loads(retVal)
		return retVal

	def configure(self):
		try:
			retVal = self.proxy.configure()
		except Exception as err:
			print('connection error')
			return -1
		retVal = pickle.loads(retVal)
		return retVal


#print "3 is even: %s" % str(proxy.is_even(3))
#print "100 is even: %s" % str(proxy.is_even(100))
