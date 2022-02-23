1. Start server using (adjust classpath parameter -cp to let it point to the directory that contains the ch3process sub directories that contain the *.class files)
java -cp /home/helmuth/workspace/OperatingSystems/bin/ ch3Processes.connectionLessSocket.ConnectionLessServer

2. Start on same machine client using (adjust classpath)
java -cp /home/helmuth/workspace/OperatingSystems/bin/ ch3Processes.connectionLessSocket.ConnectionLessClient Hello localhost

Or (without packages and adjustable path) from within the shell command line (CLI)

1. Start server using
java ConnectionLessServer

2. Start on same machine client
java ConnectionLessClient Hello localhost
