'!TITLE "<Title>"
PROGRAM PRO1

#DEFINE PART_TO_PICK I10
#DEFINE SKIP_HANDLE_PRESS_PINS I11
#DEFINE SKIP_HOPPER_PRESS_PINS I12
#DEFINE SKIP_VAC_CHECKS I13
#DEFINE POS_COUNTER I14
#DEFINE NEAREST_POINT I15
#DEFINE CUR_MOTION_COMP I16
#DEFINE SKIP_SENSOR_CHECKS I17
#DEFINE NEAREST_POINT_TOFFSET I18
#DEFINE TOOL_OFFSET I19
#DEFINE SENSOR_RESPONSE_TIMEOUT I20
#DEFINE SKIP_PP_SENSOR_CHECKS I21
#DEFINE CAMERA_NOT_BLOCKED I22
#DEFINE REQUEST_AIR1_OFF I23
#DEFINE REQUEST_AIR1_ON I24
#DEFINE MOVING_TO_PARK I25
#DEFINE ACK_AIR1_OFF I26
#DEFINE ACK_AIR1_ON I27
#DEFINE SKIP_COL_DETECTION I28
#DEFINE PREFETCH_PART I30
#DEFINE PREFETCH_FINISHED I31
#DEFINE R_WAITING I32
#DEFINE HANDLE_PLACED_OK I40
#DEFINE HOPPER_PLACED_OK I41
#DEFINE AGITATOR_PLACED_OK I42
#DEFINE HOPPER_PICKED I43
#DEFINE HANDLE_PICKED I60
#DEFINE AGITATOR_PICKED I62
#DEFINE REQUEST_ROTATOR_OPEN I64
#DEFINE REQUEST_ROTATOR_CLOSED I65
#DEFINE REQUEST_ROTATOR_HOME I66
#DEFINE REQUEST_ROTATOR_180 I67
#DEFINE PART_IN_FIXTURE I69
#DEFINE TASK_COMPLETED I50
#DEFINE PARK_COMPLETE I70
#DEFINE ERR_SENSOR_CLOSED I80
#DEFINE ERR_SENSOR_OPEN I81
#DEFINE ERR_PICKPART I82
#DEFINE ERR_PLACER_EXT I83
#DEFINE ERR_PLACER_RET I84
#DEFINE ERR_PICKER_EXT I85
#DEFINE ERR_PICKER_RET I86
#DEFINE ERR_HANDLE_PRESS_PINS I87
#DEFINE ERR_HOPPER_PRESS_PINS I88
#DEFINE ERR_VAC_SENSOR_PICK I89
#DEFINE ERR_VAC_SENSOR_PLACE I90
#DEFINE BESTFIG I95
#DEFINE MAX_POS_DIST F11
#DEFINE POS_DIST_TEMP F12
#DEFINE POS_CHECK_DISTANCE F13
#DEFINE SPDSLOW F50
#DEFINE SPD20 F51
#DEFINE SPD40 F52
#DEFINE SPD60 F53
#DEFINE SPD80 F54
#DEFINE SPD100 F55
#DEFINE SPDRAPID F56
#DEFINE P_TEMP1 P198
#DEFINE P_TEMP2 P199



RESETAREA 1      'Handle

RESETAREA 2      'Agitator

TAKEARM
GIVEARM

GOSUB *COL_DETECT_OFF

TAKEARM

IF IO[31] = OFF THEN
  MOTOR ON
END IF

CHANGEWORK 1

CHANGETOOL 0

SENSOR_RESPONSE_TIMEOUT = 0
 
POS_COUNTER = 0

POS_DIST_TEMP = 0

TASK_COMPLETED = 0

HOPPER_PICKED = 0

HANDLE_PICKED = 0

HANDLE_PLACED_OK = 0

HOPPER_PLACED_OK = 0

AGITATOR_PLACED_OK = 0

AGITATOR_PICKED = 0

CUR_MOTION_COMP = 0

REQUEST_AIR1_OFF = 0

REQUEST_AIR1_ON = 0

REQUEST_ROTATOR_OPEN = 0

REQUEST_ROTATOR_CLOSED = 0

REQUEST_ROTATOR_HOME = 0

REQUEST_ROTATOR_180 = 0

ACK_AIR1_OFF = 0

ACK_AIR1_ON = 0

ERR_SENSOR_CLOSED = 0

ERR_SENSOR_OPEN = 0

ERR_PICKPART = 0

ERR_PLACER_EXT = 0

ERR_PLACER_RET = 0

ERR_PICKER_EXT = 0

ERR_PICKER_RET = 0

ERR_HANDLE_PRESS_PINS = 0

ERR_HOPPER_PRESS_PINS = 0

ERR_VAC_SENSOR_PICK = 0

ERR_VAC_SENSOR_PLACE = 0

PARK_COMPLETE = 0

PREFETCH_FINISHED = 0

R_WAITING = 0

GOSUB *VAC_OFF

IF (SKIP_PP_SENSOR_CHECKS = 0) THEN
	IF (IO[8] = ON) OR (IO[15] = ON) THEN																		 'Make sure agitator picker and placer are retracted before starting
		GOSUB *RETRACT_AG_PICKER
		GOSUB *RETRACT_AG_PLACER
	END IF
ELSE
	GOSUB *RETRACT_AG_PICKER
	GOSUB *RETRACT_AG_PLACER
END IF


ON PART_TO_PICK GOSUB *RIGHT_HANDLE, *HOPPER, *AGITATOR, *RIGHT_HANDLE_REVERSED, *MOVE_TO_PARK               'PART_TO_PICK = 1 Pick Right handle, PART_TO_PICK = 2 pick Hopper, PART_TO_PICK = 3 Pick Agitator, PART_TO_PICK = 4 Go Home

PART_TO_PICK = 0

TASK_COMPLETED = 1

END

'----------------------------------------------------------------------------------------------------------------

*RIGHT_HANDLE:      ' Pick Right Handle


              ''' Transfer Cognex location values stored in D variables 10-12 to robot point variables
              ''' D variables at 20 for other parts.          

    PART_TO_PICK = 0
	ST_ASPCHANGE 3
    
    RESETAREA 1

    GOSUB *CLOSEHAND    
    CAMERA_NOT_BLOCKED = 1
    CHANGETOOL 0
    LETRZ P11 = D12
    MOVE P, @P P[11], NEXT

  
    LETX P40 = D10
    LETY P40 = D11
    LETRZ P40 = D12 

    LETX P41 = D10
    LETY P41 = D11
    LETRZ P41 = D12

  LETF P40 = 1
    J40 = P2J(P40)
    IF (JOINT(4, J40) >= 90) OR (JOINT(4, J40) <= -90) THEN
      LETF P40 = 5
    ENDIF

  P_TEMP1 = P40
  P_TEMP2 = P41
  GOSUB *SHORTEST_MOVE                  'Calculate the best figure for P41
  LETF P41 = BESTFIG
                  
    SPEED 75
    CAMERA_NOT_BLOCKED = 0

    SETAREA 1

    MOVE P, @P P[40]
    SPEED 40
    MOVE P, @0 P[41]
    GOSUB *PICKPARTOPEN            ' Handle picked here
    MOVE P, @P P[40]

    RESETAREA 1

    SPEED 100
    MOVE P, @P P[11]
	MOVE P, @P P[43]
	MOVE P, @E P[122]
	IF PREFETCH_PART = 1 THEN
 	    HANDLE_PICKED = 1
   	    CAMERA_NOT_BLOCKED = 1
		PREFETCH_FINISHED = 1
		WAIT PREFETCH_PART = 0
		PREFETCH_FINISHED = 0
	END IF
	'MOVE P, @P P[144]
	DECEL 10
    MOVE P, @P P[44]
    HANDLE_PICKED = 1
    CAMERA_NOT_BLOCKED = 1
    MOVE L, @P P[45], NEXT
	ARRIVE 95
  'DO UNTIL CUR_MOTION_COMP = 1
      'CALL MOTIONCOMP (CUR_MOTION_COMP)
	  'DELAY 20
    'LOOP
  'CUR_MOTION_COMP = 0
  REQUEST_AIR1_OFF = 1
  R_WAITING = 1
  WAIT ACK_AIR1_OFF = 1
  R_WAITING = 0
  MOVE L, @0 P[130]
  MOVE L, @0 P[131]
  ARRIVE 99
  MOVE L, @0 P[132], NEXT
  ARRIVE 99

  RESET IO[65]						'Closing hand without checking sensors here, because robot air has been turned off for part to relax.  Hand valves change state but hand does not close yet.
  SET IO[66]

  REQUEST_AIR1_ON = 1
  R_WAITING = 1
  WAIT ACK_AIR1_ON = 1
  R_WAITING = 0
  REQUEST_AIR1_OFF = 0
  REQUEST_AIR1_ON = 0
  ACK_AIR1_OFF = 0
  ACK_AIR1_ON = 0

	IF (SKIP_SENSOR_CHECKS = 0) THEN
	    WAIT IO[14] = ON, 2000, SENSOR_RESPONSE_TIMEOUT						'Check hand closed sensors here after air has been turned back on
		IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
			ERR_SENSOR_CLOSED = 1
			R_WAITING = 1 
	        WAIT ERR_SENSOR_CLOSED = 0 
			R_WAITING = 0
	        STOP
	    END IF
	END IF

	SPEED 100
    MOVE L, @P P[45]
    MOVE L, @P P[47]
    MOVE L, @0 P[48]
  DELAY 250
    GOSUB *VERIFY_HANDLE_PRESS_PINS
    MOVE L, @P P[49]
    MOVE P, @P P[50]
    MOVE L, @0 P[51]
  DELAY 250
    MOVE L, @P P[50]
	DECEL 20
    MOVE P, @P P[54]
    MOVE L, @P P[55]
    MOVE L, @P P[56]
    GOSUB *OPENHAND
    MOVE L, @E P[57]
    GOSUB *PICKPARTCLOSED          'Take Handle Assembly
	DECEL 50
    MOVE L, @P P[58]
    MOVE L, @P P[59]
    MOVE L, @P P[60]
    MOVE L, @0 P[61]
    MOVE L, @E P[62]
    GOSUB *OPENHAND
    MOVE L, @P P[63]
  SPEED 80
    MOVE L, @P P[64]
    CAMERA_NOT_BLOCKED = 0
    MOVE P, @P P[65]
	DECEL 20
    MOVE P, @P P[99], NEXT
	ARRIVE 30
    HANDLE_PLACED_OK = 1          'Announce part has been placed
	ARRIVE 98
    CAMERA_NOT_BLOCKED = 1

  SPEED 5

RETURN

'----------------------------------------------------------------------------------------------------------------

*RIGHT_HANDLE_REVERSED:    'Pick reversed handle

              ''' Transfer Cognex location values stored in D variables 10-12 to robot point variables
              ''' D variables at 20 for other parts.          

    PART_TO_PICK = 0
	ST_ASPCHANGE 3
    
    RESETAREA 1

    GOSUB *CLOSEHAND    
    CAMERA_NOT_BLOCKED = 1
    CHANGETOOL 0
    SPEED 75
    LETRZ P11 = D12 
    MOVE P, @P P[11], NEXT

  REQUEST_ROTATOR_OPEN = 1
  REQUEST_ROTATOR_HOME = 1
   

  LETX P110 = D10
    LETY P110 = D11
    LETRZ P110 = D12 

    LETX P111 = D10
    LETY P111 = D11
    LETRZ P111 = D12

  LETF P110 = 1
    J40 = P2J(P110)
    IF (JOINT(4, J40) >= 90) OR (JOINT(4, J40) <= -90) THEN
      LETF P110 = 5
    ENDIF

  P_TEMP1 = P110
  P_TEMP2 = P111
  GOSUB *SHORTEST_MOVE                  'Calculate the best figure for P111
  LETF P111 = BESTFIG 

    
    CAMERA_NOT_BLOCKED = 0

    SETAREA 1
    MOVE P, @P P[110]
    SPEED 40
    MOVE P, @0 P[111]

	R_WAITING = 1
    WAIT REQUEST_ROTATOR_OPEN = 0
	R_WAITING = 0
	R_WAITING = 1
    WAIT REQUEST_ROTATOR_HOME = 0
	R_WAITING = 0


    GOSUB *PICKPARTOPEN            ' Handle picked here
    MOVE P, @P P[110]

    RESETAREA 1

    SPEED 100
    MOVE P, @P P[115]
  REQUEST_ROTATOR_OPEN = 1
  R_WAITING = 1
  WAIT REQUEST_ROTATOR_OPEN = 0
  R_WAITING = 0
  HANDLE_PICKED = 1
  SPEED 50
  MOVE P, @0 P[116], NEXT
  ARRIVE 99
  REQUEST_ROTATOR_CLOSED = 1
  R_WAITING = 1
  WAIT REQUEST_ROTATOR_CLOSED = 0
  'PART_IN_FIXTURE = 1
  R_WAITING = 0
  GOSUB *CLOSEHAND
  SPEED 100
  MOVE L, @P P[117]
  MOVE P, @P P[118], NEXT
  ARRIVE 99
  REQUEST_ROTATOR_180 = 1
  R_WAITING = 1
  WAIT REQUEST_ROTATOR_180 = 0
  R_WAITING = 0
  MOVE P, @P P[117]
  MOVE P, @P P[119]
  MOVE L, @0 P[120]
  GOSUB *PICKPARTOPEN
  REQUEST_ROTATOR_OPEN = 1
  R_WAITING = 1
  WAIT REQUEST_ROTATOR_OPEN = 0
  PART_IN_FIXTURE = 0
  R_WAITING = 0
  MOVE L, @P P[121]
  MOVE P, @E P[122]
  'MOVE P, @E P[123]
  IF PREFETCH_PART = 1 THEN
    CAMERA_NOT_BLOCKED = 1
	PREFETCH_FINISHED = 1
	WAIT PREFETCH_PART = 0
	PREFETCH_FINISHED = 0
  END IF
	'MOVE P, @P P[144]
    MOVE P, @P P[44]
    CAMERA_NOT_BLOCKED = 1
    MOVE L, @P P[45], NEXT
	ARRIVE 99
  REQUEST_AIR1_OFF = 1
  R_WAITING = 1
  WAIT ACK_AIR1_OFF = 1
  R_WAITING = 0
  MOVE L, @0 P[130]
  MOVE L, @0 P[131]
  ARRIVE 99
  MOVE L, @0 P[132], NEXT
  ARRIVE 99

  RESET IO[65]						'Closing hand without checking sensors here, because robot air has been turned off for part to relax.
  SET IO[66]

  REQUEST_AIR1_ON = 1
  R_WAITING = 1
  WAIT ACK_AIR1_ON = 1
  R_WAITING = 0
  REQUEST_AIR1_OFF = 0
  REQUEST_AIR1_ON = 0
  ACK_AIR1_OFF = 0
  ACK_AIR1_ON = 0
	
	IF (SKIP_SENSOR_CHECKS = 0) THEN
    WAIT IO[14] = ON, 2000, SENSOR_RESPONSE_TIMEOUT						'Check hand closed sensors here after air has been turned back on
		IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
			ERR_SENSOR_CLOSED = 1
			R_WAITING = 1 
	        WAIT ERR_SENSOR_CLOSED = 0 
			R_WAITING = 0
	        STOP
	    END IF	
	END IF
	
	SPEED 100
    MOVE L, @P P[45]
    MOVE L, @P P[47]
    MOVE L, @0 P[48]
  DELAY 250
    GOSUB *VERIFY_HANDLE_PRESS_PINS
    MOVE L, @P P[49]
    MOVE P, @P P[50]
    MOVE L, @0 P[51]
  DELAY 250
    MOVE L, @P P[50]
	DECEL 20
    MOVE P, @P P[54]
    MOVE L, @P P[55]
    MOVE L, @P P[56]
    GOSUB *OPENHAND
    MOVE L, @E P[57]
    GOSUB *PICKPARTCLOSED                'Take handle assembly
	DECEL 50
    MOVE L, @P P[58]
    MOVE L, @P P[59]
    MOVE L, @P P[60]
    MOVE L, @0 P[61]
    MOVE L, @E P[62]
    GOSUB *OPENHAND
    MOVE L, @P P[63]
  SPEED 80
    MOVE L, @P P[64]
    CAMERA_NOT_BLOCKED = 0
    MOVE P, @P P[65]
	DECEL 20
    MOVE P, @P P[99], NEXT
	ARRIVE 30
    HANDLE_PLACED_OK = 1          'Announce part has been placed
	ARRIVE 98
    CAMERA_NOT_BLOCKED = 1

  SPEED 5

RETURN
    
 '---------------------------------------------------------------------------------------------------------------- 

*HOPPER:        ' Pick hopper
      
    PART_TO_PICK = 0
	ST_ASPCHANGE 3
    
    GOSUB *CLOSEHAND
    CAMERA_NOT_BLOCKED = 1
    CHANGETOOL 0
    SPEED 75
    CAMERA_NOT_BLOCKED = 0
    MOVE P, @P P[20]
	DECEL 20
    MOVE P, @P P[21]
    CAMERA_NOT_BLOCKED = 1
    MOVE L, @3 P[22]
	'GOSUB *MOTIONCOMPLETE
    MOVE L, @E P[23]
    RESET IO[66]				'Dont check hand open sensor here, will check hopper presence sensor instead to make sure hopper is picked.
	SET IO[65]
	DELAY 750
  MOVE L, @0 P[30]
'  DO UNTIL CUR_MOTION_COMP = 1
'      CALL MOTIONCOMP (CUR_MOTION_COMP)
'	  DELAY 20
'  LOOP
'  CUR_MOTION_COMP = 0
  HOPPER_PICKED = 1            'Announce part has been picked
  'MOVE L, @P P[31]
  'GOSUB *MOTIONCOMPLETE
  'MOVE L, @0 P[32]
  'MOVE P, @P P[31]
    CAMERA_NOT_BLOCKED = 0
	SPEED 100
	DECEL 30
    MOVE P, @P P[24]
    MOVE P, @P P[25]
    MOVE L, @P P[26]
    MOVE L, @0 P[27]
  SPEED 40
  MOVE L, @0 P[33]
  MOVE L, @P P[34]
  MOVE L, @P P[35]
  MOVE L, @E P[33]
    CAMERA_NOT_BLOCKED = 1
    GOSUB *CLOSEHAND
    SPEED 20
    MOVE L, @0 P[28]
  GOSUB *VERIFY_HOPPER_PRESS_PINS    
  MOVE L, @E P[29]
    SPEED 30
    MOVE L, @P P[27]
    CAMERA_NOT_BLOCKED = 0
    SPEED 75
    MOVE L, @P P[26]
	DECEL 20
    MOVE P, @P P[99], NEXT
	ARRIVE 30
    HOPPER_PLACED_OK = 1          'Announce part has been placed
	ARRIVE 98
    CAMERA_NOT_BLOCKED = 1

  SPEED 5

RETURN

'----------------------------------------------------------------------------------------------------------------    
  
*AGITATOR:       ' Pick Agitator

      
    PART_TO_PICK = 0
	ST_ASPCHANGE 3

    CAMERA_NOT_BLOCKED = 1
    SPEED 100
    CHANGETOOL 1
    MOVE P, @P P[13], NEXT

  
    LETX P70 = D30
    LETY P70 = D31
    LETRZ P70 = D32 

    LETX P71 = D30
    LETY P71 = D31
    LETRZ P71 = D32
      
    RESETAREA 2

    IF (D32 <= 90) AND (D32 >= -90)  THEN   '  Checking to determine if part is rotated more than 90 degrees in either direction


      CAMERA_NOT_BLOCKED = 0

      SETAREA 2
    
      SPEED 50
      MOVE L, @0 P[70]
      GOSUB *EXTEND_AG_PICKER
      GOSUB *VAC_ON
      MOVE L, @E P[71]
	  DELAY 350
      RESETAREA 2

      SPEED 100
	  ACCEL 50
      MOVE L, @P P[72]
      MOVE P, @P P[74]
    AGITATOR_PICKED = 1
	  SPEED 50
      MOVE L, @0 P[75], NEXT
	  ARRIVE 99 
      MOVE L, @0 P[76], NEXT
	  ARRIVE 99
      GOSUB *VAC_OFF
      GOSUB *VERIFY_VAC_PLACE
	  SPEED 20
      MOVE L, @P P[77]
	  SPEED 100
	  DECEL 20
      GOSUB *RETRACT_AG_PICKER
      MOVE L, @P P[78], NEXT
      GOSUB *EXTEND_AG_PLACER
	  ACCEL 30
      MOVE P, @P P[79]
      MOVE L, @P P[80]
	  SPEED 50
      MOVE L, @0 P[81], NEXT
	  ARRIVE 99
      GOSUB *VAC_ON
      GOSUB *VERIFY_VAC_PICK
      MOVE L, @0 P[80], NEXT
	  ARRIVE 99						
	  SPEED 100
	  ACCEL 20
	  DECEL 20
      MOVE P, @P P[82]
      MOVE P, @P P[83]
      MOVE P, @0 P[84]
	  ARRIVE 99
	  GOSUB *VERIFY_VAC_PICK
      GOSUB *VAC_OFF
	  GOSUB *VERIFY_VAC_PLACE
      CAMERA_NOT_BLOCKED = 1
	  DELAY 500
      MOVE L, @0 P[85], NEXT
	  ARRIVE 99
	  ACCEL 50
      MOVE L, @P P[84]
      MOVE L, @P P[83], NEXT
      GOSUB *RETRACT_AG_PLACER
      CAMERA_NOT_BLOCKED = 0
      CHANGETOOL 0
      MOVE P, @P P[99], NEXT
	  ARRIVE 30
      AGITATOR_PLACED_OK = 1          'Announce part has been placed
	  ARRIVE 98
      CAMERA_NOT_BLOCKED = 1

    SPEED 5


    ELSEIF (D32 > 90) OR (D32 < -90)  THEN   
                            

                            '  Adding 180 to rotation value so that robot always picks part away from conveyor(picking part backwards).
      LETRZ P70 = (D32 + 180)           '
      LETRZ P71 = (D32 + 180)             '




      CAMERA_NOT_BLOCKED = 0

	  SETAREA 2

	  SPEED 50
      MOVE L, @0 P[70]
      GOSUB *EXTEND_AG_PICKER
      GOSUB *VAC_ON
      MOVE L, @E P[71]
	  DELAY 350

	  RESETAREA 2

	  SPEED 100
	  ACCEL 50
      MOVE L, @P P[72]
      MOVE P, @P P[86]
      AGITATOR_PICKED = 1
	  SPEED 50
      MOVE P, @0 P[88], NEXT
	  ARRIVE 99
      MOVE L, @0 P[89], NEXT
	  ARRIVE 99
      GOSUB *VAC_OFF
      GOSUB *VERIFY_VAC_PLACE
	  SPEED 20
      MOVE L, @0 P[90]
	  SPEED 75
	  DECEL 20
      GOSUB *RETRACT_AG_PICKER
	  SPEED 100
      MOVE P, @P P[86]
      MOVE L, @P P[78]
      GOSUB *EXTEND_AG_PLACER
	  SPEED 75
	  ACCEL 20
	  DECEL 20
      MOVE P, @P P[79]
      MOVE L, @P P[80]
	  SPEED 50
      MOVE L, @0 P[81], NEXT
	  ARRIVE 99
      GOSUB *VAC_ON
      GOSUB *VERIFY_VAC_PICK
      MOVE L, @0 P[80], NEXT 	
	  ARRIVE 99				
	  SPEED 100
	  ACCEL 20
	  DECEL 20
      MOVE P, @P P[82]
      MOVE P, @P P[83]
      MOVE P, @0 P[84]
	  ARRIVE 99
	  GOSUB *VERIFY_VAC_PICK
      GOSUB *VAC_OFF
      GOSUB *VERIFY_VAC_PLACE
      CAMERA_NOT_BLOCKED = 1
	  DELAY 500
      MOVE L, @0 P[85], NEXT
	  ARRIVE 99
	  ACCEL 50
      MOVE L, @P P[84]
      MOVE L, @P P[83], NEXT
      GOSUB *RETRACT_AG_PLACER
      CAMERA_NOT_BLOCKED = 0
      CHANGETOOL 0
      MOVE P, @P P[99], NEXT
	  ARRIVE 30
      AGITATOR_PLACED_OK = 1        'Announce part has been placed  
	  ARRIVE 98
      CAMERA_NOT_BLOCKED = 1
    SPEED 5

    END IF

RETURN

'----------------------------------------------------------------------------------------------------------------
*CLOSEHAND:

    RESET IO[65]
    SET IO[66]
    IF SKIP_SENSOR_CHECKS = 1 THEN
	  DELAY 250
      RETURN
    ELSE
		IF IO[14] = OFF THEN  
	      WAIT IO[14] = ON, 2000, SENSOR_RESPONSE_TIMEOUT
	      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
	        ERR_SENSOR_CLOSED = 1
			R_WAITING = 1 
	        WAIT ERR_SENSOR_CLOSED = 0 
			R_WAITING = 0
	        STOP
	      END IF
		END IF
    END IF
RETURN

'----------------------------------------------------------------------------------------------------------------
*OPENHAND:

    SET IO[65]
    RESET IO[66]
    IF SKIP_SENSOR_CHECKS = 1 THEN
	  DELAY 250
      RETURN
    ELSE
		IF IO[13] = OFF THEN   
	      WAIT IO[13] = ON, 2000, SENSOR_RESPONSE_TIMEOUT
	      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
	        ERR_SENSOR_OPEN = 1
			R_WAITING = 1 
	        WAIT ERR_SENSOR_OPEN = 0 
			R_WAITING = 0
	        STOP
	      END IF
		END IF
    END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*PICKPARTCLOSED:

    RESET IO[65]
    SET IO[66]
    IF SKIP_SENSOR_CHECKS = 1 THEN
	  DELAY 250
      RETURN
    ELSE
	  DELAY 250  
      WAIT (IO[13] = OFF) AND (IO[14] = OFF), 2000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PICKPART = 1
		R_WAITING = 1
        WAIT ERR_PICKPART = 0
		R_WAITING = 0
        STOP
      END IF
    END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*PICKPARTOPEN:

    RESET IO[66]
    SET IO[65]
    IF SKIP_SENSOR_CHECKS = 1 THEN
      DELAY 250
      RETURN
    ELSE 
	  DELAY 400  
      WAIT (IO[13] = OFF) AND (IO[14] = OFF), 2000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PICKPART = 1
		R_WAITING = 1
        WAIT ERR_PICKPART = 0
		R_WAITING = 0
        STOP
      END IF
    END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*EXTEND_AG_PICKER:

  RESET IO[70]
  SET IO[69]
  IF SKIP_PP_SENSOR_CHECKS = 1 THEN
    DELAY 750
    RETURN
  ELSE  
      WAIT IO[15] = ON, 3000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PICKER_EXT = 1
		R_WAITING = 1 
        WAIT ERR_PICKER_EXT = 0 
		R_WAITING = 0
        STOP
      END IF
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*RETRACT_AG_PICKER:

  RESET IO[69]
  SET IO[70]
   IF SKIP_PP_SENSOR_CHECKS = 1 THEN
      DELAY 750
      RETURN
   ELSE  
    WAIT IO[10] = ON, 3000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PICKER_RET = 1
		R_WAITING = 1 
        WAIT ERR_PICKER_RET = 0 
		R_WAITING = 0
        STOP
      END IF
   END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*EXTEND_AG_PLACER:

  RESET IO[68]
  SET IO[67]
  IF SKIP_PP_SENSOR_CHECKS = 1 THEN
  	  DELAY 750
      RETURN
  ELSE  
    WAIT IO[8] = ON, 3000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PLACER_EXT = 1
		R_WAITING = 1 
        WAIT ERR_PLACER_EXT = 0 
		R_WAITING = 0
        STOP
      END IF
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*RETRACT_AG_PLACER:

  RESET IO[67]
  SET IO[68]
  IF SKIP_PP_SENSOR_CHECKS = 1 THEN
      DELAY 750
      RETURN
  ELSE  
    WAIT IO[9] = ON, 3000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_PLACER_RET = 1 
		R_WAITING = 1
        WAIT ERR_PLACER_RET = 0 
		R_WAITING = 0
        STOP
      END IF
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*VAC_ON:

  SET IO[64]

RETURN

'----------------------------------------------------------------------------------------------------------------

*VAC_OFF:

  RESET IO[64]

RETURN

'----------------------------------------------------------------------------------------------------------------

*VERIFY_VAC_PICK:

  IF SKIP_VAC_CHECKS = 1 THEN
      RETURN
  ELSE 
  	IF IO[48] = OFF THEN  
      WAIT IO[48] = ON, 2000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_VAC_SENSOR_PICK = 1
		R_WAITING = 1 
        WAIT ERR_VAC_SENSOR_PICK = 0 
		R_WAITING = 0
        STOP
      END IF
	END IF
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*VERIFY_VAC_PLACE:

  IF SKIP_VAC_CHECKS = 1 THEN
      RETURN
  ELSE
  	IF IO[48] = ON THEN 
      WAIT IO[48] = OFF, 2000, SENSOR_RESPONSE_TIMEOUT
      IF (SENSOR_RESPONSE_TIMEOUT = FALSE) THEN
        ERR_VAC_SENSOR_PLACE = 1
		R_WAITING = 1 
        WAIT ERR_VAC_SENSOR_PLACE = 0 
		R_WAITING = 0
        STOP
      END IF
	END IF
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*VERIFY_HOPPER_PRESS_PINS:

  IF SKIP_HOPPER_PRESS_PINS = 1 THEN
      RETURN
  ELSE 
      WAIT IO[12] = ON, 2000, SENSOR_RESPONSE_TIMEOUT
          IF (SENSOR_RESPONSE_TIMEOUT = 0) THEN
        	ERR_HOPPER_PRESS_PINS = 1
			R_WAITING = 1 
        	WAIT ERR_HOPPER_PRESS_PINS = 0 
			R_WAITING = 0
        	STOP
          END IF 
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*VERIFY_HANDLE_PRESS_PINS:

  IF SKIP_HANDLE_PRESS_PINS = 1 THEN
    RETURN
  ELSE 
        WAIT IO[11] = ON, 2000, SENSOR_RESPONSE_TIMEOUT
          IF (SENSOR_RESPONSE_TIMEOUT = 0) THEN
          	ERR_HANDLE_PRESS_PINS = 1
			R_WAITING = 1 
          	WAIT ERR_HANDLE_PRESS_PINS = 0 
			R_WAITING = 0
          	STOP
          END IF 
  END IF
RETURN

'----------------------------------------------------------------------------------------------------------------

*MOTIONCOMPLETE:

	DO UNTIL CUR_MOTION_COMP = 1
		CALL MOTIONCOMP (CUR_MOTION_COMP)
	LOOP
	CUR_MOTION_COMP = 0	

RETURN

'----------------------------------------------------------------------------------------------------------------

*SHORTEST_MOVE:
  
  DEFDBL JDIST = 0
  DEFDBL BEST_DIST = 10000
  DEFINT BEST_FIG = 0
  DEFINT II = 0
  DEFINT XX = 0
  DIM IIA% (7)
  IIA(0) = 1
  IIA(1) = 5
  IIA(2) = 9
  IIA(3) = 13
  IIA(4) = 21
  IIA(5) = 25
  IIA(6) = 29
  DEFINT ERRORCODE = 0

  J90 = P2J(P_TEMP1)
  FOR II = 0 TO 6
    LETF P_TEMP2 = IIA(II)
    J91 = P2J(P_TEMP2, ERRORCODE)
    FOR XX = 1 TO 6
      JDIST = JDIST + ABS(JOINT(XX, J90) - JOINT(XX, J91))
    NEXT
    IF JDIST < BEST_DIST THEN
      BEST_DIST = JDIST
      BEST_FIG = FIG(P_TEMP2)
    END IF
    JDIST = 0
  NEXT
  BESTFIG = BEST_FIG

RETURN

'----------------------------------------------------------------------------------------------------------------

*COL_DETECT_ON:

	  CALL SetCollisionJnt(1)
	  CALL SetCollisionJnt(2)
	  CALL SetCollisionJnt(3)
	  CALL SetCollisionJnt(4)
	  CALL SetCollisionJnt(5)
	  CALL SetCollisionJnt(6)
	  TAKEARM KEEP=1

RETURN

'----------------------------------------------------------------------------------------------------------------

*COL_DETECT_OFF:

	  CALL ResetCollisionJnt(1)
	  CALL ResetCollisionJnt(2)
	  CALL ResetCollisionJnt(3)
	  CALL ResetCollisionJnt(4)
	  CALL ResetCollisionJnt(5)
	  CALL ResetCollisionJnt(6)
	  TAKEARM KEEP=1

RETURN

'----------------------------------------------------------------------------------------------------------------

*MOVE_TO_PARK:

  ST_ASPCHANGE 0
  IF SKIP_COL_DETECTION = 0 THEN
	GOSUB *COL_DETECT_ON
  ELSE
  	SKIP_COL_DETECTION = 0	
  END IF


  MOVING_TO_PARK = 1

  RESETAREA 1
  RESETAREA 2

  CHANGETOOL 0
  SPEED 20
  IF (PREFETCH_PART = 1) AND (DIST(CURPOS, P[122]) < 5.0) AND (POSX(P11) < 999.0) THEN
	MOVE P, @P P[43]
	MOVE P, @P P[11]
	MOVE P, @0 P[40]
	GOSUB *CLOSEHAND
	MOVE P, @P P[11]
	CHANGETOOL 0
	MOVE P, @P P[99]
  ELSE

	PART_TO_PICK = 0
	NEAREST_POINT = -1
	SPEED 20
	DIM CURRENTPOS AS POSITION
	DIM CURRENT_P_VALUES AS POSITION
	POS_CHECK_DISTANCE = MAX_POS_DIST

	FOR TOOL_OFFSET = 0 TO 1
		CHANGETOOL TOOL_OFFSET
	FOR POS_COUNTER = 10 TO 145               			 'Find nearest taught point from current robot position within distance of variable MAX_POS_DIST
	  CURRENT_P_VALUES = P[POS_COUNTER]
	  IF POSX(CURRENT_P_VALUES) + POSY(CURRENT_P_VALUES) + POSZ(CURRENT_P_VALUES) <> 0 THEN			'Dont check unused position variables
	    POS_DIST_TEMP = DIST(CURPOS, P[POS_COUNTER])
	    IF POS_DIST_TEMP < MAX_POS_DIST THEN
	      IF POS_DIST_TEMP < POS_CHECK_DISTANCE THEN
	        POS_CHECK_DISTANCE = POS_DIST_TEMP
	        NEAREST_POINT = POS_COUNTER
	        NEAREST_POINT_TOFFSET = TOOL_OFFSET
	      END IF
	    END IF
	  END IF
	NEXT
	NEXT

	CHANGETOOL NEAREST_POINT_TOFFSET

	SELECT CASE NEAREST_POINT

	CASE 99        'Near park position
	  MOVE P, @0 P[99]

	CASE 45 TO 48    'Placing handle positions
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @P P[44]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 56 TO 57    'Grabbing handle from pallet
	  GOSUB *OPENHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[56]
	  MOVE P, @0 P[55]
	  MOVE P, @0 P[54]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 61 TO 62    'inserting handle
	  GOSUB *OPENHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[61]
	  MOVE L, @0 P[60]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 21 TO 23    'picking hopper
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	MOVE L, @0 P[21]
	  MOVE L, @0 P[20]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 27 TO 29    'Placing Hopper
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[26]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 30 TO 32  'Align hopper after picking
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	MOVE L, @P P[21]
	MOVE L, @P P[20]
	MOVE P, @0 P[99]

	CASE 33 TO 35    'Placing Hopper tilt
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[26]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 43			'Handle prefetch position
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	CHANGETOOL 0
	  MOVE P, @0 P[99]		


	CASE 84 TO 85    'Placing Agitator
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[83]
	  CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 88 TO 90    'Picking Agitator 
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[86]
	  CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 110 TO 111 'Picking Reverse Right Handle
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 115 TO 119    'Working with flip fixture
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[11]
	  CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 120 TO 122    'Departing flip fixture
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @0 P[119]
	MOVE L, @0 P[11]
	  CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 130 TO 132    'Placing handle positions alternate
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  MOVE L, @P P[44]
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE 144
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	CHANGETOOL 0
	  MOVE P, @0 P[99]

	CASE -1        ' Not near any taught point within distance of variable MAX_POS_DIST
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  CHANGETOOL 0
	SPEED 5
	  MOVE P, @0 P[99]

	CASE ELSE
	  GOSUB *CLOSEHAND
	  GOSUB *VAC_OFF
	  GOSUB *RETRACT_AG_PICKER
	  GOSUB *RETRACT_AG_PLACER
	  CHANGETOOL 0
	  MOVE P, @0 P[99]
  
	END SELECT
  END IF

PREFETCH_PART = 0
CAMERA_NOT_BLOCKED = 1
PARK_COMPLETE = 1
MOVING_TO_PARK = 0
R_WAITING = 1
WAIT PARK_COMPLETE = 0
R_WAITING = 0

RETURN
