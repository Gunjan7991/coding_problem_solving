#include "node.h"
#include <string>
using namespace std;
class sll{
	private:
		node* head;
		node* tail;
	public:
		sll();  	//constructor
		~sll();		//destructor
		
		bool isEmpty();
		node* createNode(int num, string nam);
		void insertNode();
		void insertFront(int num, string nam);
		void insertBack(int num, string nam);
		void printList();
		void printHead();
		void printTail();
		void delNode(int num);
		void searchNode(int num);
};