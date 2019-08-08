.intel_syntax noprefix
.bits 32
	
.global asm1

;asm1(0x255)

asm1:
	push	ebp						;function prologue
	mov	ebp,esp						;function prologue
	cmp	DWORD PTR [ebp+0x8],0xea	
	jg 	part_a	
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x6
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]		;eax = 0x255
	sub	eax,0x3						;eax -= 0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0x126
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]		;eax = 0xcd
	add	eax,0x3						;eax += 0x3
part_d:
	pop	ebp
	ret
