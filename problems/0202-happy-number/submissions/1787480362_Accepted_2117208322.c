bool isHappy(int n) {
    if (n==1) return 1;
    char str[19];
    int strr[9];

    int num, temp,index;
    snprintf(str, sizeof(str), "%d", n);
    while ((temp != 1)) {
        temp = 0;
        

        for (int i = 0; (str[i] != NULL ); i++) {
         printf("\nPrinting i:%d",i);
            num = str[i] - '0';
            temp += num * num;
            printf("char:%c ", str[i]);
        }
        index=temp%9;
         printf("\nPrinting Array Strr : ");
        for (int i= 0; i<9;i++)
        {
            printf("%d ",strr[i]);
        }
        printf("\t\tcalling....%d \n",strr[index]);
        if (!(strr[index])){
            strr[index] = temp;
            printf("Stored %d/%d at index %d\n\n",temp,strr[index],index);
            }
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
