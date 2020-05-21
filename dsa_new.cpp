#include <iostream>
#include <queue>
using namespace std;


class Node
{
	public:
	int data; Node* next;
	Node(int d){
		this->data = d;
		this->next = NULL;
	}
	~Node(){
		cout<<"\n\n destroying "<<this->data<<"\n";
	}
};

class LinkedList{
	private:
		Node* start = NULL;
	public:
		LinkedList(){
		}

	void printLL(){

		Node* i = start;
		cout<<"\n Printing out the LinkedList \n ";
		while(i!=NULL)
		{
			cout << " " << i->data<<" ";
			i = i->next;
		}
	}	


	void insertBeg(int key){
		if(start == NULL){
			start = new Node(key);
		}else{

			Node* temp = new Node(key);
			temp->next = start;
			start = temp;

		}
	}

	
	void insertend(int key){
		if(start == NULL){
			start = new Node(key);
		}else{
			Node* i = this->start;
		
			while(i->next != NULL)
				i = i->next;
		
			i->next = new Node(key);
		}
	}

	void insertAfter(int key, int val){
		
		Node* i = start;
		Node* temp = new Node(key);
		
		// search the val first
		while(i->next != NULL ){
			if(i->data == val)
				break;
			i = i->next;
		}

		temp->next =  i->next;
		i->next = temp;
	}


	void deleteKey(int val){
		Node* i = start;
		while(i->next != NULL){
			if(i->next->data == val)
				break;

			i = i->next;
		}

		Node* temp = i->next;
		i->next = i->next->next;

		delete temp;
	}

};



class Stack{

	private:
		Node* top = NULL;
	public:
		
		Stack(){

		}

		// Insert at begining
		void push(int key){
			if(top == NULL){
				top = new Node(key);
			}else{
				Node* temp = new Node(key);
				temp->next = top;
				top = temp;
			}
		}



		void peek(){
			cout<<"Top of the stack : "<<top->data<<"\n";
		}

		// deletion at beginning
		void pop(){
			
			if(top!=NULL){
				peek();
				Node* temp = top;
				top = top->next;
				delete temp;
			}
			
		}

		void printStack(){
			Node* i = top;
			cout<<"\nPrinting out the Stack \n ";

			while(i!=NULL){
				cout<<"  "<<i->data<<" ";
			 	i = i->next;
			}

			cout<<endl;
		}
};

class Queue
{
	Node* top = NULL;
	
	public:
	
	Queue(){		

	}

	void push(int key){
		if(top == NULL){
			top = new Node(key);
		}
		else{
			Node* temp = new Node(key);
			temp->next = top;
			top = temp;

		}

	}

	void printQueue(){
		Node* i = top;
		cout<<"\nPrinting out the Queue\n";
		while(i!=NULL){
			cout<<" "<<i->data<<" ";
			i = i->next;
		}

	}

	void pop(){


		Node* i = top;
		while(i->next->next!=NULL){
			i = i->next;
		}
		Node* temp = i->next;
		i->next = NULL;
		delete temp;
	}
	
};


class BTNode{
	int data;
	BTNode* left = NULL; 
	BTNode* right = NULL;


	public:

	BTNode(){}

	BTNode(int key){
		this->data = key;	
	}

	friend class BinaryTree;

};

class BinaryTree{

	public:

	int maxHt = 0,minW = 0;
	int** printBox = NULL;

	
	BTNode* root = NULL;
	
	BinaryTree(){

	}


	void printTree(BTNode* root, int ht, int w){
		if(root!=NULL)
		{
			printTree(root->left, ht+1+1, w-1-1);

			/*	
			cout<<" (data: "<<root->data<<" ";
			if(root->left!=NULL){
				cout<<"$(L:"<<root->left->data<<")";
			}else{
				cout<<"$(L:@)";
			}
			if(root->right!=NULL){
				cout<<"$(R:"<<root->right->data<<")";
			}else{
				cout<<"$(R:@)";
			}*/


			maxHt = (ht>maxHt)?ht:maxHt;
			minW = (w<minW)?w:minW;

			if(printBox!=NULL){
				// cout<<" Adding "<<root->data<<" to ("<<ht<<","<<w<<")"; 
				// shift data to the right if already exists
				if(printBox[ht][w] != 0)
					printBox[ht][w+1] = root->data;
				else
					printBox[ht][w] = root->data;
				

				if(root->left!=NULL){printBox[ht+1][w-1] = -119;}
				if(root->right!=NULL){printBox[ht+1][w] = +119;}
			
			}

			// cout<<" ht: "<<ht<<" wd: "<<w<<")\n";

			printTree(root->right, ht+1+1,w+1+1);
		}		
	}

	void printLevel(BTNode* root){

		if(root == NULL) return;

		queue<BTNode* > q;
		q.push(root);

		BTNode* temp = new BTNode(-1);

		while(q.empty() == false){

			int nodeCount = q.size();  
				for (int i = 0; i < nodeCount; ++i)
				{
					BTNode *BTNode = q.front();  
	            	if(BTNode->data == -1)
	            	 cout<<"  ";
	            	else 
            		  cout<<BTNode->data<<" ";  
	            	
	            	q.pop();  

	            	if(BTNode->left != NULL && BTNode->right != NULL){
	            		q.push(BTNode->left);
	            		q.push(BTNode->right);
	            	}
	            	else if(BTNode->left != NULL && BTNode->right == NULL){
	            		q.push(BTNode->left);
	            		q.push(temp);
	            	}
	            	else if(BTNode->left == NULL && BTNode->right != NULL){
	            		q.push(temp);
	            		q.push(BTNode->right);
	            	}
	                	 
				}	
	 
		    cout << endl;  
		}
	}

	void initPrinter(int ht){
		printBox = new int*[ht];
		
		for(int i = 0; i <= ht; i++) {
	    	printBox[i] = new int[ht];
		}
	}	

	void stylePrint(){

		for (int i = 0; i < maxHt; ++i)
		{
			for(int j = 0; j <= maxHt; j++){
				if(printBox[i][j] == 0){cout<<" "<<" ";}
				else if(printBox[i][j] == 119){cout<<" \\ " <<" ";}
				else if(printBox[i][j] == -119){cout<<" /"<<" ";}
				else{cout<<" "<<printBox[i][j]<<" ";}
			}
			cout<<endl;
		}
	}

	void drawTree(BTNode* root){
		this->printTree(root,0,0);
		cout<<"\nPrinting Binary Search Tree:\n";
		this->maxHt*=2;
		this->maxHt++;
		this->initPrinter(this->maxHt);
		this->printTree(root,0,-this->minW);
		cout<<"\n";
		this->stylePrint();
		cout<<"\n";
	}


	BTNode* insert(BTNode* root,int key){
		if(root == NULL){
			root = new BTNode(key);
			
		}else{
			if(key > root->data){
				root->right = insert(root->right,key);
			}
			else if(key < root->data){
				root->left = insert(root->left, key);
			}
		}
		return root;
	}



	BTNode* InOrderSuccessor(BTNode* root){

		BTNode* current = root;

		while(current && current->left!=NULL){
			current = current->left;
		}

		return current;

	}


	BTNode* deleteKey(BTNode* root,int key){
		
		if(root == NULL){ 
			return root;
		}
		if(key < root->data){ 
			root->left = deleteKey(root->left, key);
			return root;
		}
		else if(key > root->data){	
			root->right = deleteKey(root->right,key);
			return root;
		}
		else{

			// found the key	

			//	no child, direct delete
			if(root->left == NULL && root->right == NULL){
				delete root;
				return NULL;
			}

			// only left child
			if(root->left == NULL)
			{
				BTNode* temp = root->right;
				delete root;
				return temp;
			}
			// only right child
			else if(root->right == NULL)
			{
				BTNode* temp = root->left;
				delete root;
				return temp;
			}
			// both child
			else{

				// inorder successor will always be the leaf node
				BTNode* temp = InOrderSuccessor(root->right);
				root->data = temp->data;
				// delete recursively
				root->right = deleteKey(root->right, temp->data);
				return root;


			}

			
		}

	}

};


void run(){

BinaryTree bt;
BTNode* btn = NULL;

btn = bt.insert(btn,5);
btn = bt.insert(btn,3);
btn = bt.insert(btn,2);
btn = bt.insert(btn,4);
btn = bt.insert(btn,7);
btn = bt.insert(btn,6);
btn = bt.insert(btn,8);

// bt.drawTree(btn);
bt.drawTree(btn);

cout<<"Delete 5";
btn = bt.deleteKey(btn, 5);
bt.drawTree(btn);

cout<<"Delete 7";
btn = bt.deleteKey(btn, 7);
bt.drawTree(btn);

cout<<"Delete 4";
btn = bt.deleteKey(btn, 4);
bt.drawTree(btn);

// bt.drawTree(btn);
// Linear DS

/*LinkedList ll;
ll.insertend(1);
ll.insertend(2);
ll.printLL();
ll.insertBeg(3);
ll.insertAfter(5,1);
ll.printLL();
ll.deleteKey(5);
ll.insertBeg(11);
ll.printLL();
*/


/*Stack st;
st.push(1);
st.push(2);
st.push(3);
st.push(4);
st.printStack();
st.peek();
st.pop();
st.printStack();
st.pop();
st.printStack();*/

/*Queue qq;
qq.push(1);
qq.push(2);
qq.push(3);
qq.push(4);
qq.printQueue();
qq.pop();
qq.printQueue();*/


}









// 
int main(){
run();
std::cout<<"\n";
return 0;
}
