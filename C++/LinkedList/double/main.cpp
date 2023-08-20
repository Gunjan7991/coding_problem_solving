#include <iostream>
#include <string>

#include "dll.h"

using namespace std;
void displayMenu();

int main(){
	dll list;
	int choice;
	do{
		int id;
		string name;
		displayMenu();
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"enter the id: ";
				cin>>id;
				cin.ignore();
				cout<<"Enter the name: ";
				getline(cin, name);
				list.insertFront(id, name);
				cout<<"List Updated"<<endl;
				break;
				
			case 2:
				cout<<"enter the id: ";
				cin>>id;
				cin.ignore();
				cout<<"Enter the name: ";
				getline(cin, name);
				list.insertBack(id, name);
				cout<<"List Updated"<<endl;
				break;
				
			case 3:
				cout<<"enter the id: ";
				cin>>id;
				list.delNode(id);
				break;
				
			case 4:
				cout<<"enter the id: ";
				cin>>id;
				list.searchNode(id);
				break;
			
			case 5:
				list.printList();
				break;
				
			case 6:
				list.printHead();
				break;
				
			case 7:
				list.printTail();
				break;
				
			case 0:
				cout<<"program terminated\n";
				break;
			
			default:
				cout<<"Wrong choice. try again..."<<endl;
				
				
		}
		
	}while(choice !=0);
	return 0;
}

void displayMenu(){
	cout<<"Enter a option form the menu:\n1) Insert in the front of the list.\n2) Instert in the back of the list.\n3) Delete a Item from the list.\n4) Search an item in the list.\n5) print list.\n6) head\n7)tail \n0) QUIT.\n:";
}