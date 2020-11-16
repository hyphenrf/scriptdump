global max
section .text

max:
	mov    eax,edi
	cmp    edi,esi
	cmovl  eax,esi
	ret
