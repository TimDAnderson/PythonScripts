:: This will run PSNR JND and DMOS on clips that are in the same library::

cv libraryactivate F:\Library_name_here\

cv mapa Source_clip 1 -1 1
cv mapb ATSC 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\ATSC.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\ATSC.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\ATSC.jnd

cv mapa Source_clip 1 -1 1
cv mapb AT&T 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\AT&T.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\AT&T.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\AT&T.jnd

cv mapa Source_clip 1 -1 1
cv mapb Comcast 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\Comcast.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\Comcast.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\Comcast.jnd


cv mapa Source_clip 1 -1 1
cv mapb DirecTV 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\DirecTV.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\DirecTV.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\DirecTV.jnd

cv mapa Source_clip 1 -1 1
cv mapb Dish 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\Dish.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\Dish.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\Dish.jnd

cv mapa Source_clip 1 -1 1
cv mapb Amazon 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\Amazon.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\Amazon.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\Amazon.jnd

cv mapa Source_clip 1 -1 1
cv mapb AppleTV 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\AppleTV.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\AppleTV.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\AppleTV.jnd

cv mapa Source_clip 1 -1 1
cv mapb Roku 1 -1 1
cv autoalign 1 0
cv spatialalign
cv metricwindow 0 0 1920 960
cv psnr C:\Users\user\Desktop\Metric_Results\Roku.psnr
cv dmos C:\Users\user\Desktop\Metric_Results\Roku.dmos
cv jnd C:\Users\user\Desktop\Metric_Results\Roku.jnd
