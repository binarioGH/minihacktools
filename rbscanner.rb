require "socket"
require "timeout"
class String
  def red; colorize(self, "\e[1m\e[31m"); end
  def green; colorize(self, "\e[1m\e[32m"); end
  def colorize(text, color_code) "#{color_code}#{text}\e[0m" end
end
class Main
	def initialize()
		if ARGV.length == 1 && ARGV[0] == "-h"
			self.h
		elsif ARGV.length == 6
			argcount = 0
			mn = 0
			mx = 0
			ip = ""
			ARGV.each do |arg|
				if arg[0] != "-"
					argcount += 1
					next
				elsif arg == "-mn"
					mn = ARGV[argcount + 1]
				elsif arg == "-mx"
					mx = ARGV[argcount + 1]
				elsif arg == "-i"
					ip = ARGV[argcount + 1]
				else
					puts("Por favor usa -h para ver las opciones.")
					exit
				end
				argcount += 1
			end
			self.scann(ip, mn, mx)
		end
	end
	def h()
		puts("Escaner de puertos con ruby.")
		puts("Opciones:\n-h: Ver opciones.\n-i: Determinar la ip del objetivo.")
		puts("-mn: Poner el primer puerto que se scanneara\n-mx: El utimo puerto que se va a escanear.")
		exit
	end
	def scann(ip, min, max)
		min = min.to_i
		max = max.to_i
		ports = min..max
		ports.each do |port|
			begin
				Timeout::timeout(5){TCPSocket.new(ip.to_s, port.to_i)}
			rescue
				puts("[-]".red() +"Puerto #{port} cerrado.")
			else
				puts("[+]".green() + "Puerto #{port} abierto.")
			end
		end
	end
end

start = Main.new()