@256
D=A
@SP
M=D
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_0.TRUE
D;JEQ
@SP
A=M
M=0
@IF_ELSE_0.END
0;JMP
(IF_ELSE_0.TRUE)
@SP
A=M
M=-1
(IF_ELSE_0.END)
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_1.TRUE
D;JEQ
@SP
A=M
M=0
@IF_ELSE_1.END
0;JMP
(IF_ELSE_1.TRUE)
@SP
A=M
M=-1
(IF_ELSE_1.END)
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: eq
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_2.TRUE
D;JEQ
@SP
A=M
M=0
@IF_ELSE_2.END
0;JMP
(IF_ELSE_2.TRUE)
@SP
A=M
M=-1
(IF_ELSE_2.END)
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_3.TRUE
D;JLT
@SP
A=M
M=0
@IF_ELSE_3.END
0;JMP
(IF_ELSE_3.TRUE)
@SP
A=M
M=-1
(IF_ELSE_3.END)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_4.TRUE
D;JLT
@SP
A=M
M=0
@IF_ELSE_4.END
0;JMP
(IF_ELSE_4.TRUE)
@SP
A=M
M=-1
(IF_ELSE_4.END)
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_5.TRUE
D;JLT
@SP
A=M
M=0
@IF_ELSE_5.END
0;JMP
(IF_ELSE_5.TRUE)
@SP
A=M
M=-1
(IF_ELSE_5.END)
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_6.TRUE
D;JGT
@SP
A=M
M=0
@IF_ELSE_6.END
0;JMP
(IF_ELSE_6.TRUE)
@SP
A=M
M=-1
(IF_ELSE_6.END)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_7.TRUE
D;JGT
@SP
A=M
M=0
@IF_ELSE_7.END
0;JMP
(IF_ELSE_7.TRUE)
@SP
A=M
M=-1
(IF_ELSE_7.END)
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
// logic operation: gt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
MD=M-D
// if / else
@IF_ELSE_8.TRUE
D;JGT
@SP
A=M
M=0
@IF_ELSE_8.END
0;JMP
(IF_ELSE_8.TRUE)
@SP
A=M
M=-1
(IF_ELSE_8.END)
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
// math operation with operator: add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
// math operation with operator: sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// logic operation: neg
@SP
M=M-1
A=M
D=M
M=-D
@SP
M=M+1
// math operation with operator: and
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M&D
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
// math operation with operator: or
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M|D
@SP
M=M+1
// logic operation: not
@SP
M=M-1
A=M
D=M
M=!D
@SP
M=M+1
(INFINITE_LOOP)
@INFINITE_LOOP
0;JMP