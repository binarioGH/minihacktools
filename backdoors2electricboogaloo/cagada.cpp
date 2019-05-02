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
	bind(sock, (SOCKADDR*)&addr, sizeof(addr));
	listen(sock, SOMAXCONN);
	SOCKET conn;
	conn = accept(sock, (SOCKADDR*)&addr, &addrl);
	char cmd[255];
	while(cmd != "exit"){
		cout<<"->";
		cin.getline(cmd, 255);
		send(conn, cmd, sizeof(conn), 0);
	}
	closesocket(sock);
	closesocket(conn);
	return 0;
}