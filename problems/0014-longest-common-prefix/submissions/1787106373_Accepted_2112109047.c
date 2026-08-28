char* longestCommonPrefix(char** strs, int strsSize) {
    int tmp=0,small;
    char *str= strs[0];
    for (int i = 0; i < strsSize; i++) {
        tmp = strlen(strs[i]);
        if (tmp < small)
            small = tmp;
    }
    for (int i = 1; i < strsSize; i++) {
        for (int j = 0; j < strlen(strs[0]); j++) {
            if (!(strs[i][j] == str[j])) 
                str[j]='\0';
        }

    }
    return str;
}
