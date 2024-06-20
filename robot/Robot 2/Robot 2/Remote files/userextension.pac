'!TITLE "UserExtension"
'=================================================
'# ORiN reserved file
'# WARNING: DO NOT EDIT OR DELETE THIS FILE!
'=================================================

#include "RobSlave.h"

'User Extension Commands Def.
'-----------------------------------------------------------
#define RBS_CMD_APPROACH_P          (RBS_CMD_EXTENSION +1)
#define RBS_CMD_APPROACH_L          (RBS_CMD_EXTENSION +2)
#define RBS_CMD_GETSRVDATA          (RBS_CMD_EXTENSION +3)
#define RBS_CMD_GETJNTDATA          (RBS_CMD_EXTENSION +4)
#define RBS_CMD_DEPART_P            (RBS_CMD_EXTENSION +5)
#define RBS_CMD_DEPART_L            (RBS_CMD_EXTENSION +6)
#define RBS_CMD_CLRSPLINEPOINT      (RBS_CMD_EXTENSION +7)
#define RBS_CMD_SETSPLINEPOINT      (RBS_CMD_EXTENSION +8)
#define RBS_CMD_GETSPLINEPOINT      (RBS_CMD_EXTENSION +9)
#define RBS_CMD_WAITSPLINEPOINT     (RBS_CMD_EXTENSION +10)
#define RBS_CMD_GETSRVSTATE         (RBS_CMD_EXTENSION +11)
#define RBS_CMD_WAITMOTIONEND       (RBS_CMD_EXTENSION +12)
#define RBS_CMD_MOTOR               (RBS_CMD_EXTENSION +13)
#define RBS_CMD_DRAW_P              (RBS_CMD_EXTENSION +14)
#define RBS_CMD_DRAW_L              (RBS_CMD_EXTENSION +15)
#define RBS_CMD_INTERRUPT           (RBS_CMD_EXTENSION +16)
#define RBS_CMD_POSCLR              (RBS_CMD_EXTENSION +17)
#define RBS_CMD_ARRIVE              (RBS_CMD_EXTENSION +18)
#define RBS_CMD_ROTATEH             (RBS_CMD_EXTENSION +19)
#define RBS_CMD_DRIVEEX             (RBS_CMD_EXTENSION +20)
#define RBS_CMD_DRIVEAEX            (RBS_CMD_EXTENSION +21)
'ST_MIN
#define RBS_CMD_ST_ASPACLD          (RBS_CMD_EXTENSION +22)
#define RBS_CMD_ST_ASPCHG           (RBS_CMD_EXTENSION +23)
#define RBS_CMD_ST_SETGRAV          (RBS_CMD_EXTENSION +24)
#define RBS_CMD_ST_RSTGRAV          (RBS_CMD_EXTENSION +25)
#define RBS_CMD_ST_SETGRVOFST       (RBS_CMD_EXTENSION +26)
#define RBS_CMD_ST_RSTGRVOFST       (RBS_CMD_EXTENSION +27)
#define RBS_CMD_ST_SETCURLMT        (RBS_CMD_EXTENSION +28)
#define RBS_CMD_ST_RSTCURLMT        (RBS_CMD_EXTENSION +29)
#define RBS_CMD_ST_SETERALW         (RBS_CMD_EXTENSION +30)
#define RBS_CMD_ST_RSTERALW         (RBS_CMD_EXTENSION +31)
#define RBS_CMD_ST_SETCMPCTRL       (RBS_CMD_EXTENSION +32)
#define RBS_CMD_ST_SETCMPFCTRL      (RBS_CMD_EXTENSION +33)
#define RBS_CMD_ST_RSTCMPCTRL       (RBS_CMD_EXTENSION +34)
#define RBS_CMD_ST_SETFRCCORD       (RBS_CMD_EXTENSION +35)
#define RBS_CMD_ST_SETFRCLMT        (RBS_CMD_EXTENSION +36)
#define RBS_CMD_ST_RSTFRCLMT        (RBS_CMD_EXTENSION +37)
#define RBS_CMD_ST_SETCMPRATE       (RBS_CMD_EXTENSION +38)
#define RBS_CMD_ST_RSTCMPRATE       (RBS_CMD_EXTENSION +39)
#define RBS_CMD_ST_SETFRCASST       (RBS_CMD_EXTENSION +40)
#define RBS_CMD_ST_RSTFRCASST       (RBS_CMD_EXTENSION +41)
#define RBS_CMD_ST_SETCMPJLMT       (RBS_CMD_EXTENSION +42)
#define RBS_CMD_ST_RSTCMPJLMT       (RBS_CMD_EXTENSION +43)
#define RBS_CMD_ST_SETCMPVMD        (RBS_CMD_EXTENSION +44)
#define RBS_CMD_ST_RSTCMPVMD        (RBS_CMD_EXTENSION +45)
#define RBS_CMD_ST_SETCMPERALW      (RBS_CMD_EXTENSION +46)
#define RBS_CMD_ST_RSTCMPERALW      (RBS_CMD_EXTENSION +47)
#define RBS_CMD_ST_SETDMPRATE       (RBS_CMD_EXTENSION +48)
#define RBS_CMD_ST_RSTDMPRATE       (RBS_CMD_EXTENSION +49)
#define RBS_CMD_ST_ONSRVLOCK        (RBS_CMD_EXTENSION +50)
#define RBS_CMD_ST_OFFSRVLOCK       (RBS_CMD_EXTENSION +51)
#define RBS_CMD_ST_SETZBLNCE        (RBS_CMD_EXTENSION +52)
#define RBS_CMD_ST_RSTZBLNCE        (RBS_CMD_EXTENSION +53)
'ST_MAX
#define RBS_CMD_DELAY               (RBS_CMD_EXTENSION +54)
#define RBS_CMD_SYSSTATE            (RBS_CMD_EXTENSION +55)
#define RBS_CMD_J2P                 (RBS_CMD_EXTENSION +56)
#define RBS_CMD_J2T                 (RBS_CMD_EXTENSION +57)
#define RBS_CMD_P2J                 (RBS_CMD_EXTENSION +58)
#define RBS_CMD_P2T                 (RBS_CMD_EXTENSION +59)
#define RBS_CMD_T2J                 (RBS_CMD_EXTENSION +60)
#define RBS_CMD_T2P                 (RBS_CMD_EXTENSION +61)
#define RBS_CMD_TINV                (RBS_CMD_EXTENSION +62)
#define RBS_CMD_NORMTRN             (RBS_CMD_EXTENSION +63)
#define RBS_CMD_TRACKDATAINIT       (RBS_CMD_EXTENSION +64)
#define RBS_CMD_TRACKDATASET        (RBS_CMD_EXTENSION +65)
#define RBS_CMD_TRACKDATAGET        (RBS_CMD_EXTENSION +66)
#define RBS_CMD_TRACKDATAINFO       (RBS_CMD_EXTENSION +67)
#define RBS_CMD_TRACKDATANUM        (RBS_CMD_EXTENSION +68)
#define RBS_CMD_CURTRACKPOS         (RBS_CMD_EXTENSION +69)
#define RBS_CMD_CURTRACKSPD         (RBS_CMD_EXTENSION +70)
#define RBS_CMD_WAITTRACKMOVE       (RBS_CMD_EXTENSION +71)
#define RBS_CMD_CALCWORKPOS         (RBS_CMD_EXTENSION +72)
#define RBS_CMD_CURTRACKPOSEX       (RBS_CMD_EXTENSION +73)
#define RBS_CMD_WAITTRACKMVEX       (RBS_CMD_EXTENSION +74)
#define RBS_CMD_SETTRACKMOVE        (RBS_CMD_EXTENSION +75)
#define RBS_CMD_RESETTRACKMOVE      (RBS_CMD_EXTENSION +76)
#define RBS_CMD_SETTRACKSTAREA      (RBS_CMD_EXTENSION +77)
#define RBS_CMD_DEVH                (RBS_CMD_EXTENSION +78)
#define RBS_CMD_DEV                 (RBS_CMD_EXTENSION +79)
#define RBS_CMD_TMUL                (RBS_CMD_EXTENSION +80)
#define RBS_CMD_MPS                 (RBS_CMD_EXTENSION +81)
#define RBS_CMD_POSTUREAREA         (RBS_CMD_EXTENSION +82) 
#define RBS_MAX_POSTUREAREA         10
#define RBS_CMD_SETPOSTUREAREA      (RBS_CMD_EXTENSION +83) 
#define RBS_CMD_RESETPOSTUREAREA    (RBS_CMD_EXTENSION +84) 
#define RBS_CMD_SETSINGULARAVOID    (RBS_CMD_EXTENSION +85)
#define RBS_CMD_SETHIGHPATHACC      (RBS_CMD_EXTENSION +86)
#define RBS_CMD_RESETHIGHPATHACC    (RBS_CMD_EXTENSION +87)
#define RBS_CMD_FIGAPRP             (RBS_CMD_EXTENSION +88)
#define RBS_CMD_FIGAPRL             (RBS_CMD_EXTENSION +89)
#define RBS_CMD_CHGFIXEDTOOL        (RBS_CMD_EXTENSION +90)
#define RBS_CMD_GETCOLLISIONFORCE   (RBS_CMD_EXTENSION +91)
#define RBS_CMD_CLRCOLLISIONFORCE   (RBS_CMD_EXTENSION +92)
#define RBS_CMD_RSTCOLLISIONJNT     (RBS_CMD_EXTENSION +93)
#define RBS_CMD_SETCOLLISIONJNT     (RBS_CMD_EXTENSION +94)
#define RBS_CMD_SETCOLLISIONLEVEL   (RBS_CMD_EXTENSION +95)
#define RBS_CMD_SETEXTFORCEDETECT   (RBS_CMD_EXTENSION +96)
#define RBS_CMD_RPM                 (RBS_CMD_EXTENSION +97)
' :

' User Extension Commands Impl.
'--------------------------------------------------------------------------------------
PROGRAM UserExtension(pv as VECTOR, ov as VECTOR, av as VECTOR, istate as INTEGER, icompletion as INTEGER)

    DEFINT cmd, index, path
    DEFINT no, nx, mode, vartype, varindex
    DEFSNG ret, length, fx, fy, fz
    DEFJNT jv
    DEFSNG m(9), a(9), n(9), k(9), q, w
    DEFVEC vv
    DEFPOS ps, pa, pb

    'for PostureArea
    DEFPOS arP(RBS_MAX_POSTUREAREA)  'position
    DEFVEC arD(RBS_MAX_POSTUREAREA)  'dx,dy,dz
    DEFINT arIO(RBS_MAX_POSTUREAREA) 'io
    DEFINT arPS(RBS_MAX_POSTUREAREA) 'pos
    DEFINT arER(RBS_MAX_POSTUREAREA) 'err
    DEFINT arEN(RBS_MAX_POSTUREAREA) 'enable
    DEFVEC arV(RBS_MAX_POSTUREAREA)  'tpos
    DEFSNG arVM(RBS_MAX_POSTUREAREA) 'tpos margin
    DEFSNG arEV(RBS_MAX_POSTUREAREA,9)  'exa
    DEFSNG arEM(RBS_MAX_POSTUREAREA,9) 'exa margin
    
    cmd = POSX(pv)
    istate = RBS_STA_DONE
    select case cmd
    '-----------------------------------------------------------
    case RBS_CMD_APPROACH_L   'APPROACH L,... ,NEXT
    'APPROACH L, <Base position>,[@<Path start desplacement> ]<Approach length>[,<Motion option>][,NEXT]
        index = 1
        gosub *GetCmdParam ' <Base position> variable type = RBS_POSE_P or RBS_POSE_T or RBS_POSE_J 
        vartype = ret
        index = 2
        gosub *GetCmdParam ' <Base position> variable index
        varindex = ret
        index = 3
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret
        index = 4
        gosub *GetCmdParam ' <Approach length>
        length = ret
        index = 5
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

#ifdef  __VERTICAL_ROBOT__
        vv = (0,0,-length)
#else
        vv = (0,0,length)
#endif
        select case vartype
        case RBS_POSE_P
            CODE((P[varindex]),(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed13,&Hef4f) 'Approach L, P[
        case RBS_POSE_T
            CODE((T[varindex]),&Hec60,(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed13,&Hef4f) 'Approach L, T[
        case RBS_POSE_J
            CODE((J[varindex]),&Hec01,(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed13,&Hef4f) 'Approach L, J[
        end select
    '-----------------------------------------------------------
    case RBS_CMD_APPROACH_P   'APPROACH P,... , NEXT
    'APPROACH P, <Base position>,[@<Path start desplacement> ]<Approach length>[,NEXT]
        index = 1
        gosub *GetCmdParam ' <Base position> variable type = RBS_POSE_P or RBS_POSE_T or RBS_POSE_J 
        vartype = ret
        index = 2
        gosub *GetCmdParam ' <Base position> variable index
        varindex = ret
        index = 3
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret
        index = 4
        gosub *GetCmdParam ' <Approach length>
        length = ret
        index = 5
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

#ifdef  __VERTICAL_ROBOT__
        vv = (0,0,-length)
#else
        vv = (0,0,length)
#endif
        select case vartype
        case RBS_POSE_P
            CODE((P[varindex]),(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed11,&Hef4f) 'Approach P, P[
        case RBS_POSE_T
            CODE((T[varindex]),&Hec60,(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed11,&Hef4f) 'Approach P, T[
        case RBS_POSE_J
            CODE((J[varindex]),&Hec01,(path),&Hed1a,&Hef4f,(vv),&Hef43,&Hed11,&Hef4f) 'Approach P, J[
        end select
    case RBS_CMD_GETJNTDATA       'GetJntData(<Index>, <JontNo>)
    '-----------------------------------------------------------
        LETX T[RBS_IDX_RESULT] = GetJntData ( POSY(pv), POSZ(pv) )
        istate = RBS_STA_RETVAL ' Return value
    case RBS_CMD_GETSRVDATA       'GetSrvData(<Index>)
        '-----------------------------------------------------------
        jv = GetSrvData ( POSY(pv) )
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), JOINT(5,jv), JOINT(6,jv), 0,0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), 0,0,0,0,0, -1 )
#endif
        istate = RBS_STA_RETVAL ' Return value
    '-----------------------------------------------------------
    case RBS_CMD_GETSRVSTATE
        LETX T[RBS_IDX_RESULT] = GetSrvState ( POSY(pv) )
        istate = RBS_STA_RETVAL ' Return value
    '-----------------------------------------------------------
    case RBS_CMD_DEPART_L 'DEPART L,... , NEXT
    'DEPART L, [@<Path start desplacement>]<Depart length>[,NEXT]
        index = 1
        gosub *GetCmdParam ' [@<Path start desplacement>]
        path = ret
        index = 2
        gosub *GetCmdParam ' <Depart length>
        length = ret
        index = 3
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

#ifdef  __VERTICAL_ROBOT__
        vv = (0,0,-length)
#else
        vv = (0,0,length)
#endif
        CODE(&Hecd6,(path),&Hed1a,&Hef4f,&Hec4c,(vv),&Hef43,&Hed13,&Hef4f) 'Depart L
    '-----------------------------------------------------------
    case RBS_CMD_DEPART_P 'DEPART P,... , NEXT
    'DEPART P, [@<Path start desplacement> ]<Depart length> [,NEXT]
        index = 1
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret
        index = 2
        gosub *GetCmdParam ' <Depart length>
        length = ret
        index = 3
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

#ifdef  __VERTICAL_ROBOT__
        vv = (0,0,-length)
#else
        vv = (0,0,length)
#endif
        CODE(&Hecd6,(path),&Hed1a,&Hef4f,&Hec4c,(vv),&Hef43,&Hed11,&Hef4f) 'Depart P
    '-----------------------------------------------------------
    case RBS_CMD_CLRSPLINEPOINT
        if F[RBS_IDX_ROMVER] < 2.3 then
            istate = RBS_STA_ERR
        else
            index = 1
            gosub *GetCmdParam
            no = ret
            'ClrSplinePoint no
            CODE((no),(17),&Heef4)
        end if
    '-----------------------------------------------------------
    case RBS_CMD_SETSPLINEPOINT
        if F[RBS_IDX_ROMVER] < 2.3 then
            istate = RBS_STA_ERR
        else
            index = 1
            gosub *GetCmdParam
            no = ret
            index = 2
            gosub *GetCmdParam
            vartype = ret
            index = 3
            gosub *GetCmdParam
            varindex = ret

            select case vartype
            case RBS_POSE_P
                'SetSplinePoint no, P[varindex]
                 CODE((no),(P[varindex]),(16),&Heef4)
            case RBS_POSE_J
                'SetSplinePoint no, J[varindex]
                 CODE((no),(J[varindex]),(16),&Heef4)
            end select
        end if
    '-----------------------------------------------------------
    case RBS_CMD_GETSPLINEPOINT
        if F[RBS_IDX_ROMVER] < 2.3 then
            istate = RBS_STA_ERR
        else
            index = 1
            gosub *GetCmdParam
            no = ret
            index = 2
            gosub *GetCmdParam
            varindex = ret
            index = 3
            gosub *GetCmdParam
            index = ret
            
            'P[RBS_IDX_TMP1] = GetSplinePoint(no, varindex)
            CODE(&H1013,(RBS_IDX_TMP1),(no),(varindex),(18),&Heef4,&Hef57)
            ps = P[RBS_IDX_TMP1]
#ifdef  __VERTICAL_ROBOT__
            T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
            T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
            istate = RBS_STA_RETVAL
        end if
    '-----------------------------------------------------------
    case RBS_CMD_WAITSPLINEPOINT ' = xdWAITSPLINE
        if F[RBS_IDX_ROMVER] < 2.3 then
            istate = RBS_STA_ERR
        else
            index = 1
            gosub *GetCmdParam
            no = ret
            index = 2
            gosub *GetCmdParam
            mode = ret
            
            LETENV cnfSPD, 298, no
            if mode = 0 then
              ret = GetSrvState(71)
            else
              ret = GetSrvState(72)
            endif
        end if
    '-----------------------------------------------------------
    case RBS_CMD_MOTOR
    'MOTOR <mode=0:OFF,1:ON>
        index = 1
        gosub *GetCmdParam ' mode
        mode = ret
        if mode = 0 then
            Motor OFF
        else
            Motor ON
        endif
    '-----------------------------------------------------------
    case RBS_CMD_WAITMOTIONEND
        icompletion = 0 'wait for motion end
    '-----------------------------------------------------------
    case RBS_CMD_DRAW_P 'DRAW P,... , NEXT
    'DRAW P, [@<Path start desplacement> ] (V<n>) [,NEXT]
        icompletion = POSX(ov)
        CODE(&Hecd6,&Hec4c,(POSY(pv)),&Hed1a,&Hef4f,(V[POSZ(pv)]),&Hef42,&Hed11,&Hef4f) ' DRAW P
    '-----------------------------------------------------------
    case RBS_CMD_DRAW_L 'DRAW L,... , NEXT
    'DRAW L, [@<Path start desplacement> ] (V<n>) [,NEXT]
        icompletion = POSX(ov)
        CODE(&Hecd6,&Hec4c,(POSY(pv)),&Hed1a,&Hef4f,(V[POSZ(pv)]),&Hef42,&Hed13,&Hef4f) ' DRAW L
    '-----------------------------------------------------------
    case RBS_CMD_INTERRUPT
    'INTERRUPT <mode=0:OFF,1:ON>
        index = 1
        gosub *GetCmdParam ' mode
        mode = ret
        if mode = 0 then
            Interrupt OFF
        else
            Interrupt ON
        endif
    '-----------------------------------------------------------
    case RBS_CMD_POSCLR
    'POSCLR <no>
        index = 1
        gosub *GetCmdParam ' no
        no = ret
        Posclr no
    '-----------------------------------------------------------
    case RBS_CMD_ARRIVE
    'ARRIVE <radio>
        index = 1
        gosub *GetCmdParam ' radio
        Arrive ret
    '-----------------------------------------------------------
    case RBS_CMD_ROTATEH 'ROTATEH ... , NEXT
    'ROTATEH [@<Path start desplacement> ] <angle> [,NEXT]
        index = 1
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret
        index = 2
        gosub *GetCmdParam ' <angle>
        fx = ret
        index = 3
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

        CODE(&Hecd6,(path),&Hed1a,&Hef4f,&Hec4c,&Hf100,&Hf100,&Hf100,&Hf100,&Hf100,(fx),&Hf106,&Hed25,&Hed13,&Hef4f) ' Rotateh
    '-----------------------------------------------------------
    case RBS_CMD_DRIVEEX 'DRIVE ...(,),(,)... , NEXT
    'DRIVE [@<Path start desplacement> ] (<no>,<fx>),(<no>,<fx>),(<no>,<fx>),(<no>,<fx>),.. [,NEXT]
        index = 9
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

        index = 1
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret

        for nx = 1 to 8
            m(nx) = 0
            a(nx) = 0
        next
        for nx = 1 to 8
            index = index + 1
            if index = 9 then index = 10 'skip FIG
            gosub *GetCmdParam ' <no>
            if ret = 0 then exit for
            no = ret
            index = index + 1
            if index = 9 then index = 10
            gosub *GetCmdParam ' <fx>
            fx = ret
            if no >= 1 and no <= 8 then
                m(no) = 1
                a(no) = fx
            endif
        next
        CODE(&Hecd6,(path),&Hed1a,&Hef4f,(m(1)),(m(2)),(m(3)),(m(4)),(m(5)),(m(6)),(m(7)),(m(8)),&Hf108,&Hf0f5,&Hef4a,&Hf0,(q),&Hef6a,&Hf0,(q),&Hef52)
        CODE((a(1)),(a(2)),(a(3)),(a(4)),(a(5)),(a(6)),(a(7)),(a(8)),&Hf108,&Hf0f5,&Hef4a,&hf0,(w),&Hef6a,&hf0,(w),&Hef52,(q),(w),&Hed19,&Hef4f)
    '-----------------------------------------------------------
    case RBS_CMD_DRIVEAEX 'DRIVEA ...(,),(,)... , NEXT
    'DRIVEA [@<Path start desplacement> ] (<no>,<fx>),(<no>,<fx>),(<no>,<fx>),(<no>,<fx>),.. [,NEXT]
        index = 9
        gosub *GetCmdParam ' <NEXT option>
        icompletion = ret

        index = 1
        gosub *GetCmdParam ' [@<Path start desplacement> ]
        path = ret

        for nx = 1 to 8
            m(nx)=0
            if  GETENV(cnfSRV,nx) <> 3 then
                a(nx)=DESTEXJ(nx)
            else
                a(nx)=0
            end if
        next
        for nx = 1 to 8
            index = index + 1
            if index = 9 then index = 10 'skip FIG
            gosub *GetCmdParam ' <no>
            if ret = 0 then exit for
            no = ret
            index = index + 1
            if index = 9 then index = 10
            gosub *GetCmdParam ' <fx>
            fx = ret
            if no >= 1 and no <= 8 then
                m(no) = 1
                a(no) = fx
            endif
        next
        CODE((path),&Hed1a,&Hef4f,(m(1)),(m(2)),(m(3)),(m(4)),(m(5)),(m(6)),(m(7)),(m(8)),&Hf108,&Hf0f5,&Hef4a,&Hf0,(q),&Hef6a,&Hf0,(q),&Hef52)
        CODE((a(1)),(a(2)),(a(3)),(a(4)),(a(5)),(a(6)),(a(7)),(a(8)),&Hf108,&Hf0f5,&Hef4a,&hf0,(w),&Hef6a,&hf0,(w),&Hef52,(q),(w),&Hed18,&Hef4f) 'DriveA
   '-----------------------------------------------------------
    case RBS_CMD_ST_ASPACLD
        ST_aspACLD POSY(pv), POSZ(pv), POSX(ov), POSY(ov)
    case RBS_CMD_ST_ASPCHG
        ST_aspChange POSY(pv)
#ifdef  __VERTICAL_ROBOT__
    case RBS_CMD_ST_SETGRAV
        ST_SetGravity
    case RBS_CMD_ST_RSTGRAV 
        ST_ResetGravity
    case RBS_CMD_ST_SETGRVOFST
        ST_SetGrvOffset
    case RBS_CMD_ST_RSTGRVOFST
        ST_ResetGrvOffset
#endif
    case RBS_CMD_ST_SETCURLMT
        ST_SetCurLmt POSY(pv), POSZ(pv)
    case RBS_CMD_ST_RSTCURLMT
        ST_ResetCurLmt POSY(pv)
    case RBS_CMD_ST_SETERALW
        ST_SetEralw POSY(pv), POSZ(pv)
    case RBS_CMD_ST_RSTERALW
        ST_ResetEralw POSY(pv)
#ifdef  __VERTICAL_ROBOT__
    case RBS_CMD_ST_SETCMPCTRL
        ST_SetCompControl
    case RBS_CMD_ST_SETCMPFCTRL
        ST_SetCompFControl
    case RBS_CMD_ST_RSTCMPCTRL
        ST_ResetCompControl
    case RBS_CMD_ST_SETFRCCORD
        ST_SetFrcCoord POSY(pv)
    case RBS_CMD_ST_SETFRCLMT
        ST_SetFrcLimit POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTFRCLMT
        ST_ResetFrcLimit
    case RBS_CMD_ST_SETCMPRATE
        ST_SetCompRate POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTCMPRATE
        ST_ResetCompRate
    case RBS_CMD_ST_SETFRCASST
        ST_SetFrcAssist POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTFRCASST
        ST_ResetFrcAssist
    case RBS_CMD_ST_SETCMPJLMT
        ST_SetCompJLimit POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTCMPJLMT
        ST_ResetCompJLimit
    case RBS_CMD_ST_SETCMPVMD
        ST_SetCompVMode
    case RBS_CMD_ST_RSTCMPVMD
        ST_ResetCompVMode
    case RBS_CMD_ST_SETCMPERALW
        ST_SetCompEralw POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTCMPERALW
        ST_ResetCompEralw
    case RBS_CMD_ST_SETDMPRATE
        ST_SetDampRate POSY(pv), POSZ(pv), POSX(ov), POSY(ov), POSZ(ov), POSX(av)
    case RBS_CMD_ST_RSTDMPRATE
        ST_ResetDampRate
#else
    case RBS_CMD_ST_ONSRVLOCK
        ST_OnSrvLock POSY(pv)
    case RBS_CMD_ST_OFFSRVLOCK
        ST_OffSrvLock POSY(pv)
    case RBS_CMD_ST_SETZBLNCE
        ST_SetZBalance
    case RBS_CMD_ST_RSTZBLNCE
        ST_ResetZBalance
#endif
   '-----------------------------------------------------------
    case RBS_CMD_DELAY
        Delay POSY(pv)
    case RBS_CMD_SYSSTATE
        nx = SYSSTATE
        a(0) = nx MOD &H10000 'LOW(16bit)
        a(1) = nx / &H10000   'HIGH(16bit)
        T[RBS_IDX_RESULT] = ( a(0), a(1), 0, 0, 0, 0, 0, 0, 0, -1 )
        istate = RBS_STA_RETVAL ' Return value
    '-----------------------------------------------------------  
    case RBS_CMD_J2P
        ps = J2P(J[POSY(pv)])
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_J2T
        T[RBS_IDX_RESULT] = J2T(J[POSY(pv)])
        istate = RBS_STA_RETVAL
    case RBS_CMD_P2J
        jv = P2J(P[POSY(pv)])
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), JOINT(5,jv), JOINT(6,jv), 0,0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), 0,0,0,0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_P2T
        T[RBS_IDX_RESULT] = P2T(P[POSY(pv)])
        istate = RBS_STA_RETVAL
    case RBS_CMD_T2J
        jv = T2J(T[POSY(pv)])
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), JOINT(5,jv), JOINT(6,jv), 0,0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), 0,0,0,0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_T2P
        ps = T2P(T[POSY(pv)])
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_TINV
        T[RBS_IDX_RESULT] = TINV(T[POSY(pv)])
        istate = RBS_STA_RETVAL
    case RBS_CMD_NORMTRN
        T[RBS_IDX_RESULT] = NORMTRN(T[POSY(pv)])
        istate = RBS_STA_RETVAL
    case RBS_CMD_TMUL
        T[RBS_IDX_RESULT] = T[POSY(pv)] *  T[POSZ(pv)]
        istate = RBS_STA_RETVAL
    case RBS_CMD_DEVH ' = Pa/* + (x,y,z,rx,ry,rz)H
        index = POSY(pv)
        if index < 0 then 'return = * + (,,,)
            pa = * 'CURPOS
        elseif index = 0 then 'return = DESTPOS + (,,,)
            pa = DESTPOS
        else
            pa = P[index]
        endif
        pb = P[POSZ(pv)] 
#ifdef  __VERTICAL_ROBOT__
        ps = pa + (POSX(pb), POSY(pb), POSZ(pb), POSRX(pb), POSRY(pb), POSRZ(pb))H
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        ps = pa + (POSX(pb), POSY(pb), POSZ(pb), POST(pb))H
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_DEV ' = Pa/* + (x,y,z,rx,ry,rz)
        index = POSY(pv)
        if index < 0 then 'return = * + (,,,)
            pa = * 'CURPOS
        elseif index = 0 then 'return = DESTPOS + (,,,)
            pa = DESTPOS
        else
            pa = P[index]
        endif
        pb = P[POSZ(pv)] 
#ifdef  __VERTICAL_ROBOT__
        ps = pa + (POSX(pb), POSY(pb), POSZ(pb), POSRX(pb), POSRY(pb), POSRZ(pb))
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        ps = pa + (POSX(pb), POSY(pb), POSZ(pb), POST(pb))
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    '-----------------------------------------------------------  
    case RBS_CMD_TRACKDATAINIT 
        TRACKDATAINITIALIZE POSY(pv)
    case RBS_CMD_TRACKDATASET    
        TRACKDATASET POSY(pv), POSZ(pv), P[POSX(ov)]
    case RBS_CMD_TRACKDATAGET    
        TRACKDATAGET POSY(pv), POSZ(pv), nx, ps
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( nx, POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0, -1 )
#else
        T[RBS_IDX_RESULT] = ( nx, POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_TRACKDATAINFO   
        TRACKDATAINFO POSY(pv), POSZ(pv), nx, mode, ps
        a(0) = nx MOD &H10000 'LOW(16bit)
        a(1) = nx / &H10000   'HIGH(16bit)
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( a(0), a(1), mode, POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps) )
#else
        T[RBS_IDX_RESULT] = ( a(0), a(1), mode, POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps) )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_TRACKDATANUM    
        nx = TRACKDATANUM( POSY(pv) )
        T[RBS_IDX_RESULT] = ( nx, 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL
    case RBS_CMD_CURTRACKPOS     
        ps = CURTRACKPOS( POSY(pv), P[POSZ(pv)], POSX(ov) ) ' Arg1, P[Arg2], Arg3
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_CURTRACKSPD     
        ret = CURTRACKSPD( POSY(pv) )
        T[RBS_IDX_RESULT] = ( ret, 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL
    case RBS_CMD_WAITTRACKMOVE   
        WAITTRACKMOVE POSY(pv), P[POSZ(pv)], POSX(ov) ' Arg1, P[Arg2], Arg3
    case RBS_CMD_CALCWORKPOS     
        nx = POSY(ov)
        nx = (nx * &H10000) + POSX(ov)
        ps = CALCWORKPOS( POSY(pv), P[POSZ(pv)], nx )
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0,0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_CURTRACKPOSEX   
        ps = CURTRACKPOSEX( POSY(pv), P[POSZ(pv)], POSX(ov), nx ) ' Arg1, P[Arg2], Arg3
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( nx, POSX(ps), POSY(ps), POSZ(ps), POSRX(ps), POSRY(ps), POSRZ(ps), FIG(ps), 0, -1 )
#else
        T[RBS_IDX_RESULT] = ( nx, POSX(ps), POSY(ps), POSZ(ps), 0, 0, POST(ps), FIG(ps), 0, -1 )
#endif
        istate = RBS_STA_RETVAL
    case RBS_CMD_WAITTRACKMVEX   
        ret = WAITTRACKMOVEEX( POSY(pv), P[POSZ(pv)], POSX(ov) ) ' Arg1, P[Arg2], Arg3
        T[RBS_IDX_RESULT] = ( ret, 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL
    case RBS_CMD_SETTRACKMOVE    
        no =  POSY(pv)
        select case no
        case 1
            nx = GetSrvState(131)
        case 2
            nx = GetSrvState(132)
        case else
            istate = RBS_STA_ERR
        end select
    case RBS_CMD_RESETTRACKMOVE  
        nx = GetSrvState(130)
    case RBS_CMD_SETTRACKSTAREA
        no = POSY(pv)
        a(0) = POSZ(pv) 'NArea
        a(1) = POSX(ov) 'PArea
        select case no
        case 1
            LETENV cnfSPD,254,(a(1)*100)
            LETENV cnfSPD,255,(a(0)*100)
        case 2
            LETENV cnfSPD,256,(a(1)*100)
            LETENV cnfSPD,257,(a(0)*100)
        case else
            istate = RBS_STA_ERR
        end select
   '-----------------------------------------------------------
    case RBS_CMD_MPS
        T[RBS_IDX_RESULT] = ( MPS(POSY(pv)), 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL
    '-----------------------------------------------------------
    case RBS_CMD_POSTUREAREA
        no = POSY(pv)
        arP(no) = P[POSZ(pv)]
        arD(no) = V[POSX(ov)]
        arIO(no) = POSY(ov)
        arPS(no) = POSZ(ov)
        arER(no) = POSX(av)
        arEN(no) = POSY(av)
        '
        ' T[RBS_IDX_CMDEX1] = (<PoseType>,<PoseIndex>,<PoseMargin>)
        vv = PVEC(T[RBS_IDX_CMDEX1])
        fx = POSX(vv)
        fy = POSY(vv)
        fz = POSZ(vv)
        if fx = RBS_POSE_V then
            vv = V[fy]
        else
#ifdef  __VERTICAL_ROBOT__
            vv = RVEC(P[fy])
#else
            vv = (0,0,POST(P[fy]))
#endif
        endif
        arV(no) = vv
        arVM(no) = fz

        ' T[RBS_IDX_EXJENBL] = (<J1 Enable>,<J2 Enable>,...,<J8 Enable>)
        ' T[RBS_IDX_EXJVAL] = (<J1 Value>,<J2 Value>,...,<J8 Value>)
        ' T[RBS_IDX_CMDEX2] = (<J1 Margin>,<J2 Margin>,...,<J8 Margin>)
        ' Enabled
        vv = PVEC(T[RBS_IDX_EXJENBL])
        m(1) = POSX(vv)
        m(2) = POSY(vv)
        m(3) = POSZ(vv)
        vv = OVEC(T[RBS_IDX_EXJENBL])
        m(4) = POSX(vv)
        m(5) = POSY(vv)
        m(6) = POSZ(vv)
        vv = AVEC(T[RBS_IDX_EXJENBL])
        m(7) = POSX(vv)
        m(8) = POSY(vv)
        ' Value
        vv = PVEC(T[RBS_IDX_EXJVAL])
        arEV(no,1) = POSX(vv)
        arEV(no,2) = POSY(vv)
        arEV(no,3) = POSZ(vv)
        vv = OVEC(T[RBS_IDX_EXJVAL])
        arEV(no,4) = POSX(vv)
        arEV(no,5) = POSY(vv)
        arEV(no,6) = POSZ(vv)
        vv = AVEC(T[RBS_IDX_EXJVAL])
        arEV(no,7) = POSX(vv)
        arEV(no,8) = POSY(vv)
        ' ExJ Margin
        vv = PVEC(T[RBS_IDX_CMDEX2])
        arEM(no,1) = POSX(vv)
        arEM(no,2) = POSY(vv)
        arEM(no,3) = POSZ(vv)
        vv = OVEC(T[RBS_IDX_CMDEX2])
        arEM(no,4) = POSX(vv)
        arEM(no,5) = POSY(vv)
        arEM(no,6) = POSZ(vv)
        vv = AVEC(T[RBS_IDX_CMDEX2])
        arEM(no,7) = POSX(vv)
        arEM(no,8) = POSY(vv)
        for nx=1 to 8
            if m(nx)=0 then arEM(no,nx) = -1
        next

    case RBS_CMD_SETPOSTUREAREA
        no = POSY(pv)
        for nx=1 to 8
            a(nx) = arEV(no,nx)
            m(nx) = arEM(no,nx)
            if m(nx) = -1 then
                n(nx) = 0
            else
                n(nx) = 1
            end if
        next

        CODE((arP(no)),(arD(no)),(arIO(no)),(arPS(no)),(arER(no)),(&h29),&hEEF4)
        CODE((arV(no)),(arVM(no)),(1),(a(1)),(m(1)),(n(1)),(2),(a(2)),(m(2)),(n(2)),(3),(a(3)),(m(3)),(n(3)),(4),(a(4)),(m(4)),(n(4)),(5),(a(5)),(m(5)),(n(5)),(6),(a(6)),(m(6)),(n(6)),(7),(a(7)),(m(7)),(n(7)),(8),(a(8)),(m(8)),(n(8)),(&h2C),&hEEF4)
        CODE((&h2A), &hEEF4)

    case RBS_CMD_RESETPOSTUREAREA
        CODE((&h2B), &hEEF4)

    case RBS_CMD_SETSINGULARAVOID
        LETENV cnfSPD,308, POSY(pv)

    case RBS_CMD_SETHIGHPATHACC
#ifdef  __VERTICAL_ROBOT__
        LETENV 6,307,63
#else
        LETENV 6,307,15
#endif

    case RBS_CMD_RESETHIGHPATHACC
        LETENV 6,307,0

    case RBS_CMD_FIGAPRP   'FIGAPRP P[Arg1], Arg2
        ret = FIGAPRP( P[POSY(pv)], POSZ(pv) )
        T[RBS_IDX_RESULT] = ( ret, 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL

    case RBS_CMD_FIGAPRL   'FIGAPRL P[Arg1], Arg2
        ret = FIGAPRL( P[POSY(pv)], POSZ(pv) )
        T[RBS_IDX_RESULT] = ( ret, 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL

    case RBS_CMD_CHGFIXEDTOOL 'CHANGEGFIXEDTOOL no ,nx
        no = POSY(pv)
        nx = POSZ(pv)
        ChangeTool 0
        ChangeWork 0
        Tool nx, T2P(TINV(CURTRN) * P2T(WORKPOS(no)))
        ChangeTool nx

    case RBS_CMD_GETCOLLISIONFORCE 'GETCOLLISIONFORCE
        jv = GetSrvData(36)
#ifdef  __VERTICAL_ROBOT__
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), JOINT(5,jv), JOINT(6,jv), 0,0,0, -1 )
#else
        T[RBS_IDX_RESULT] = ( JOINT(1,jv), JOINT(2,jv), JOINT(3,jv), JOINT(4,jv), 0,0,0,0,0, -1 )
#endif
        istate = RBS_STA_RETVAL

    case RBS_CMD_CLRCOLLISIONFORCE 'CLEARCOLLISIONFORCE
        nx = GetSrvState(30)

    case RBS_CMD_RSTCOLLISIONJNT 'RESETCOLLISIONJNT no
        no = POSY(pv)
        if no > RBT_JOINT then
            istate = RBS_STA_ERR
        else
            nx = GETENV(cnfSPD,206)
            index = 2^(no-1)
            if (nx AND index) <> 0 then
                nx = nx AND (NOT(index))
                LETENV cnfSPD,206,nx
            endif
        endif

    case RBS_CMD_SETCOLLISIONJNT 'SETCOLLISIONJNT no
        no = POSY(pv)
        if no > RBT_JOINT then
            istate = RBS_STA_ERR
        else
            nx = GETENV(cnfSPD,204)
            if nx = 0 then
                LETENV cnfSPD,204,1
            endif
            nx = GETENV(cnfSPD,206)
            index = 2^(no-1)
            if (nx AND index) = 0 then
                nx = nx OR index
                LETENV cnfSPD,206,nx
            endif
        endif

    case RBS_CMD_SETCOLLISIONLEVEL 'SETCOLLISIONLEVEL no, nx
        no = POSY(pv)
        nx = POSZ(pv)
        if no > RBT_JOINT then
            istate = RBS_STA_ERR
        else
            mode = GetSrvState(29)
            if mode = 2 then 'AUTO
                index = 206+no
            else
                index = 214+no
            endif
            LETENV cnfSPD,index,nx
        endif

    case RBS_CMD_SETEXTFORCEDETECT 'SETEXTFORCEDETECT val(=POSY(pv))
        LETENV cnfSPD,231,POSY(pv)

    case RBS_CMD_RPM 'ret = RPM(no,nx)
        no = POSY(pv)
        nx = POSZ(pv)
        'F[RBS_IDX_TMP1] = RPM(no, nx)
        CODE(&H1021,(RBS_IDX_TMP1),(no),(nx),(28),&Heef4,&Hef2f,&Hef57)
        T[RBS_IDX_RESULT] = ( F[RBS_IDX_TMP1], 0,0,0,0,0,0,0,0, -1 )
        istate = RBS_STA_RETVAL

    case else
        istate = RBS_STA_ERR
    end select
END

' ret = GetCmdParam(index)
*GetCmdParam:
    select case index
    case 0  'T[RBS_IDX_COMMAND].X = COMMAND
        ret = POSX(pv)
    case 1  'T[RBS_IDX_COMMAND].Y
        ret = POSY(pv)
    case 2  'T[RBS_IDX_COMMAND].Z
        ret = POSZ(pv)
    case 3  'T[RBS_IDX_COMMAND].OX
        ret = POSX(ov)
    case 4  'T[RBS_IDX_COMMAND].OY
        ret = POSY(ov)
    case 5  'T[RBS_IDX_COMMAND].OZ
        ret = POSZ(ov)
    case 6  'T[RBS_IDX_COMMAND].AX
        ret = POSX(av)
    case 7  'T[RBS_IDX_COMMAND].AY
        ret = POSY(av)
    case 8  'T[RBS_IDX_COMMAND].AZ
        ret = POSZ(av)
    case 9  'T[RBS_IDX_COMMAND].FIG
        ret = FIG(T[RBS_IDX_COMMAND])
    case 10  'T[RBS_IDX_CMDEX1].X
        ret = POSX(PVEC(T[RBS_IDX_CMDEX1]))
    case 11  'T[RBS_IDX_CMDEX1].Y
        ret = POSY(PVEC(T[RBS_IDX_CMDEX1]))
    case 12  'T[RBS_IDX_CMDEX1].Z
        ret = POSZ(PVEC(T[RBS_IDX_CMDEX1]))
    case 13  'T[RBS_IDX_CMDEX1].OX
        ret = POSX(OVEC(T[RBS_IDX_CMDEX1]))
    case 14  'T[RBS_IDX_CMDEX1].OY
        ret = POSY(OVEC(T[RBS_IDX_CMDEX1]))
    case 15  'T[RBS_IDX_CMDEX1].OZ
        ret = POSZ(OVEC(T[RBS_IDX_CMDEX1]))
    case 16  'T[RBS_IDX_CMDEX1].AX
        ret = POSX(AVEC(T[RBS_IDX_CMDEX1]))
    case 17  'T[RBS_IDX_CMDEX1].AY
        ret = POSY(AVEC(T[RBS_IDX_CMDEX1]))
    case 18  'T[RBS_IDX_CMDEX1].AZ
        ret = POSZ(AVEC(T[RBS_IDX_CMDEX1]))
    case else
        ret = 0
    end select
RETURN

