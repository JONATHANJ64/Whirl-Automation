' Definition File For PAC
' Var. Type
#DEFINE	pacINT 	1
#DEFINE	pacSNG 	2
#DEFINE	pacDBL 	3
#DEFINE	pacVEC 	4
#DEFINE	pacPOS 	5
#DEFINE	pacJNT 	6
#DEFINE	pacTRN 	7
#DEFINE	pacSTR 	8
' Configuration Table No.
#DEFINE cnfSYS	1
#DEFINE cnfARM	2
#DEFINE cnfVIS	3
#DEFINE cnfPAC	4
#DEFINE cnfSRV	5
#DEFINE cnfSPD	6
#DEFINE cnfITP	7
#DEFINE cnfDIO	8
#DEFINE cnfCOM	9

'This code will be unnecessary in the future, when a compiler support this function.
'Remember that you must delete this code at that time.
#DEFINE GSRVDAT(NUM,LJNT)  CODE(#LJNT,(NUM),&hEC70,&hef4b,&hef4f,&hef4f,&hef4f,&hf106,&hef98,&hef53)
#DEFINE GSRVSTATE(NUM,LINT) CODE(#LINT,(NUM),&hec71,&hef53)
#DEFINE _CUREXJ(RET,JNT)	CODE(#RET,(JNT),&hed2d,&hef2f,&hef53)
#DEFINE _DESTEXJ(RET,JNT)	CODE(#RET,(JNT),&hed2e,&hef2f,&hef53)

