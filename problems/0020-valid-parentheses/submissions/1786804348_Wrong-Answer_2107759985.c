bool isValid(char* s) {
    char stack[30];
    int top=-1;
    for (int i = 0 ; i != '\0' ; i++)
    {
        if ( s[i] == '{' ||s[i] == '[' ||s[i] == '(' ){
            top++;
            stack[top]=s[i] ;
        }
        else {
            if  (s[i]=='}'){
                if(stack[top]!='{' ){
                    return "false";
                }else{
                    top--;
                }

            }
            if (s[i]==')') {
                if(stack[top]!='(' ){
                    return "false";
                }else{
                    top--;
                }

            }
            if (s[i]==']'){
                if(stack[top]!='[' ){
                    return "false";
                }else{
                    top--;
                }

            }
        }
}
if (top!=-1){
return false;
}

return "tue";
}
