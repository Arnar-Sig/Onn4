1. Start programm using (adjust classpath parameter -cp to let it point to the directory that contains the .class files):

java -cp /home/helmut/workspace/Assignment11/bin/ Assignment11 100

2. Run your program: is the printed value of in the expected value? How would you see
that a race condition occurred?

3. What command line parameter value demonstrates typically at
 each run the race condition on your computer?



Lausn:

2. Gildi� sem ma�ur b�st vi� a� f� er tv�falt �a� sem sett er inn, �.a. ef sett er inn 200 f�r hver �r��ur a� b�ti vi� 1 tv�hundru� sinnum og �v� v�ri heildin 400. Ef talan er minni en �a� hefur race-condition �tt s�r sta�.


3. Svo vir�ist sem a� � bilinu 5000-5500 byrjar race-conditioni� a� koma fyrir �v� ef kalla� er � forriti� me� 5500 kemur stundum sk�kk ni�ursta�a, �ar a� segja � sta�inn fyrir a� b��ir �r��irnir telja upp � 5500 og b�ta vi� � sameiginlegu breytuna � sitthvoru lagi (sem yr�i 11000) �� fara �eir a� reyna a� vinna me� breytuna � sama t�ma og �ar me� n� �eir ekki upp � 11000. �etta gerist �� ekki alltaf en ef kalla� er � me� 6000 gerist �a� st��ugt svo t�fratalan er �v� � milli 5500 og 6000.

