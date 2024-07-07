#include<bits/stdc++.h>
using namespace std;
 
//Key values of a and b
const int a = 17;
const int b = 20;
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
int oclitmr2(int r, int r1 ){
	int p = r;
	int q[100];
	int t[100];
	int s[100];
	int r2 = -1;
	int i = 0;
	while( r2!= 0 ){
		r2 = r%r1;
		q[i+1] = r/r1;
		switch(i){
			case 0 :
				s[i] = 1;
				t[i] = 0;
				break;
			case 1:
				s[i] = 0; 
				t[i] = 1;
				break;
			default:
				s[i] = s[i-2]  - q[i-1] * s[i-1];
				t[i] = t[i-2] - q[i-1] * t[i-1]; 			
				break;
				
		}
		r = r1;
		r1=r2;
		i++;
	}
		s[i] = s[i-2] - q[i-1] * s[i-1];
		t[i] = t[i-2] - q[i-1] * t[i-1];
		if(t[i] > 0) return t[i];
		else return t[i]+ p;
}
string encryptMessage(string msg)
{
    ///Cipher Text initially empty
    string cipher = ""; 
    for (int i = 0; i < msg.length(); i++)
    {
        // Avoid space to be encrypted 
        if(msg[i]!=' ') 
            /* applying encryption formula ( a x + b ) mod m
            {here x is msg[i] and m is 26} and added 'A' to 
            bring it in range of ascii alphabet[ 65-90 | A-Z ] */
            cipher = cipher + 
                        (char) ((((a * (msg[i]-'A') ) + b) % 26) + 'A');
        else
            //else simply append space character
            cipher += msg[i];     
    }
    return cipher;
}
 
string decryptCipher(string cipher)
{
    string msg = "";
    int a_inv = oclitmr(26,a);
    int flag = 0;
     
    //Find a^-1 (the multiplicative inverse of a 
        //in the group of integers modulo m.) 
  
    for (int i = 0; i < cipher.length(); i++)
    {
        if(cipher[i]!=' ')
            /*Applying decryption formula a^-1 ( x - b ) mod m 
            {here x is cipher[i] and m is 26} and added 'A' 
            to bring it in range of ASCII alphabet[ 65-90 | A-Z ] */
            msg = msg + 
                       (char) (((a_inv * ((cipher[i]+'A' - b)) % 26)) + 'A');
        else
            //else simply append space character
            msg += cipher[i]; 
    }
 
    return msg;
}
 
//Driver Program
int main(void)
{
	
	
    string msg = "AFFINE CIPHER";
     
    //Calling encryption function
    string cipherText = encryptMessage(msg);
    cout << "Encrypted Message is : " << cipherText<<endl;
     
    //Calling Decryption function
    cout << "Decrypted Message is: " << decryptCipher(cipherText);
 
    return 0;
}
