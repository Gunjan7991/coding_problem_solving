#include "node.h"
#include <string>
using namespace std;
class dll{
	private:
		node* head;
		node* tail;
	public:
		dll();  	//constructor
		~dll();		//destructor
		
		bool isEmpty();
		node* createNode(int, string);
		void insertNode();
		void insertFront(int, string);
		void insertBack(int, string);
		void printList();
		void delNode(int);
		void searchNode(int);
		
		void printHead();
		void printTail();
		
	
};