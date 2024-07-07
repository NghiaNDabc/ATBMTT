#include<bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
	if(a==0) return b;
	if(b==0) return a;
	while(b!=0){
		int tmp = a%b;
		a = b;
		b = tmp;
	}
	return a;
}

int oclitmr(int r, int r1){
	int p = r;
	int s[100], q[100], t[100];
	int r2 = -1, i = 0;
	while(r2!=0){
		q[i+1]  = r/r1;
		r2 = r%r1;
		switch(i){
			case 0:
				s[i] = 1;
				t[i] = 0;
				break;
			case 1:
				s[i] = 0;
				t[i] = 1;
				break;
			default:
				s[i] = s[i-2] - q[i-1] * s[i-1];
				t[i] = s[i-2] - q[i-1] * t[i-1];
				break;
		}
		r = r1;
		r1= r2;
		i++;
	}
	s[i] = s[i-2] - q[i-1] * s[i-1];
	t[i] = s[i-2] - q[i-1] * t[i-1];
	if(t[i]>0) return t[i];
	return t[i] + p;	
}

void getKeyMatrix(string key, int keyMaTrix[][3]){
	int k = 0;
	for(int i = 0; i < 3; i++)
	{
		for(int j = 0; j < 3; j++){
			keyMaTrix[i][j] = key[k]%65;
			k++;
		}
	}
}
void encrypt(int cipherMatrix[][1], int keyMatrix[][3], int message[][1]){
	for(int i = 0; i < 3; i++){
		cipherMatrix[i][0] =  0;
		for(int x = 0; x < 3; x++){
			cipherMatrix[i][0] += message[x][0] * keyMatrix[i][x];
			
		}
		cipherMatrix[i][0]= cipherMatrix[i][0]%26;	
		
	}
}
string hill(string mess, string key){
	int keyMatrix[3][3];
	
	getKeyMatrix(key, keyMatrix);
	int messageVector[3][1];
	for(int i = 0; i < 3;i++){
		messageVector[i][0] = mess[i]%65;
		
	}
	cout << endl;
	int cipherMatrix[3][1];
	encrypt(cipherMatrix,keyMatrix,messageVector);
	string cipher;
	for(int i = 0; i < 3;i++)
		cipher+=cipherMatrix[i][0] + 65;
	return cipher;
}
int main(){
	string key = "GYBNQKURP";
	string mess = "ACT";
	int keyMatrix[3][3];
	cout << hill(mess,key);
}