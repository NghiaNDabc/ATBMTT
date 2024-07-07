#include<bits/stdc++.h>
using namespace std;
int gcd(int a, int b){
	if(a==0) return b;
	if(b==0) return a;
	while(b!=0){
		int tmp =a%b;
		a = b;
		b = tmp;
	}
	return a;
}
int oclitmr(int r, int r1){
	int p = r;// l?y ra Zp
	int q[100], t[100], s[100];
	int r2 = -1, i = 0;
	while(r2!=0){
		q[i+1] = r/r1;
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
	if(t[i]>0) return t[i];
	return t[i] + p;
}
int main(){
	cout << gcd(29,8) << " " << oclitmr(29,8);
}