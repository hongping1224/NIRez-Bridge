
#ifndef _NIREZ20_SDK_H_
#define _NIREZ20_SDK_H_
extern "C" __declspec(dllexport) int  NIRez20_Initial(void);                            //NIRez�ϥΫe����l�ưʧ@
extern "C" __declspec(dllexport) int  NIRez20_Link_Status(void);                        //NIRez�s�u���A
extern "C" __declspec(dllexport) int  NIRez20_Config(int,int,int,double,int,int,int,int,int);   //�t�mNIRez���y�Ѽ�
extern "C" __declspec(dllexport) int  NIRez20_Scan(int*,int*,double*,int*);             //NIRez�}�l���y
extern "C" __declspec(dllexport) void NIRez20_Destroy(void);                            //���ϥ�(�h�X)NIRez�ɩI�s�ϥ�
extern "C" __declspec(dllexport) void NIRez20_Connect(void);                            //��ʳs�u
extern "C" __declspec(dllexport) void NIRez20_Disconnect(void);                        //������u
//-----------
#endif
