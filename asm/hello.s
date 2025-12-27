        .section __TEXT,__text,regular,pure_instructions
        .globl _main
        // .p2align 4, 0x90

_main:
        // subq    $8, %rsp                # align stack to 16 bytes before call
        leaq    message(%rip), %rdi      # 1st arg to puts: pointer to string
        callq   _puts
        // addq    $8, %rsp

        xorl    %eax, %eax              # return 0 from main
        retq

        .section __TEXT,__cstring,cstring_literals
message:
        .asciz  "Hello, world!"