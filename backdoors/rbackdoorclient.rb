require "socket"
class Client
	def initialize()
		loop{
			print(">>>")
			cmd = $stdin.gets
			TCPSocket.open("127.0.0.1",5000).puts(cmd)
		}
	end
end
iniciar = Client.new()