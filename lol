Writing back with: <class 'instruction.Nop'>
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: <class 'instruction.Nop'>
	hazards: []
Fetching: addi 24, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: addi 24, 0, 0
	hazards: []
Fetching: addi 25, 0, 36


Writing back with: <class 'instruction.Nop'>
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: addi 24, 0, 0
	hazards: []
On deck: addi 25, 0, 36
	hazards: []
Fetching: lw 2, 24, 0


Writing back with: <class 'instruction.Nop'>
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: addi 24, 0, 0
	hazards: []
	RS: 0 RT: 24
	instr: addi 24, 0, 0 -- 0,0
Decoding: addi 25, 0, 36
	hazards: [24]
On deck: lw 2, 24, 0
	hazards: [24]
Fetching: lw 3, 24, 36


Writing back with: <class 'instruction.Nop'>
	hazards: [24]
Access memory with: addi 24, 0, 0
	hazards: [24]
Executing: addi 25, 0, 36
	hazards: [24]
	RS: 0 RT: 25
	instr: addi 25, 0, 36 -- 0,36
Decoding: lw 2, 24, 0
	hazards: [24, 25]
On deck: lw 3, 24, 36
	hazards: [24, 25]
Fetching: add 8, 2, 3


Writing back with: addi 24, 0, 0
	hazards: [24, 25]
Access memory with: addi 25, 0, 36
	hazards: [25]
Executing: lw 2, 24, 0
	hazards: [25]
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 0,0
Decoding: lw 3, 24, 36
	hazards: [25, 2]
On deck: add 8, 2, 3
	hazards: [25, 2]
Fetching: sw 8, 24, 72


Writing back with: addi 25, 0, 36
	hazards: [25, 2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 0; result: 1
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 0,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 36; result: 2
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 1,2
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 3
	Forwarded RT val: 3
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 0,3
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 0,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 4,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 4; result: 2
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 4,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 40; result: 4
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 2,4
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 6
	Forwarded RT val: 6
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 4,6
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 4,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 8,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 8; result: 3
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 8,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 44; result: 6
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 3,6
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 9
	Forwarded RT val: 9
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 8,9
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 8,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 12,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 12; result: 4
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 12,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 48; result: 8
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 4,8
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 12
	Forwarded RT val: 12
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 12,12
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 12,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 16,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 16; result: 5
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 16,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 52; result: 10
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 5,10
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 15
	Forwarded RT val: 15
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 16,15
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 16,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 20,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 20; result: 6
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 20,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 56; result: 12
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 6,12
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 18
	Forwarded RT val: 18
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 20,18
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 20,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 24,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 24; result: 12
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 24,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 60; result: 14
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 12,14
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 26
	Forwarded RT val: 26
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 24,26
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 24,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 28,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 28; result: 8
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 28,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 64; result: 16
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 8,16
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 24
	Forwarded RT val: 24
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 28,24
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 28,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = false, move on!
On deck: j 4104
	hazards: [15, 15]
Fetching: addi 2, 0, 0


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: j 4104
	hazards: [15]
On deck: was: addi 2, 0, 0, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15]
Fetching: lw 2, 24, 0


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: j 4104
	hazards: []
Decoding: <class 'instruction.Nop'>
	hazards: []
On deck: lw 2, 24, 0
	hazards: []
Fetching: lw 3, 24, 36


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: j 4104
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: lw 2, 24, 0
	hazards: []
On deck: lw 3, 24, 36
	hazards: []
Fetching: add 8, 2, 3


Writing back with: j 4104
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: lw 2, 24, 0
	hazards: []
	RS: 24 RT: 2
	instr: lw 2, 24, 0 -- 32,0
Decoding: lw 3, 24, 36
	hazards: [2]
On deck: add 8, 2, 3
	hazards: [2]
Fetching: sw 8, 24, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: lw 2, 24, 0
	hazards: [2]
	offset: 32; result: 9
Executing: lw 3, 24, 36
	hazards: [2]
	RS: 24 RT: 3
	instr: lw 3, 24, 36 -- 32,36
Decoding: add 8, 2, 3
	hazards: [2, 3]
	Load-use hazard detected! Inserting bubble.
On deck: was: sw 8, 24, 72, now: add 8, 2, 3 (load use)
	hazards: [2, 3]
Fetching: sw 8, 24, 72


Writing back with: lw 2, 24, 0
	hazards: [2, 3]
Access memory with: lw 3, 24, 36
	hazards: [3]
	offset: 68; result: 18
Executing: <class 'instruction.Nop'>
	hazards: [3]
Decoding: add 8, 2, 3
	hazards: [3]
On deck: sw 8, 24, 72
	hazards: [3]
Fetching: addi 24, 24, 4


Writing back with: lw 3, 24, 36
	hazards: [3]
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: add 8, 2, 3
	hazards: []
	RS: 2 RT: 3
	instr: add 8, 2, 3 -- 9,18
Decoding: sw 8, 24, 72
	hazards: [8]
On deck: addi 24, 24, 4
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: <class 'instruction.Nop'>
	hazards: [8]
Access memory with: add 8, 2, 3
	hazards: [8]
Executing: sw 8, 24, 72
	hazards: [8]
	Hazardous RT found!
	X-X forwarding: RD - 8, value - 27
	Forwarded RT val: 27
	RS: 24 RT: 8
	instr: sw 8, 24, 72 -- 32,27
Decoding: addi 24, 24, 4
	hazards: [8]
On deck: add 15, 0, 0
	hazards: [8]
Fetching: add 15, 0, 0


Writing back with: add 8, 2, 3
	hazards: [8]
Access memory with: sw 8, 24, 72
	hazards: []
Executing: addi 24, 24, 4
	hazards: []
	RS: 24 RT: 24
	instr: addi 24, 24, 4 -- 32,4
Decoding: add 15, 0, 0
	hazards: [24]
On deck: add 15, 0, 0
	hazards: [24]
Fetching: beq 24, 25, 1


Writing back with: sw 8, 24, 72
	hazards: [24]
Access memory with: addi 24, 24, 4
	hazards: [24]
Executing: add 15, 0, 0
	hazards: [24]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: add 15, 0, 0
	hazards: [24, 15]
On deck: beq 24, 25, 1
	hazards: [24, 15]
Fetching: j 4104


Writing back with: addi 24, 24, 4
	hazards: [24, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: add 15, 0, 0
	hazards: [15]
	RS: 0 RT: 0
	instr: add 15, 0, 0 -- 0,0
Decoding: beq 24, 25, 1
	hazards: [15, 15]
	branch condition = true, jump to addr 4148
On deck: was: j 4104, now: <class 'instruction.Nop'> (jump stall)
	hazards: [15, 15]
Fetching: addi 2, 2, 4


Writing back with: add 15, 0, 0
	hazards: [15, 15]
Access memory with: add 15, 0, 0
	hazards: [15]
Executing: beq 24, 25, 1
	hazards: [15]
Decoding: <class 'instruction.Nop'>
	hazards: [15]
On deck: addi 2, 2, 4
	hazards: [15]
Fetching: lw 9, 2, 72


Writing back with: add 15, 0, 0
	hazards: [15]
Access memory with: beq 24, 25, 1
	hazards: []
Executing: <class 'instruction.Nop'>
	hazards: []
Decoding: addi 2, 2, 4
	hazards: []
On deck: lw 9, 2, 72
	hazards: []
Fetching: addi 2, 2, 4


Writing back with: beq 24, 25, 1
	hazards: []
Access memory with: <class 'instruction.Nop'>
	hazards: []
Executing: addi 2, 2, 4
	hazards: []
	RS: 2 RT: 2
	instr: addi 2, 2, 4 -- 9,4
Decoding: lw 9, 2, 72
	hazards: [2]
On deck: addi 2, 2, 4
	hazards: [2]
Fetching: lw 10, 2, 72


Writing back with: <class 'instruction.Nop'>
	hazards: [2]
Access memory with: addi 2, 2, 4
	hazards: [2]
Executing: lw 9, 2, 72
	hazards: [2]
	Hazardous RS found!
	X-X forwarding: RT - 2, value - 13
	Forwarded RS val: 13
	RS: 2 RT: 9
	instr: lw 9, 2, 72 -- 13,72
Decoding: addi 2, 2, 4
	hazards: [2, 9]
On deck: lw 10, 2, 72
	hazards: [2, 9]
Fetching: addi 2, 2, 4


Writing back with: addi 2, 2, 4
	hazards: [2, 9]
Access memory with: lw 9, 2, 72
	hazards: [9]