bool isPowerOfTwo(int n) {
    if (n == 1)
        return 1;
    else if (n == 3 || n%2 == 1)
    return 0;
  
    for (int i = 2; i< (n/2) ; i=i*2){
        if (n/2==3)
            return 0;
        //if (n%i!=0 ||(n/2)%2 !=0)
        //return 0;
        
        
    }
    return 1;
}
