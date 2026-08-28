bool isHappy(int n) {
    if (n == 1)
        return 1;
    char str[19];
    int strr[9];
    int num, temp, index;
    snprintf(str, sizeof(str), "%d", n);
    while ((temp != 1)) {
        temp = 0;
        for (int i = 0; (str[i] != NULL); i++) {
            num = str[i] - '0';
            temp += num * num;
        }
        index = temp % 9;
        if (!(strr[index]))strr[index] = temp;
        else {
            if (strr[index] == temp)return 0;}
        snprintf(str, sizeof(str), "%d", temp);
    }return 1;
}
