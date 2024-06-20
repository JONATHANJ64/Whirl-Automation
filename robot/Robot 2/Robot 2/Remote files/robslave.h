'=================================================
'# ORiN reserved file
'# WARNING: DO NOT EDIT OR DELETE THIS FILE!
'=================================================
'Reserved indexies
#define RBS_IDX_COMMAND     0   'T<n>
#define RBS_IDX_RESULT      1   'T<n>
#define RBS_IDX_STATE       0   'I<n>
#define RBS_IDX_SLVCRC      1   'I<n>
#define RBS_IDX_EXTCRC      2   'I<n>
#define RBS_IDX_VERSION     0   'S<n>
#define RBS_IDX_ROMVER      0   'F<n>
#define RBS_IDX_TMPFA       1   'F<n>
#define RBS_IDX_CMDEX1      6   'T<n>
#define RBS_IDX_CMDEX2      7   'T<n>
#define RBS_IDX_EXJENBL     8   'T<n>
#define RBS_IDX_EXJVAL      9   'T<n>
#define RBS_IDX_PARAM1      2   'P/J/T/V<n>
#define RBS_IDX_PARAM2      3   'P/J/T/V<n>
#define RBS_IDX_PARAM3      4   'P/J/T/V<n>
#define RBS_IDX_PARAM4      5   'P/J/T/V<n>
#define RBS_IDX_TMP1        3   'I/P/J/T/V/F/S<n>
#define RBS_IDX_TMP2        4   'I/P/J/T/V/F/S<n>

'CRC code
#define RBS_SLVCRC_CODE     &Hb1c04c48
#define RBS_EXTCRC_CODE     &H743614a5

'RobSlave Version
#define RBS_VERSION         "ROBSLAVE 1.300"

'Path definitions
#define RBS_PATH_NONE       0
#define RBS_PATH_AT_P       -1
#define RBS_PATH_AT_E       -2

'Plane definitions
#define RBS_ROT_XY      1
#define RBS_ROT_YZ      2
#define RBS_ROT_ZX      3
#define RBS_ROT_XYH     4
#define RBS_ROT_YZH     5
#define RBS_ROT_ZXH     6

'Pose definitions
#define RBS_POSE_P      0
#define RBS_POSE_T      1
#define RBS_POSE_J      2
#define RBS_POSE_V      3

'State definitions
#define RBS_STA_CLR     0
#define RBS_STA_DOING   1
#define RBS_STA_DONE    2
#define RBS_STA_RETVAL  3
#define RBS_STA_ERR     -1

'ExJnt definitions
#define RBS_EXJNT_NONE  0
#define RBS_EXJNT_EX_   1
#define RBS_EXJNT_EXA   2

'Variable definitions
#define VAR_INT_ID  1
#define VAR_SNG_ID  2
#define VAR_DBL_ID  3
#define VAR_VEC_ID  4
#define VAR_POS_ID  5
#define VAR_JNT_ID  6
#define VAR_TRN_ID  7
#define VAR_STR_ID  8

'User extension commands
#define RBS_CMD_EXTENSION       10000   'for user extension

#ifdef  __VERTICAL_ROBOT__
  #define RBT_JOINT  6
  #define RBT_JPAT  63
#else
  #define RBT_JOINT  4
  #define RBT_JPAT  15
#endif
#define MAXJOINT  8

'#include <pacman.h>
'--------------------------------------------
' Definition File For PAC
' Var. Type
#DEFINE pacINT  1
#DEFINE pacSNG  2
#DEFINE pacDBL  3
#DEFINE pacVEC  4
#DEFINE pacPOS  5
#DEFINE pacJNT  6
#DEFINE pacTRN  7
#DEFINE pacSTR  8
' Configuration Table No.
#DEFINE cnfSYS  1
#DEFINE cnfARM  2
#DEFINE cnfVIS  3
#DEFINE cnfPAC  4
#DEFINE cnfSRV  5
#DEFINE cnfSPD  6
#DEFINE cnfITP  7
#DEFINE cnfDIO  8
#DEFINE cnfCOM  9

'This code will be unnecessary in the future, when a compiler support this function.
'Remember that you must delete this code at that time.
#DEFINE GSRVDAT(NUM,LJNT)  CODE(#LJNT,(NUM),&hEC70,&hef4b,&hef4f,&hef4f,&hef4f,&hf106,&hef98,&hef53)
#DEFINE GSRVSTATE(NUM,LINT) CODE(#LINT,(NUM),&hec71,&hef53)
#DEFINE _CUREXJ(RET,JNT)    CODE(#RET,(JNT),&hed2d,&hef2f,&hef53)
#DEFINE _DESTEXJ(RET,JNT)   CODE(#RET,(JNT),&hed2e,&hef2f,&hef53)
'--------------------------------------------

