bool isValid(char* s) {
    char stack[500];
    int len=strlen(s);
    int top=-1;
    if (len%2==1)
    return 0;
    if (s[0]!=')'||s[0]!=']'||s[0]!='}'){
            return 0;
        }
        
    
    for (int i = 0 ; i <= len ; i++)
    {
        if ( s[i] == '{' ||s[i] == '[' ||s[i] == '(' ){
            top++;
            stack[top]=s[i] ;
            
        }
        else {
            if  (s[i]=='}'){
                if(stack[top]!='{' ){
                    return 0;
                }else{
                    top--;
                }
            }
            if (s[i]==')') {
                if(stack[top]!='(' ){
        
                    return 0;
                }else{
                    top--;
                }

            }
            if (s[i]==']'){
                if(stack[top]!='[' ){
                    return 0;
                }else{
                    top--;
                }

            }
        }
    }
    if (top>-1){
        
    return 0;
    }
printf("%d",top);

return 1;
    }
