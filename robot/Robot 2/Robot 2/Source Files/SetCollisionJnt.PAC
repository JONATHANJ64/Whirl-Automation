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

PROGRAM SetCollisionJnt(jnt%)
defint prcctrl,bpat,coljpat,jtn

if jnt > RBT_JOINT then
	PRINTMSG "Excess in effective joint value range",0,"SetCollisionJnt.pac"
	END
endif

prcctrl=GETENV(cnfSPD,204)
if prcctrl = 0 then	'""
	LETENV cnfSPD,204,1
endif

coljpat=GETENV(cnfSPD,206)
bpat=1
for jtn = 1 to jnt-1
	bpat=bpat*2
next

'""
if (coljpat AND bpat)=0 then
	coljpat = coljpat OR bpat
	LETENV cnfSPD,206,coljpat
endif

END
