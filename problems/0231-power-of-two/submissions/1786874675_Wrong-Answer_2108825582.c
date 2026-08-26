bool isPowerOfTwo(int n) {
    if (n==1)
    return 1;
    else if (n%2 != 0 || ((n/2)%2)!=0)
    return 0;
    else {
        int half = n/2;
        for (int i =2 ; i < half ;i=i+2)
        {
            if (pow(2,i)==n)
                return 1;
        }
    }
    return 0;
}
