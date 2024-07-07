#include<bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
	if( a==0 ) return b;
	if( b==0 ) return a;
	
	while(b!=0){
		int tmm = a%b;
		a = b;
		b = tmm;
	}
	return a;
}

int main(){
	cout << gcd(5,15) << endl;
	
}