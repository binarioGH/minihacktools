require "socket"
class Server
	def initialize()
		server = TCPServer.open("127.0.0.1", 5000)
		loop{
			Thread.start(server.accept) do |recv|
				cmd = recv.gets
				system(cmd)
			end
		}
	end
end
iniciar = Server.new()