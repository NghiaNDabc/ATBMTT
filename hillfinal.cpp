#include<bits/stdc++.h>
using namespace std;
int gcd(int a, int b){
	if(a==0) return b;
	if(b==0) return a;
	while(b!=0){
		int tmp  =a%b;
		a = b;
		b = tmp;
	}	
	return a;
}

int oclitmr(int r, int r1){
	int p=r;
	int q[100], s[100], t[100];
	int r2 = -1, i = 0;
	while(r2!=0){
		q[i+1] = r/r1;
		r2 = r%r1;
		switch(i){
			case 0 :
				s[i] = 1;
				t[i] = 0;
				break;
			case 1 :
				s[i] = 0;
				t[i] =1;
				break;
			default:
				s[i] = s[i-2]- q[i-1] * s[i-1];
				t[i] = t[i-2]- q[i-1] * t[i-1];
				break;
		}
		r=r1;
		r1=r2;
		i++;
	}
	s[i] = s[i-2]- q[i-1] * s[i-1];
	t[i] = t[i-2]- q[i-1] * t[i-1];
	if(t[i]>0) return t[i];
	return t[i] + p;
}

bool checkDet(int key[][2]){
	int det = abs(key[1][1] * key[0][0] - key[1][0]*key[0][1]);
	det = det%26;
	if(gcd(26,det) != 1){
		return false;
	}
	return true;
}

bool getKhoaGiaiMa(int key_inv[][2], int key[][2]){
	int det = abs(key[1][1] * key[0][0] - key[1][0]*key[0][1]);
	det = det%26;
	// đoạn này check bỏ đi cũng đc vì check ở hàm checkdet rồi
	if(gcd(26,det) != 1){
		return false;
	}
	int det_inv = oclitmr(26,det);
	key_inv[0][0] = key[1][1];
	key_inv[1][1] = key[0][0];
	key_inv[1][0] = -key[1][0];
	key_inv[0][1] = -key[0][1];
	for(int i = 0; i< 2; i++){
		for(int j = 0; j<2; j++)
		{
			int temp = (key_inv[i][j] * det_inv)%26;
			if(temp < 0) temp+=26;
			key_inv[i][j] = temp	;
		
		}
	}
	return true;
}
string hill(string banma, int key[][2]){
	int key_inv[2][2];
	getKhoaGiaiMa(key_inv,key);
	cout << "Ma tran giai ma "<< endl ;
	for(int i = 0; i <2; i++)
	{
		for(int j = 0; j <2; j++)
			cout << key_inv[i][j];
		cout << endl;
	}
	int p = banma.length()/2;
	cout <<"p " << p << " ;" <<endl;
	string res = "";
	int temp = 0;
	while(p--){
		string ans = "";
		for(int i = 0; i < 2; i++){
			ans+= banma[temp];
			temp++;
		}
		int a[2];
		for(int i = 0 ; i < 2; i++){
			if(islower(ans[i]))
				a[i] = int(ans[i]) - 97;
			else a[i] = int(ans[i]) - 65;
		}
		int c[2];
		c[0] = (a[0] * key_inv[0][0] + a[1] * key_inv[1][0])%26;
    	c[1] = (a[0] * key_inv[0][1] + a[1] * key_inv[1][1])%26;
    	cout << c[0] << " " << c[1];
		cout << endl;
		for(int i = 0; i < 2; i++){
			if(islower(ans[i])) res+= (char) (c[i] + 'a');
			else res+= (char) (c[i] + 'A');
		}
		
	}
	return res;
}

int main(){
	int key[2][2];
	cout << "test " << oclitmr(29,8) << endl;
	do{
		cout << "Nhap a b c d: " << endl;
		for(int i = 0; i <2; i++){
			for(int j = 0; j <2; j++)
			 cin >> key[i][j];
		}
		if(checkDet(key) ==  false)
	cout << "Nhap lai" << endl;
	}while(checkDet(key) ==  false);
	string banro, banma;
	cout << "Nhap xau 1: ";
	cin.ignore();
	getline(cin,banro);
	cout << "Nhap xau 2: ";
	getline(cin,banma);
	if (hill(banma, key).compare(banro)==0)cout << "Ban nhap dung";
}