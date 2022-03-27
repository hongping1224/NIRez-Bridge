
#ifndef _NIREZ20_SDK_H_
#define _NIREZ20_SDK_H_
extern "C" __declspec(dllexport) int  NIRez20_Initial(void);                            //NIRez使用前的初始化動作
extern "C" __declspec(dllexport) int  NIRez20_Link_Status(void);                        //NIRez連線狀態
extern "C" __declspec(dllexport) int  NIRez20_Config(int,int,int,double,int,int,int,int,int);   //配置NIRez掃描參數
extern "C" __declspec(dllexport) int  NIRez20_Scan(int*,int*,double*,int*);             //NIRez開始掃描
extern "C" __declspec(dllexport) void NIRez20_Destroy(void);                            //不使用(退出)NIRez時呼叫使用
extern "C" __declspec(dllexport) void NIRez20_Connect(void);                            //手動連線
extern "C" __declspec(dllexport) void NIRez20_Disconnect(void);                        //手動離線
//-----------
#endif
