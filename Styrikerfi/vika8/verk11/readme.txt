1. Start programm using (adjust classpath parameter -cp to let it point to the directory that contains the .class files):

java -cp /home/helmut/workspace/Assignment11/bin/ Assignment11 100

2. Run your program: is the printed value of in the expected value? How would you see
that a race condition occurred?

3. What command line parameter value demonstrates typically at
 each run the race condition on your computer?



Lausn:

2. Gildið sem maður býst við að fá er tvöfalt það sem sett er inn, þ.a. ef sett er inn 200 fær hver þráður að bæti við 1 tvöhundruð sinnum og því væri heildin 400. Ef talan er minni en það hefur race-condition átt sér stað.


3. Svo virðist sem að á bilinu 5000-5500 byrjar race-conditionið að koma fyrir því ef kallað er á forritið með 5500 kemur stundum skökk niðurstaða, þar að segja í staðinn fyrir að báðir þráðirnir telja upp í 5500 og bæta við í sameiginlegu breytuna í sitthvoru lagi (sem yrði 11000) þá fara þeir að reyna að vinna með breytuna á sama tíma og þar með ná þeir ekki upp í 11000. Þetta gerist þó ekki alltaf en ef kallað er á með 6000 gerist það stöðugt svo töfratalan er því á milli 5500 og 6000.

