#include<bits/stdc++.h>

using namespace std;
int gcd(int a, int b){
	if(a==0) return b;
	if(b==0) return a;
	while(b!=0){
		int temp = a%b;
		a = b;
		b = temp;
		
	}
	return a;
}
int oclitmr(int r, int r1){
	int p = r;
	int q[100];
	int s[100];
	int t[100];
	int r2 = -1, i =0;
	
	while(r2!=0){
		q[i+1] = r/r1;
		r2 = r%r1;
		switch(i){
			case 0:
				s[i] = 1;
				t[i] = 0;break;
			case 1:
				s[i] = 0;
				t[i] = 1; break;
			default:
				s[i] = s[i-2]  - q[i-1] * s[i-1];
				t[i] = t[i-2] - q[i-1] * t[i-1]; 
				break;
		}
		r = r1;
		r1 = r2;
		i++;
		//cout << i<< endl;
	
	}
		s[i] = s[i-2]  - q[i-1] * s[i-1];
		t[i] = t[i-2] - q[i-1] * t[i-1]; 
		
		//cout << t[i] << endl;
	
	if(t[i] > 0) return t[i];
	return t[i]+p;
}

string mahoa(string banro, int a, int b){
	string banma = "";
	for(int i = 0; i < banro.length();i++){
		if(islower(banro[i]))
			banma +=(char)(((a * (banro[i] - 'a')) + b) %26 + 'a');
		else if(banro[i] == ' ') banma+=' ';
		else banma +=(char) (((a * (banro[i] - 'A') )+ b)%26 + 'A');
	}
	return banma;
}
string giaima(string banma, int a, int b){
	int x = oclitmr(26,a);
	string cipher = "";
	for(int i = 0; i < banma.length(); i++){
		if( islower(banma[i])){
			cipher+= (char)(((x * (banma[i] - 'a' - b + 26))%26) + 'a');
		}
		else if(banma[i]==' ') cipher+=' ';
		else{
			cipher+=  (char)(((x * (banma[i] - 'A' - b + 26))%26) + 'A');
			//cipher += (char)(((x * (banma[i] - 'A' - b + 26)) % 26) + 'A');
		}
	}
	return cipher;
}

int main(){
	string msg = "Nghia dz vc";
	int a = 17;
	int b = 20;
	if(gcd(26,a)!=1){
		cout << "ko =  1"; return 0;
	}
	string banma = mahoa(msg,a,b);
	cout << banma<< endl;
	cout << giaima(banma,a,b);
}