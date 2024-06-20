'----------------------------------------
'!Title      
'!Author     DENSO WAVE INCORPORATED
'!Date       
'!Link       
'!Include    <pacman.h>
'!CalledPrg
'
'!ARG 1     "Axis number",1,"0"
'----------------------------------------

#INCLUDE  <pacman.h>
#ifdef  __VERTICAL_ROBOT__
	#define RBT_JOINT	6
	#define RBT_JPAT	63
#else
	#define RBT_JOINT	4
	#define RBT_JPAT  15
#endif

PROGRAM ResetCollisionJnt(jnt%)
defint bpat,coljpat,jtn

TAKEARM KEEP=1

if jnt > RBT_JOINT then
	PRINTMSG "Excess in effective joint value range",0,"ResetCollisionJnt.pac"
	END
endif

coljpat=GETENV(cnfSPD,206)
bpat=1
for jtn = 1 to jnt-1
	bpat=bpat*2
next

if (coljpat AND bpat)=0 then	'""
	END
else
	coljpat = coljpat AND (NOT(bpat))
	LETENV cnfSPD,206,coljpat
endif
GIVEARM
END
