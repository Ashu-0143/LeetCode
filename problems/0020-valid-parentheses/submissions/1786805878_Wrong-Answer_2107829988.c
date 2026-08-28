bool isValid(char* s) {
    char stack[100];
    int len=strlen(s);
    if (len%2==1){
        return 0;
    }
    int top=-1;
    for (int i = 0 ; i <= len ; i++)
    {
        if ( s[i] == '{' ||s[i] == '[' ||s[i] == '(' ){
            top++;
            stack[top]=s[i] ;
        }
        else {
            if (top==-1){
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
        else{
            return 0;
        }
        }
}
if (top!=-1){
return 0;
}

return 1;
}
