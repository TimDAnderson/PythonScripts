:top
cv reset
cv libraryactivate F:\4K_10Bit_Patterns
cv videooutput broadcast
cv mapa 4K_Patterns 0 -1 1
cv videoinput broadcast inout 0 0 SDI SDI SDI 0
cv play
cv record F:\4K_10Bit_Patterns\ test 250000 0 0
sleep 4000
cv stop
cv reset
cv seqdelete F:\4K_10Bit_Patterns\ test
goto top