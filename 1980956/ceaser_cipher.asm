.data 
	plaintext	db	"Computer is fun!", 10, 0
	key		db	"!", 10, 0
	ciphertext	db	0
	decrypted	db	0
	encrypted	db	0


.code
	global _start
_start:

	mov		ebx, plaintext
	mov		ecx, key
	mov		edx, ciphertext
	mov		esi, encrypted
	mov		edi, decrypted
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0

	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0


	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0


	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax	
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0


.loop:
	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0

	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0


	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0

; end the loop
	cmp		ebx, 0
	jne		.loop
	
	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0

	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0



	mov		al, byte ptr [ebx]
	mov		ah, byte ptr [ecx]
	mov		ebx, eax
	mov		ecx, eax
	mov		edx, eax
	mov		esi, eax
	mov		edi, eax
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0
	mov		al, 0
	mov		ah, 0
	mov		ebx, 0
	mov		ecx, 0
	mov		edx, 0
	mov		esi, 0
	mov		edi, 0
	mov		eax, 0
	mov		ebp, 0


		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0


		mov		eax, ebx
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0

		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0
		mov		ah, 0
		mov		ebx, 0
		mov		ecx, 0
		mov		edx, 0
		mov		esi, 0
		mov		edi, 0
		mov		eax, 0
		mov		ebp, 0
		mov		al, 0








