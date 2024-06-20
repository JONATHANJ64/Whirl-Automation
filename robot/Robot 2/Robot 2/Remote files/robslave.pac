'!TITLE "RobSlave"
'=================================================
'# ORiN reserved file
'# WARNING: DO NOT EDIT OR DELETE THIS FILE!
'=================================================

#include "RobSlave.h"

'Command definitions
#define RBS_CMD_MOVEP           1000
#define RBS_CMD_MOVEL           1001
#define RBS_CMD_MOVEC           1002
#define RBS_CMD_MOVES           1003
#define RBS_CMD_MOVP_EX_        1050
#define RBS_CMD_MOVL_EX_        1051
#define RBS_CMD_MOVC_EX_        1052
#define RBS_CMD_MOVS_EX_        1053
#define RBS_CMD_MOVP_EXA        1060
#define RBS_CMD_MOVL_EXA        1061
#define RBS_CMD_MOVC_EXA        1062
#define RBS_CMD_MOVS_EXA        1063
#define RBS_CMD_MOTIONSKIP      1010
#define RBS_CMD_MOTIONCOMP      1011
#define RBS_CMD_DRIVE           1020
#define RBS_CMD_ROTATE          1030
#define RBS_CMD_ROTATE_XYZH     1040
#define RBS_CMD_TAKEARM         1100
#define RBS_CMD_GIVEARM         1101
#define RBS_CMD_DEFAREA         1140
#define RBS_CMD_CHANGETOOL      1150
#define RBS_CMD_DEFTOOL         1151
#define RBS_CMD_CHANGEWORK      1160
#define RBS_CMD_DEFWORK         1161
#define RBS_CMD_ACCEL           1170
#define RBS_CMD_DECEL           1171
#define RBS_CMD_JACCEL          1172
#define RBS_CMD_JDECEL          1173
#define RBS_CMD_SPEED           1180
#define RBS_CMD_JSPEED          1181

PROGRAM RobSlave
    DEFVEC pv,ov,av
    DEFINT istate, icompletion, n, iarmsem
    DEFINT jpat,add_jpat,rsel,cmd,jnt,skipj,targetj,ireturn
    DEFSNG q, w, sp, csp
    DEFSNG g(9), k(9)

    'Init
    F[RBS_IDX_ROMVER] = VAL(VER$(0))
    I[RBS_IDX_SLVCRC] = RBS_SLVCRC_CODE
    I[RBS_IDX_EXTCRC] = RBS_EXTCRC_CODE
    S[RBS_IDX_VERSION] = RBS_VERSION
    T[RBS_IDX_COMMAND] = (0, 0, 0, 0, 0, 0, 0, 0, 0, -1)
    I[RBS_IDX_STATE] = RBS_STA_ERR ' Return ERROR if the RobMaster is waitting for.
    if F[RBS_IDX_ROMVER] >= 2.3 then
        LI% = GetSrvState(73) ' = xdSPLClrTakeArm(0) 
        'the viapoint of the free curve during TakeArm is not cleared.
    end if
    TAKEARM KEEP=1
    iarmsem = 1
    'Main
    do
        pv = PVEC(T[RBS_IDX_COMMAND])
        if POSX(pv) > 0 then
            I[RBS_IDX_STATE] = RBS_STA_DOING
            icompletion = -1
            istate = I[RBS_IDX_STATE]
            ov = OVEC(T[RBS_IDX_COMMAND])
            av = AVEC(T[RBS_IDX_COMMAND])
            '---------------------------------------------------
            if POSX(pv) >= RBS_CMD_EXTENSION then
                call UserExtension(pv,ov,av,istate,icompletion)
                goto *DoLoop
            end if
            '---------------------------------------------------
            select case POSX(pv)
            '===========================================================
            case RBS_CMD_MOVEP      'MOVE P,...
            '-----------------------------------------------------------
                gosub *SetJSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE P,[@?] P<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),&Hed11,&Hef4f)
                case RBS_POSE_T                 'MOVE P,[@?] T<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),&Hed11,&Hef4f)
                case RBS_POSE_J                 'MOVE P,[@?] J<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),&Hed11,&Hef4f)
                end select
                gosub *RestoreJSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVEL      'MOVE L,...
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE L,[@?] P<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),&Hed13,&Hef4f)
                case RBS_POSE_T                 'MOVE L,[@?] T<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),&Hed13,&Hef4f)
                case RBS_POSE_J                 'MOVE L,[@?] J<n1> ,NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),&Hed13,&Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVEC      'MOVE C,...
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE C, P<n1> ,[@?] P<n2> ,NEXT
                    CODE((P[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(P[POSX(av)]),&Hed17,&Hef4f)
                case RBS_POSE_T                 'MOVE C,[@?] T<n1> ,[@?] T<n2> ,NEXT
                    CODE((T[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(T[POSX(av)]),&Hed17,&Hef4f)
                case RBS_POSE_J                 'MOVE C,[@?] J<n1> ,[@?] J<n2> ,NEXT
                    CODE((J[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(J[POSX(av)]),&Hed17,&Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVES      'MOVE S,...
            '-----------------------------------------------------------
                if F[RBS_IDX_ROMVER] < 2.3 then
                    istate = RBS_STA_ERR
                else
                    gosub *SetSpeed
                    icompletion = POSY(av)
                    n = POSX(ov)
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(n),(13),&Heef4,&Hef4f)
                    gosub *RestoreSpeed
                    istate = RBS_STA_DONE
                end if
            '[EX()]=====================================================
            ' T[RBS_IDX_EXJENBL] = (<J1 Enable>,<J2 Enable>,...,<J8 Enable>)
            ' T[RBS_IDX_EXJVAL] = (<J1 Value>,<J2 Value>,...,<J8 Value>)
            case RBS_CMD_MOVP_EX_      'MOVE P,...EX()  
            '-----------------------------------------------------------
                gosub *SetJSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE P,[@?] P<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed30, &Hef4f)
                case RBS_POSE_T                 'MOVE P,[@?] T<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed30, &Hef4f)
                case RBS_POSE_J                 'MOVE P,[@?] J<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed30, &Hef4f)
                end select
                gosub *RestoreJSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVL_EX_      'MOVE L,...EX()
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE L,[@?] P<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed32, &Hef4f)
                case RBS_POSE_T                 'MOVE L,[@?] T<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed32, &Hef4f)
                case RBS_POSE_J                 'MOVE L,[@?] J<n1> EX(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed32, &Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVC_EX_      'MOVE C,...EX()
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE C, P<n1> ,[@?] P<n2> EX(),NEXT
                    CODE((P[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(P[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed34, &Hef4f)
                case RBS_POSE_T                 'MOVE C,[@?] T<n1> ,[@?] T<n2> EX(),NEXT
                    CODE((T[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(T[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed34, &Hef4f)
                case RBS_POSE_J                 'MOVE C,[@?] J<n1> ,[@?] J<n2> EX(),NEXT
                    CODE((J[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(J[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed34, &Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVS_EX_      'MOVE S,...EX()
            '-----------------------------------------------------------
                if F[RBS_IDX_ROMVER] < 2.3 then
                    istate = RBS_STA_ERR
                else
                    gosub *SetSpeed
                    icompletion = POSY(av)
                    n = POSX(ov)
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(n),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, (14), &Heef4, &Hef4f)
                    gosub *RestoreSpeed
                    istate = RBS_STA_DONE
                end if
            '[EXA()]====================================================
            ' T[RBS_IDX_EXJENBL] = (<J1 Enable>,<J2 Enable>,...,<J8 Enable>)
            ' T[RBS_IDX_EXJVAL] = (<J1 Value>,<J2 Value>,...,<J8 Value>)
            case RBS_CMD_MOVP_EXA      'MOVE P,...EXA()
            '-----------------------------------------------------------
                gosub *SetJSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE P,[@?] P<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed2f, &Hef4f)
                case RBS_POSE_T                 'MOVE P,[@?] T<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed2f, &Hef4f)
                case RBS_POSE_J                 'MOVE P,[@?] J<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed2f, &Hef4f)
                end select
                gosub *RestoreJSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVL_EXA      'MOVE L,...EXA()
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE L,[@?] P<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(P[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed31, &Hef4f)
                case RBS_POSE_T                 'MOVE L,[@?] T<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(T[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed31, &Hef4f)
                case RBS_POSE_J                 'MOVE L,[@?] J<n1> EXA(),NEXT
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(J[POSX(ov)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed31, &Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVC_EXA      'MOVE C,...EXA()
            '-----------------------------------------------------------
                gosub *SetSpeed
                icompletion = POSY(av)
                select case POSY(pv)
                case RBS_POSE_P                 'MOVE C, P<n1> ,[@?] P<n2> EXA(),NEXT
                    CODE((P[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(P[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed33, &Hef4f)
                case RBS_POSE_T                 'MOVE C,[@?] T<n1> ,[@?] T<n2> EXA(),NEXT
                    CODE((T[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(T[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed33, &Hef4f)
                case RBS_POSE_J                 'MOVE C,[@?] J<n1> ,[@?] J<n2> EXA(),NEXT
                    CODE((J[POSX(ov)]),(POSZ(ov)),&Hed1a,&Hef4f,(J[POSX(av)]),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, &Hed33, &Hef4f)
                end select
                gosub *RestoreSpeed
                istate = RBS_STA_DONE
            case RBS_CMD_MOVS_EXA      'MOVE S,...EXA()
            '-----------------------------------------------------------
                if F[RBS_IDX_ROMVER] < 2.3 then
                    istate = RBS_STA_ERR
                else
                    gosub *SetSpeed
                    icompletion = POSY(av)
                    n = POSX(ov)
                    CODE((POSZ(pv)),&Hed1a,&Hef4f,(n),(T[RBS_IDX_EXJENBL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a,(T[RBS_IDX_EXJVAL]),&Hef93, &Hef4f, &Hef4f,&Hf108, &Hf0f5, &Hef4a, (15), &Heef4, &Hef4f)
                    gosub *RestoreSpeed
                    istate = RBS_STA_DONE
                end if
            '============================================================
            case RBS_CMD_MOTIONSKIP     'MOTIONSKIP
            '-----------------------------------------------------------
                gosub *MotionSkip
                istate = RBS_STA_DONE
            case RBS_CMD_MOTIONCOMP     'MOTIONCOMP
            '-----------------------------------------------------------
                gosub *MotionComp
                T[RBS_IDX_RESULT] = (0, 0, 0, 0, 0, 0, 0, 0, 0, -1)
                LETX T[RBS_IDX_RESULT] = ireturn
                istate = RBS_STA_RETVAL ' Return value
            case RBS_CMD_TAKEARM        'TAKEARM
            '-----------------------------------------------------------
                if iarmsem <> 0 then
                    GiveArm
                    iarmsem = 0
                end if
                TakeArm POSY(pv) Keep = POSZ(pv)
                iarmsem = 1
                istate = RBS_STA_DONE
            case RBS_CMD_GIVEARM        'GIVEARM
            '-----------------------------------------------------------
                 if iarmsem <> 0 then
                    GiveArm
                    iarmsem = 0
                end if
                istate = RBS_STA_DONE
            case RBS_CMD_CHANGETOOL     'CHANGETOOL
            '-----------------------------------------------------------
                ChangeTool POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_CHANGEWORK     'CHANGEWORK
            '-----------------------------------------------------------
                ChangeWork POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_ACCEL          'ACCEL
            '-----------------------------------------------------------
                if POSZ(pv) > 0 then
                    Accel POSY(pv), POSZ(pv) 
                else
                    Accel POSY(pv)
                end if
                istate = RBS_STA_DONE
            case RBS_CMD_DECEL      'DECEL
            '-----------------------------------------------------------
                Decel POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_SPEED      'SPEED
            '-----------------------------------------------------------
                Speed POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_JACCEL     'JACCEL
            '-----------------------------------------------------------
                if POSZ(pv) > 0 then
                    JAccel POSY(pv), POSZ(pv) 
                else
                    JAccel POSY(pv)
                end if
                istate = RBS_STA_DONE
            case RBS_CMD_JDECEL     'JDECEL
            '-----------------------------------------------------------
                JDecel POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_JSPEED     'JSPEED
            '-----------------------------------------------------------
                JSpeed POSY(pv)
                istate = RBS_STA_DONE
            case RBS_CMD_ROTATE     'ROTATE
            '-----------------------------------------------------------
#ifdef  __VERTICAL_ROBOT__
                icompletion = POSY(av)
                CODE((V[POSY(pv)]),(V[POSZ(pv)]),(V[POSX(ov)]),&Hef9a,(POSX(av)),&Hed1a,&Hef4f,(POSY(ov)),(V[POSZ(ov)]),(POSZ(av)),&Hec63,&Hef4f)
                istate = RBS_STA_DONE
#else
                istate = RBS_STA_ERR
#endif
            case RBS_CMD_ROTATE_XYZH     'ROTATE XY:1|YZ:2|ZX:3|XYH:4|YZH:5|ZXH:6
            '-----------------------------------------------------------
                icompletion = POSY(av)
                istate = RBS_STA_DONE
                select case POSY(pv)
                case RBS_ROT_XY
                case RBS_ROT_XYH
#ifdef  __VERTICAL_ROBOT__
                case RBS_ROT_YZ
                case RBS_ROT_YZH
                case RBS_ROT_ZX
                case RBS_ROT_ZXH
#endif
                case else
                   istate = RBS_STA_ERR
                end select
                if istate = RBS_STA_DONE then
                   CODE((POSY(pv)),(POSX(av)),&Hed1a,&Hef4f,(POSY(ov)),(V[POSZ(ov)]),(POSZ(av)),&Hed16,&Hef4f)
                end if
            case RBS_CMD_DRIVE      'DRIVE
            '-----------------------------------------------------------
                icompletion = POSY(ov)
                for n = 1 to 8 
                   g(n) = 0
                   k(n) = 0
                next
                g(POSY(pv)) = 1
                k(POSY(pv)) = POSZ(pv)
                CODE(&Hecd6,(POSX(ov)),&Hed1a,&Hef4f,(g(1)),(g(2)),(g(3)),(g(4)),(g(5)),(g(6)),(g(7)),(g(8)),&Hf108,&Hf0f5,&Hef4a,&Hf0,(q),&Hef6a,&Hf0,(q),&Hef52)
                CODE((k(1)),(k(2)),(k(3)),(k(4)),(k(5)),(k(6)),(k(7)),(k(8)),&Hf108,&Hf0f5,&Hef4a,&hf0,(w),&Hef6a,&hf0,(w),&Hef52,(q),(w),&Hed19,&Hef4f)
                istate = RBS_STA_DONE
           case RBS_CMD_DEFTOOL     'TOOL
            '-----------------------------------------------------------
                Tool POSY(pv), P[POSZ(pv)]
                istate = RBS_STA_DONE
           case RBS_CMD_DEFWORK     'WORK
            '-----------------------------------------------------------
                if F[RBS_IDX_ROMVER] < 2.902 then
                   Work POSY(pv), P[POSZ(pv)]
                else
                   'Work POSY(pv), P[POSZ(pv)], POSX(ov)
                   CODE((POSY(pv)),(P[POSZ(pv)]),(POSX(ov)),&Hec04)
                end if
                istate = RBS_STA_DONE
           case RBS_CMD_DEFAREA     'AREA
            '-----------------------------------------------------------
                '    no,       P[n]         V[m]         IO<i>     P<o>      <err>
                Area POSY(pv), P[POSZ(pv)], V[POSX(ov)], POSY(ov), POSZ(ov), POSX(av)
                if POSY(av) = 0 then 'Disable
                    ResetArea POSY(pv)
                else
                    SetArea POSY(pv)
                end if
                istate = RBS_STA_DONE
            '-----------------------------------------------------------
             case else
                istate = RBS_STA_ERR
            end select
*DoLoop:
            if icompletion = 0 then
                CODE(&Hf2,&hffff,&Hed1c,&Hef4f) 'WaitForCompletion
            end if
            LETX pv = 0
            LETP T[RBS_IDX_COMMAND] = pv
            I[RBS_IDX_STATE]  = istate
        end if
    loop
END

*MotionSkip:
  jpat=GetSrvState(5)
  rsel=jpat AND RBT_JPAT
  if rsel = 0 then
    add_jpat = RBT_JPAT+1
    for jnt=RBT_JOINT+1 to MAXJOINT
      rsel=jpat AND add_jpat
      if rsel = add_jpat then
        skipj = jnt+10
        cmd=GetSrvState(skipj)
        exit for
      end if
      add_jpat = add_jpat*2
    next
  else
    cmd=GetSrvState(10)
  end if
return

*MotionComp:
  ireturn=1
  jpat=GetSrvState(5)
  rsel=jpat AND RBT_JPAT
  if rsel = 0 then
    add_jpat = RBT_JPAT+1
    for jnt=RBT_JOINT+1 to MAXJOINT
      rsel=jpat AND add_jpat
      if rsel = add_jpat then
        targetj = jnt+20
        ireturn=GetSrvState(targetj)
        exit for
      end if
      add_jpat = add_jpat*2
    next
  else
    ireturn=GetSrvState(20)
  end if
return

*SetSpeed:
  sp = POSZ(av)
  if sp <> 0 then
    csp = CURSPD 
    SPEED ABS(sp)
  end if
return
*RestoreSpeed:
  if sp > 0 then
    SPEED csp
  end if
return

*SetJSpeed:
  sp = POSZ(av)
  if sp <> 0 then
    csp = CURJSPD 
    JSPEED ABS(sp)
  end if
return
*RestoreJSpeed:
  if sp > 0 then
    JSPEED csp
  end if
return

