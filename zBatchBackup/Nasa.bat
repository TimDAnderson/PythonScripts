:: Nasa.bat requires the user designate the longer processed clip on entry
:: If there are spaces then you must include quotes around the processed clip name
:: Examples of acceptable entries
:: Nasa.bat TestClip
:: Nasa.bat "Test Clip"

::The script also assumes all clips are stored in F:\nasa-tEST\


:: Align then measure against Popcorn VCR1
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "Popcorn VCR1" 0 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\Popcorn VCR1_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\Popcorn VCR1_%~1.jnd"




:: Align then measure against Popcorn VCR5
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "Popcorn VCR5" 0 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\Popcorn VCR5_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\Popcorn VCR5_%~1.jnd"




:: Align then measure against Popcorn VCR8
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "Popcorn VCR8" 0 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\Popcorn VCR8_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\Popcorn VCR8_%~1.jnd"




:: Align then measure against QM2 VCR1
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "QM2 VCR1" 0 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\QM2 VCR1_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\QM2 VCR1_%~1.jnd"




:: Align then measure against QM2 VCR8
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "QM2 VCR8" 0 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\QM2 VCR8_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\QM2 VCR8_%~1.jnd"




:: Align then measure against SLS VCR1
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "SLS VCR1" 99 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\SLS VCR1_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\SLS VCR1_%~1.jnd"




:: Align then measure against SLS VCR8
cv reset
cv libraryactivate F:\nasa-tEST\
cv mapa "SLS VCR8" 99 -1 1
cv libraryactivate F:\nasa-tEST\
cv mapb %1 0 -1 1

cv autoalign 1 0 1

sleep 2
cv dmos "F:\NASA-TEST4\DATA FILES\SLS VCR8_%~1.dmos"
sleep 2
cv jnd "F:\NASA-TEST4\DATA FILES\SLS VCR8_%~1.jnd"