import SimpleXMLRPCServer,Memory,pickle,sys

filesystem=Memory.Operations()

def check_status():
    return "Alive"

def main():
	try:
		portno=0
		if len(sys.argv)==2:
			if sys.argv[1].isdigit():
				portno=int(sys.argv[1])
				pass
			else:
				print ("Usage: python filename portno")
				exit(0)
		else:
			print ("Usage: python filename portno")
			exit(0)
		server=SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",portno),allow_none=True)
		print ("Listening on port "+str(portno)+"....")
		server.register_function(check_status)
		server.register_function(Memory.Initialize)
		server.register_function(filesystem.inode_number_to_inode)
		server.register_function(filesystem.get_data_block)
		server.register_function(filesystem.get_valid_data_block)
		server.register_function(filesystem.free_data_block)
		server.register_function(filesystem.update_data_block)
		server.register_function(filesystem.update_inode_table)
		server.register_function(filesystem.status)
		server.serve_forever()
	except:
		
		print("Error occurred")

if __name__ == "__main__":
	main()

