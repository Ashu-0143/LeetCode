int valueFinder(char roman)
    {
        switch (roman){
            case 'I':return 1;
            case 'V':return 5;
            case 'X':return 10;
            case 'L':return 50;
            case 'C':return 100;
            case 'D':return 500;
            case 'M':return 1000;
        }
    return 0;
    }
int romanToInt(char* s) {
    int len = strlen(s);
    int valCurrent,res=0,valPrev;
    for (int i = len; i!=-1 ;i--)
    {
        if (i==len){
            valPrev= 0;
            valCurrent = valueFinder(s[i]);
        }
        else{
        valCurrent = valueFinder(s[i]);
        valPrev = valueFinder(s[i+1]);
        }
        if (valPrev>valCurrent)
        {
            res-=valCurrent;
        }
        else{
            res+=valCurrent;
        }
    }
    return res;
}
