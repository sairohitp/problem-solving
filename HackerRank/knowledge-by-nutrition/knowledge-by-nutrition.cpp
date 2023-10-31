#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isPrime(int n){
    for(int i=2;i<=sqrt(n);i++){
        if(n%i==0)
            return false;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,k;
    cin>>n>>k;
    int count = 0;
    int sum = 0;
    int prime1,prime2;
    int i=2;
    while(true){
        if(isPrime(i)){
            prime1 = i;
            break;
        }
        i++;
        
    }
    i++;
    while(true){
        if(isPrime(i)){
            prime2 = i;
            break;
        }
        i++;
        
    }
    for(int j=2;sum<=n;j++){
        sum = prime1+prime2+1;
        if(sum<=n && isPrime(sum)){
            count++;
        }
        prime1 = prime2;
        i++;
        while(true){
            if(isPrime(i)){
                prime2 = i;
                break;
            }
            i++;

        }
    }
    if(count>=k)
        cout<<"YES";
    else
        cout<<"NO";
    return 0;
}