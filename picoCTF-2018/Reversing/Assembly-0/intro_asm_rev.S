.intel_syntax noprefix
.bits 32
	
.global asm0

;asm0(0xaa,0xf2)
asm0:
	push	ebp						;Funtion Prologue
	mov	ebp,esp						;Funtion Prologue
	mov	eax,DWORD PTR [ebp+0x8]		;eax = 0xaa
	mov	ebx,DWORD PTR [ebp+0xc]		;ebx = 0xf2
	mov	eax,ebx						;eax = ebx = 0xf2
	mov	esp,ebp
	pop	ebp	
	ret