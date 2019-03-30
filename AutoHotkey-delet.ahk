^BS::
BreakLoop = 0

Loop,
	if (Breakloop = 1)
		break
	else
	{
    		send, {Up}
    		send, ^a
    		send, {BS}
   		send, {Enter}
    		send, {Enter}
    		sleep, 300
	}
return

ESC::
	BreakLoop = 1
return