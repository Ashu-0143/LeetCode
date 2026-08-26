
bool isPalindrome(int x) {
    char str[10000];
    char str2[10000];
    snprintf(str,sizeof(str),"%d",x);
    int start=0;
    int end=strlen(str)-1;
    char a;
    while (start < end){
        a=str[start];
        str[start]=str[end];
        str[end]=a;
        start++;
        end--;
    }
    int num=atoi(str);
    if (num == x)
    return 1;
    return 0;
}
