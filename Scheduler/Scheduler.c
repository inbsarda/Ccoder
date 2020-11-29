// Online C compiler to run C program online
#include <stdio.h>

#define TRUE 1
#define FALSE 0

#define TASK_PRIORITY_10MS  10
#define TASK_PRIORITY_20MS  20
#define TASK_PRIORITY_99MS  99

typedef enum
{
    TASK_ID_1,
    TASK_ID_2,
    TASK_ID_3,
    TASK_ID_END
}TASK_ID;

typedef enum
{
    TASK_STATE_INACTIVE,
    TASK_STATE_READY
}TASK_STATE;

typedef struct 
{
    void (*pTaskFunction)(void);
    TASK_ID TaskID;
    int TaskPeriod;
    int TaskOffset;
    int TaskEnable;
    int TaskElapsedTime;
    TASK_STATE TaskState;
}stSCHEDULERTASKTABLE;

void SLR_TASK_10ms()
{
    printf("\n Hello 10ms");
}

void SLR_TASK_20ms()
{
    printf("\n Hello 20ms");
}

void SLR_TASK_99ms()
{
    printf("\n Hello 99ms");
}

stSCHEDULERTASKTABLE stSCHEDULERTASK[TASK_ID_END] =
{
    { SLR_TASK_10ms, TASK_ID_1, TASK_PRIORITY_10MS, 0, TRUE, 0, 0 },
    { SLR_TASK_20ms, TASK_ID_2, TASK_PRIORITY_20MS, 0, TRUE, 0, 0 },
    { SLR_TASK_99ms, TASK_ID_3, TASK_PRIORITY_99MS, 0, FALSE, 0, 0 },
};


void taskScheduler()
{
    int tIndex;
    for(tIndex = 0; tIndex < TASK_ID_END; tIndex++)
    {
        if(stSCHEDULERTASK[tIndex].TaskEnable == TRUE)
        {
            stSCHEDULERTASK[tIndex].TaskElapsedTime++;
        }
        
        if((stSCHEDULERTASK[tIndex].TaskElapsedTime + stSCHEDULERTASK[tIndex].TaskOffset) == stSCHEDULERTASK[tIndex].TaskPeriod)
        {
            stSCHEDULERTASK[tIndex].TaskState = TASK_STATE_READY;
            stSCHEDULERTASK[tIndex].TaskElapsedTime = 0;
        }
    }
    
    for(tIndex = 0; tIndex < TASK_ID_END; tIndex++)
    {
        if(stSCHEDULERTASK[tIndex].TaskState == TASK_STATE_READY)
        {
            stSCHEDULERTASK[tIndex].pTaskFunction();
            stSCHEDULERTASK[tIndex].TaskState = TASK_STATE_INACTIVE;
        }
    }
}

int main() {
    
    while(1)
    {
        for(int i = 0; i < 10000; i++);
        taskScheduler();
    }
    return 0;
}