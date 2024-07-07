#include<bits/stdc++.h>
using namespace std;
int gcd(int a , int b){
	if( a==0 ) return b;
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
	int q[100], s[100], t[100];
	int r2 = -1;
	int i = 0;
	while(r2!=0){
		r2 = r%r1;
		q[i+1] = r/r1;
		switch(i){
			case 0:
				s[i] = 1;
				t[i] = 0;
				break;
			case 1:
				s[i] = 0;
				t[i]= 1;
				break;
			default:
				s[i] = s[i-2] - q[i-1]*s[i-1];
				t[i] = t[i-2] - q[i-1]*t[i-1];
				break;
		}
		r = r1;
		r1=r2;
		i++;
	}
	s[i] = s[i-2] - q[i-1]*s[i-1];
	t[i] = t[i-2] - q[i-1]*t[i-1];
	if(t[i] >0) return t[i];
	return t[i] + p;
}

string mahoa(string banro, int a, int b){
	string banma = "";
	for(int i = 0; i < banro.length(); i++){
		if(islower(banro[i])){
			banma+= (char)((a * (banro[i] - 'a') + b) %26 + 'a');
		}
		else if(banro[i] ==' ') banma+= ' ';
		else banma+= (char)((a * (banro[i] - 'A') + b) %26 + 'A');
	}
	return banma;
}
string giaima(string banma, int a, int b){
	string banro = "";
	int a_inv = oclitmr(26,a);
	for(int i = 0; i < banma.length(); i++){
		if(banma[i] == ' ') banro+=' ';
		else if(islower(banma[i])) banro+= (char) (( a_inv*(banma[i] - 'a' - b + 26)%26))+'a';
		else banro+= (char) (( a_inv*(banma[i] - 'A' - b + 26)%26))+'A';
	}
	return banro;
}
int main(){
	int a, b;
	do{
		cout << "Nhap a: "; cin >>a;
		cout << "Nhap b: "; cin >> b;
		if(gcd(26,a)!=1){
			cout << "Khong co modulo nghich dao cua " << a << endl << "Nhap lai" << endl; 
		}
	}while(gcd(26,a)!=1);
	cin.ignore();
	int a_inv = oclitmr(26,a);
	cout << "Khoa (" << a_inv << ", " << b << ")" << endl;
	string s1,s2;
	cout << "Nhap vao xau 1: "; getline(cin, s1);
	//cout << s1; 
	
	cout << "Nhap vao xau 2: "; getline(cin, s2);
	cout << "s1 " << s1 <<" s2 " << s2<< endl;
	string tmp = giaima(s2,a,b);
	cout << "TMP " << tmp << endl;
	if(s1.compare(tmp)==0 ) cout << "Ban da nhap dung";
	else cout << "Ban da nhap sai"; 
//	string banma = mahoa("ATTACK", a, b);
//	cout <<giaima(banma,a,b);
}