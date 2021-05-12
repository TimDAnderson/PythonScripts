cv stop
cv pause
cv enablepixval 1
cv pause
set /a x=0
cv setpixvalxy %x% 960
sleep 1
cv getpixval 0 > tmp.txt
:top
if %x% lss 3839 (
	echo %x%
	set /a x+=1
	cv setpixvalxy %x% 960
	cv getpixval 0 >> tmp.txt
	goto :top
	)
grep PixVals tmp.txt > output.txt