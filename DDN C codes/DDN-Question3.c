int main()
{
    char *a = "CBACD";
    printf("solution1 %s", a);
    char *c = solution(a);
    //printf("solution %s", solution("CBACD"));

    return 0;
}

char* solution(char *S)
{
    int r =0, w=0;
    int flag;
    
    while(1)
    {
        flag = 0;
        while(S[r])
        {
            printf("solution1 %s", S);
            if((S[r] == 'A' && S[r+1] == 'B') || (S[r] == 'B' && S[r+1] == 'A') || (S[r] == 'C' && S[r+1] == 'D') || (S[r] == 'D' && S[r+1] == 'C'))
            {
                r = r+2;
                flag = 1;
            }
            else
            {
                printf("solution %s", S);
                S[w++] = S[r];
                r++;
            }
        }
        
        printf("solution %s", S);
        r = 0;
        w = 0;
        if(flag == 0)
        {
            break;
        }
    }
    
    return S;
}
