#include<iostream>
#include<string>
#include "dll.h"

using namespace std;

dll::dll(){
	head = NULL;
	tail =NULL;
}

dll::~dll(){
	if(!isEmpty()){
		node *currentNode = head, *nextNode = NULL;
		do{
			nextNode = currentNode->next;
			delete currentNode;
			currentNode = nextNode;
		}while(currentNode != NULL);
		head = NULL;
		tail = NULL;
	}
}

bool dll::isEmpty(){
	if(head == NULL){
		return true;
	}
	else{
		return false;
	}
}

 
node* dll::createNode(int i, string n){ // i is id and n is name.
	node *newNode = new  node;
	newNode->data = i;
	newNode->name = n;
	newNode->next = NULL;
	newNode->prev = NULL;
	return newNode;
	
}


void dll::insertFront(int i, string n){ // i is id and n is name;
	node *newNode = createNode(i,n);
	if(isEmpty()){
		head = newNode;
		tail = newNode;
	}
	else{
		node *currentNode = head;
		head = newNode;
		head->next = currentNode;
		currentNode->prev = head;
	}
	
}


void dll::insertBack(int i, string n){// i is id and n is name;
	node *newNode = createNode(i,n);
	if(isEmpty()){
		head = newNode;
		tail = newNode;
	}
	else{
		node *currentNode = tail;
		tail = newNode;
		tail->prev = currentNode;
		currentNode->next = tail;	
	}
	
	
}


void dll::printList(){

	if(!isEmpty()){
		node *currentNode = head;
		while(currentNode!=NULL){
			cout<<currentNode->data<<"  ::  "<<currentNode->name<<endl;
			currentNode = currentNode->next;
		}
	}
	else{
		cout<<" List is Empty \n";
	}
}


void dll::printHead(){
	if(!isEmpty()){
		cout<<" Head -> " <<head->data<<" :: "<< head->name<<endl;
	}
}


void dll::printTail(){
	if(!isEmpty()){
		cout<<" Tail -> " <<tail->data<<" :: "<< tail->name<<endl;
	}
}


void dll::delNode(int num){
	
	if(isEmpty()){
		cout<<"List is empty"<<endl;
	}
	else{
		node *currNode = NULL, *baseNode= NULL;
		bool found = true;
		if(head->data == num){
			currNode = head;
			if( head->next == NULL){
				head = NULL;
				tail = NULL;
			}
			else{
				head = head->next;
			}
			delete currNode;
			cout<<"Node deleted"<<endl;
		}
		else if(tail->data == num){
			currNode = tail;
			tail = tail->prev;
			tail->next = NULL;
			delete currNode;
			cout<<"Node deleted"<<endl;
		}
		else{
			currNode = head;
			if(currNode->next == NULL){
				cout<<"node not found!!!"<<endl;
			}
			else{
				while(currNode->data !=  num){
					currNode = currNode->next;
					if(currNode == NULL){
						found  = false;
						break;
					}
				}
				if (found){
					baseNode = currNode->prev;
					baseNode->next = currNode->next;
					currNode->next->prev = baseNode;
					delete currNode;
					cout<<"Node deleted"<<endl;
				}
				else{
					cout<<"node not found!!!"<<endl;
				}
			
			}
			
		}
	}
	
}


void dll::searchNode(int num){
	if(isEmpty()){
		cout<<"node not found!!!"<<endl;
	}
	else{
		node *currNode = head, *nextNode = NULL;
		bool found = true;
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




