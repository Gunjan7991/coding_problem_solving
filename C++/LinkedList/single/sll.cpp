#include<iostream>
#include<string>
#include "sll.h"

using namespace std;
sll::sll(){
	
	head = NULL;
	tail = NULL;
}

sll::~sll(){
	if(!isEmpty()){
		node * currentNode = head, *nextNode = NULL;
		while(currentNode != NULL){
			nextNode = currentNode->next;
			delete currentNode;
			currentNode = nextNode;
		}
		head = NULL;
		tail = NULL;
	}
}

bool sll::isEmpty(){
	if(head  == NULL){
		return true;
	}
	else{
		return false;
	}
	
}

node* sll::createNode(int num, string nam){
	node* newNode = new node;
	newNode->data = num;
	newNode->name = nam;
	newNode->next = NULL;
	return newNode;
}

void sll::insertFront(int num, string nam){
	node* newNode = createNode(num, nam);
	if(isEmpty()){
		head = newNode;
		tail = newNode;
	}
	else{
		node* currNode = head;
		head = newNode;
		newNode->next = currNode;
	}
}

void sll::insertBack(int num, string nam){
	node* newNode = createNode(num, nam);
	if(isEmpty()){
		head = newNode;
		tail = newNode;
	}
	else{
		node* currNode = tail;
		currNode->next = newNode;
		currNode = currNode->next;
		tail = currNode;
	}
}

void sll::printHead(){
	node* currNode = head;
	cout<<"HEAD : "<<currNode->data<<endl;
	
}

void sll::printTail(){
	node* currNode = tail;
	cout<<"TAIL : "<<currNode->data<<endl;
	
}

void sll::printList(){
	node* currNode = head;
	while(currNode != NULL){
		cout<<currNode->data<<" : "<<currNode->name<<endl;
		currNode = currNode->next;
	}
	
}

void sll::delNode(int num){
	node *currNode = head, *nextNode = NULL;
	bool found = true;
	if(isEmpty()){
		cout<<"List is empty"<<endl;
	}
	else{
		if(head->data == num){
			delete currNode;
			if( head->next == NULL){
				head = NULL;
			}
			else{
				head = head->next;
			}
				cout<<"Node deleted"<<endl;
		}
		else if(tail->data == num){
			nextNode = currNode->next;
			if(nextNode == NULL){
				cout<<"node not found!!!"<<endl;
			}
			else{
				while(nextNode->next !=  NULL){
					currNode = nextNode;
					nextNode = nextNode->next;
				}
				tail = currNode;
				currNode->next = NULL;
				delete nextNode;
				cout<<"Node deleted"<<endl;
			}
		}
		else{
			nextNode = currNode->next;
			if(nextNode == NULL){
				cout<<"node not found!!!"<<endl;
			}
			else{
				while(nextNode->data !=  num){
					currNode = nextNode;
					nextNode = nextNode->next;
					if(nextNode == NULL){
						found  = false;
						break;
					}
				}
				if (found){
					currNode->next = nextNode->next;
					delete nextNode;
					cout<<"Node deleted"<<endl;
				}
				else{
					cout<<"node not found!!!"<<endl;
				}
			
			}
			
		}
	}
	
	
}


void sll::searchNode(int num){
	node *currNode = head, *nextNode = NULL;
	bool found = true;
	if(isEmpty()){
		cout<<"node not found!!!"<<endl;
	}
	else{
		if(head->data == num){
			cout<<"node Found"<<endl;
		}
		else if(tail->data == num){
			nextNode = currNode->next;
			if(nextNode == NULL){
				cout<<"node not found!!!"<<endl;
			}
			else{
				while(nextNode->next !=  NULL){
					currNode = nextNode;
					nextNode = nextNode->next;
				}
				cout<<"node Found"<<endl;
			}
		}
		else{
			nextNode = currNode->next;
			if(nextNode == NULL){
				cout<<"node not found!!!"<<endl;
			}
			else{
				while(nextNode->data !=  num){
					currNode = nextNode;
					nextNode = nextNode->next;
					if(nextNode == NULL){
						found  = false;
						break;
					}
				}
				if (found){
					cout<<"node Found"<<endl;
				}
				else{
					cout<<"node not found!!!"<<endl;
				}
			}
		}
	}
	
	
}
























