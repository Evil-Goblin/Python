#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;


int main(int argc, char const *argv[])
{
	while(1){
		char a = getch();
		// if(a == 75){
		// 	cout << "left" << endl;
		// }else if(a == 72){
		// 	cout << "up" << endl;
		// }else if(a == 80){
		// 	cout << "down" << endl;
		// }else if(a == 77){
		// 	cout << "right" << endl;
		// }else if(a == 0x1B){
		// 	break;
		// }else if ( a == 13 ){
		// 	cout << "space" << endl;
		// }else{
		// 	cout << a << endl;
		// }
		
		
		if(kbhit()){
			 a = getch();
			if(a == 75){
				cout << "left" << endl;
			}else if(a == 72){
				cout << "up" << endl;
			}else if(a == 80){
				cout << "down" << endl;
			}else if(a == 77){
				cout << "right" << endl;
			}
		}
		else if(a == 0x1B){
			break;
		}
		printf("%d\n", a);
	}
	return 0;
}