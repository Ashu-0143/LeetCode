bool isHappy(int n) {
    if (n==1) return 1;
    char str[10], strr[19];

    int num, temp,index;
    snprintf(str, sizeof(str), "%d", n);
    while ((temp != 1)) {
        temp = 0;
        

        for (int i = 0; str[i] != NULL; i++) {
            num = str[i] - '0';
            temp += num * num;
            printf("char:%c ", str[i]);
        }
        index=temp % 19;
         printf("Printing Array Strr \n");
        for (int i= 0; i<19;i++)
        {
            printf("%d ",strr[i]);
        }
        printf("\n%d ", temp);
        if (!(strr[index])){
            printf("Stored %d at index %d\n",temp,index);
            strr[index] = temp;}
        else {
            if (strr[index] == temp){
                printf("Found %d at index %d!\n\n",temp,index);
                return 0;
            }
                
        }
        snprintf(str, sizeof(str), "%d", temp);
       
    }
     
    return 1;
}
