#include<iostream>
using namespace std;
 
int main()
{
     int T; cin>>T;
     while(T--)
     {
          int N; cin>>N;
          int curr; cin>>curr; 
          int prev,i; 
          for(i=1;i<=N;i++) { 
          char c; cin>>c; 
          if(c=='P') { 
               prev = curr;  
               scanf("%d",&curr);
          } 
          else { 
               int temp=curr; 
               curr = prev; 
               prev = temp;  
          } 
     } 
     cout<<"Player "<<curr<<endl;  
   } 
}