'----------------------------------------
'!Title      Obtains the state of the motion execution
'!Author     DENSO WAVE INCORPORATED
'!Date       
'!Link       
'!Include
'!CalledPrg
'
'!ARG 1     "The state of motion execution",1,""
'----------------------------------------

#INCLUDE  <pacman.h>
#ifdef  __VERTICAL_ROBOT__
  #define RBT_JOINT  6
  #define RBT_JPAT  63
#else
  #define RBT_JOINT  4
  #define RBT_JPAT  15
#endif
#define MAXJOINT  8
#define REL_8SMRT 2.800

PROGRAM MotionComp(CmpFlag as integer)
defint jpat,add_jpat,rsel,cmd,jnt,targetj,rbt_joint2,rbt_jpat2,b_pat
defsng ver_num

  CmpFlag=1
  jpat=GetSrvState(5)

  ver_num = VAL(VER$(0))
  if ver_num >= REL_8SMRT then
    rbt_jpat2=GETENV(cnfSRV,2108)
    rbt_joint2=0
    b_pat=1
    for jnt=1 to MAXJOINT
      rsel=rbt_jpat2 AND b_pat
      if rsel = b_pat then
        rbt_joint2=rbt_joint2+1
      end if
      b_pat = b_pat*2
	next
  else
    rbt_jpat2=RBT_JPAT
    rbt_joint2=RBT_JOINT
  endif

  'rsel=jpat AND RBT_JPAT
  rsel=jpat AND rbt_jpat2

  if rsel = 0 then

  '"Robot and the external joints move synchronously"
    'add_jpat = RBT_JPAT+1
    add_jpat = rbt_jpat2+1
    'for jnt=RBT_JOINT+1 to MAXJOINT
    for jnt=rbt_joint2+1 to MAXJOINT
      rsel=jpat AND add_jpat
      if rsel = add_jpat then
        targetj = jnt+20
        CmpFlag=GetSrvState(targetj)
        EXIT FOR
      end if
      add_jpat = add_jpat*2
    next
  else

  '"Robot and the external joints move independently"
    CmpFlag=GetSrvState(20)
  end if
END
