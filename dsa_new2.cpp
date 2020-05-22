#include <iostream>
#include <queue>
using namespace std;



class avlNode{

	public:

	int data;
	avlNode* left = NULL; 
	avlNode* right = NULL;
	int height = 1;


	avlNode(int key){
		this->data = key;
		this->height = 1;	
	}

	friend class AVLTree;

};

class AVLTree{

	public:
	
	avlNode* root = NULL;
	
	AVLTree(){

	}

	int max(int a, int b){
		return (a>b)?a:b;
	}

	int height(avlNode* Node){  
	    return ((Node == NULL)? 0: Node->height);  
	} 

	int getBalance(avlNode *N){
		return ((N == NULL)?0:(height(N->left)-height(N->right)));
	} 


	avlNode* rightRotate(avlNode* root){

		avlNode* y = root;
		avlNode* x = root->left;

		avlNode* T2 = x->right;
		x->right = y;
		y->left = T2;

		y->height = max(height(y->left), 
                    height(y->right)) + 1;  
    	x->height = max(height(x->left), 
                    height(x->right)) + 1;  

		return x;

	}


	avlNode* leftRotate(avlNode* root){

		avlNode* x = root;
		avlNode* y = root->right;

		avlNode* T2 = y->left;
		y->left = x;
		x->right = T2;

		y->height = max(height(y->left), 
                    height(y->right)) + 1;  
    	x->height = max(height(x->left), 
                    height(x->right)) + 1;  

		return y;

	}
	
	void preOrder(avlNode *root)  
	{  
	    if(root != NULL)  
	    {  
	        cout << root->data << " ";  
	        preOrder(root->left);  
	        preOrder(root->right);  
	    }  
	}  

	void printLevel(avlNode* root){
		if(root == NULL) return;

		queue<avlNode *> q;
		q.push(root);

		while(q.empty() == false){

			int nodeCount = q.size();

			for (int i = 0; i < nodeCount; i++)
			{
				avlNode* n = q.front();
				cout<< n->data<<" ";
				q.pop();

				if (n->left!=NULL){
					cout<<"(L:"<<n->left->data<<",";
					q.push(n->left);
				}
				
				if (n->right!=NULL){
					cout<<"R:"<<n->right->data<<")\t";
					q.push(n->right);
				}
				

			}
			cout<<endl;
		}


	}

	avlNode* avlBalancing(avlNode* root, int key){
		
		root->height = 1 + max(height(root->left),height(root->right));		
		int balance = getBalance(root);
			 
		if(balance > 1){
			
			// Left Left Case 
		    if (key < root->left->data)  
		        return rightRotate(root);  

		     // Left Right Case  
		    if (key > root->left->data){  
		        root->left = leftRotate(root->left);  
		        return rightRotate(root);  
		    }
	    }  
	  
	    if(balance < -1){

	    	// Right Left Case  
		    if (key < root->right->data){  
		        root->right = rightRotate(root->right);  
		        return leftRotate(root);  
		    }  

		    // Right Right Case  
		    if (key > root->right->data)  
		        return leftRotate(root);  
		  
		}

		return root;

	}

	avlNode* insert(avlNode* root, int key){
		if(root== NULL)
			return new avlNode(key);

		if(key < root->data){			
			root->left = insert(root->left,key); 
		}

		else if(key > root->data){
			root->right = insert(root->right,key);
		}
		else{
			return root;
		}
		
		return avlBalancing(root, key);

	}

	avlNode* findMin(avlNode* root){
		
		avlNode* current = root;

		while(current && current->left != NULL){
			current = current->left;
		}
		return current;

	}

	avlNode* deleteKey(avlNode* root, int key){
		if(root == NULL){
			return root;
		}

		if(key < root->data){
			root->left = deleteKey(root->left,key);
			return root;
		}

		else if(key > root->data){
			root->right = deleteKey(root->right,key);
			return root;
		}

		// found the key

		if(root->left == NULL && root->right == NULL){
			delete root;
			return root;
		}
		else if(root->left == NULL){
			avlNode* temp = root->right;
			delete root;
			return temp;
		}
		else if(root->right == NULL){
			avlNode* temp = root->left;
			delete root;
			return temp;
		}
		else{

			avlNode* temp = findMin(root->right);
			root->data = temp->data;
			root->right = deleteKey(root->right, temp->data);
			return root;
		}

		return avlBalancing(root,key);

	}


};


void run(){

AVLTree bt;
avlNode* btn = NULL;

btn = bt.insert(btn,10);
btn = bt.insert(btn,20);
btn = bt.insert(btn,30);
btn = bt.insert(btn,40);
btn = bt.insert(btn,50);
btn = bt.insert(btn,60);
btn = bt.insert(btn,70);
btn = bt.insert(btn,80);

bt.printLevel(btn);
btn = bt.deleteKey(btn, 60);
bt.printLevel(btn);


}









// 
int main(){
run();
std::cout<<"\n";
return 0;
}
