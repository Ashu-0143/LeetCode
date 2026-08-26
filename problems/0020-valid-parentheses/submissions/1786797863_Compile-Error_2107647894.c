bool isValid(char* s) {
    char stack[30];
    int top=-1;
    for (int i = 0 ; i != '\0' ; i++)
    {
        if ( s[i] == '{' ||s[i] == '[' ||s[i] == '(' ){
            top++;
            stack[top]=s[i] ;
        }
        else{
            if !(stack[top]) == '{' && s[i]=='}'){
                return 0;
            if !(stack[top]) == '(' && s[i]==')'){
                return 0;
            if !(stack[top]) == '[' && s[i]==']'){
                return 0;
            }
        }
    }
    return true;
}
