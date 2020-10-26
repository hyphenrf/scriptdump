void main()
{
	string msg = "Hello World!\n";
	int    len = cast(int) msg.length;

	print(msg, len);
}

void print(string msg, int len)
{
	asm {
		mov  EDX,  len;  //message length -- directly from d variables!
		mov  ECX,  msg;  //message to write
		mov  EBX,  1;    //file descriptor (stdout)
		mov  EAX,  4;    //system call number (sys_write)

		syscall;
	}
}
