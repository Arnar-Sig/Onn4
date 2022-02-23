1. Start server using
java ConnectionOrientedServer

2. Start on same machine client in multiple terminals 
java ConnectionOrientedClient 45 localhost

(see picture "skjaskot af keyrslu.png" for 3 clients asking for calculations at the same time)





Assignment 8 Part 3:
a) kveikt á server:
   			Local Address		 Foreign address
   tcp6       0      0 [::]:7896               [::]:*                  LISTEN     

   
   kveikt á server og með 4 clients:
   			Local Address		 Foreign address
   tcp6       0      0 [::]:7896               [::]:*                  LISTEN
   tcp6       0      0 127.0.0.1:60800         127.0.0.1:7896          ESTABLISHED
   tcp6       0      0 127.0.0.1:7896          127.0.0.1:60802         TIME_WAIT  
   tcp6       0      0 127.0.0.1:7896          127.0.0.1:60798         ESTABLISHED
   tcp6       0      0 127.0.0.1:60804         127.0.0.1:7896          ESTABLISHED
   tcp6       0      0 127.0.0.1:7896          127.0.0.1:60800         ESTABLISHED
   tcp6       0      0 127.0.0.1:60798         127.0.0.1:7896          ESTABLISHED
   tcp6       0      0 127.0.0.1:7896          127.0.0.1:60804         ESTABLISHED


Assignment 8 Part 4:
Local address er serverinn og foreign address væri þá clientinn eins og sést þegar aðeins er kveikt á servernum, þá birtist portið í local address. Svo þegar ég setti 4 clienta af stað birtast tengingarnar við serverinn þarna, og allir nema 1 virðist hafa verið established á þessum tíma, en hann fékk state-ið TIME_WAIT sem þýðir að sá client var að bíða eftir staðfestingu við hostinn áður en hann gat haldið áfram.
