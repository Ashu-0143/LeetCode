bool isHappy(int n) {
    if (n==1) return 1;
    char strr[1000], str[1000];
    int num, temp = 0;
    int j=(n*n);
    snprintf(strr, sizeof(strr), "%d", n);
    snprintf(str, sizeof(str), "%d", n);
    num = atoi(strr);
    while (temp != 1) {
        temp = 0;
        for (int i = 0; strr[i] != NULL; i++) 
        {
            num = strr[i] - '0';
            temp += num * num;
        }
        if (temp == j)
            return 0;
        else if (temp == 1)
            return 1;
        snprintf(strr, sizeof(strr), "%d", temp);
    }
    return 0;
}
