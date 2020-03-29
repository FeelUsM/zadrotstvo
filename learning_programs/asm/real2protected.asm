ORG 100h ; com-программа

start:
; очистка экрана:
        mov     ax, 3
        int     10h
; msg0
        mov dx,msg0
        mov ah,9
        int 21h
; открываем линию A20 (для 32-битной адресации): ; 32-битная адресация видеопамяти
        in      al, 92h
        or      al, 2
        out     92h, al
        
; вычисляем линейный адрес точки входа в защищенный режим
        xor     eax,eax
        mov     ax,cs
        shl     eax, 4
        add     eax, PROTECTED_MODE_ENTRY_POINT
        mov     [ENTRY_OFF],eax
; теперь надо вычислить линейный адрес GDT
        xor     eax,eax
        mov     ax,cs
        shl     eax, 4
        add     ax, GDT
; линейный адрес GDT кладем в заранее подготовленную переменную
        mov     dword [GDTR+2],eax
; msg1
        mov dx,msg1
        mov ah,9
        int 21h

; загрузка регистра GDTR:
        lgdt fword [GDTR]
; msg2
        mov dx,msg2
        mov ah,9
        int 21h
; запрет всех прерываний:
        cli
        in al,70h
        or al,80h
        out 70h,al
; msg1
        mov dx,msg1
        mov ah,9
        int 21h
; переключение в защищенный режим
        mov eax,cr0
        or al, 1
        mov cr0,eax
        
; загрузить новый селектор в регистр CS
        db 66h ; префикс изменения разрядности операнда
        db 0EAh ; опкод команды JMP FAR
        ENTRY_OFF dd PROTECTED_MODE_ENTRY_POINT; 32-битное смещение
        dw 00001000b ; селектор первого дескриптора
; ѓ‹ЋЃЂ‹њЌЂџ ’ЂЃ‹€–Ђ „…‘Љђ€Џ’ЋђЋ‚
GDT:
        NULL_descr  db 8 dup(0)
        CODE_descr  db 0FFh,0FFh,00h,00h, 00h,10011010b,11001111b,00h
        DATA_descr  db 0FFh,0FFh,00h,00h, 00h,10010010b,11001111b,00h
        VIDEO_descr db 0FFh,0FFh,00h,80h, 0Bh,10010010b,01000000b,00h
GDT_size equ $-GDT
label GDTR fword
        dw GDT_size-1; 16-битный лимит GDT
        dd ? ; здесь будет 32-битный линейный адрес GDT

use32 ; далее следует 32-битный код
PROTECTED_MODE_ENTRY_POINT:
; загрузим сегментные регистры требуемыми селекторами
        mov     bx,ds ; номер сегмента кода режима реальных адресов
        
        mov     ax,00010000b ; DATA_descr
        mov     ds, ax
        
        mov     ax,00011000b ; VIDEO_descr
        mov     es, ax
        
; вывод на экран:
        xor     esi,esi
        mov     si,bx
        shl     esi,4
        add     esi, message
        xor     edi,edi
        mov     ecx,18
        rep movsb ; ds:[esi]->es:[edi]
        jmp     $
message:
         db '1',35h,'2',35h,'3',35h,'4',35h,'5',35h,'6',35h,'7',35h,'8',35h,'9',35h
msg0: db 'msg0',0Dh,0Ah,'$'
msg1: db 'msg1',0Dh,0Ah,'$'
msg2: db 'msg2',0Dh,0Ah,'$'

