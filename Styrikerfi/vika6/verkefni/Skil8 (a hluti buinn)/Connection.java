//package ch3Processes.connectionOrientedSocket;
import java.net.*;
import java.io.*;
class Connection {
  DataInputStream in;
  DataOutputStream out;
  Socket clientSocket;
  public Connection(Socket aClientSocket) {
    try {
      clientSocket = aClientSocket;
      in = new DataInputStream(clientSocket.getInputStream());
      out = new DataOutputStream(clientSocket.getOutputStream());
      handleRequest();
    } catch (IOException e) { System.out.println("Connection:" + e.getMessage()); }
  }

  public int fibo(int n){
    if(n <= 1){
      return n;
    }
    else{
      return (fibo(n-1) + fibo(n-2));
    }
  }

  public void handleRequest() {
    try { //an echo server
      String data = in.readUTF(); // read a line of data from the stream
      int dataFibo = fibo(Integer.valueOf(data));
      out.writeUTF(String.valueOf(dataFibo));
    } catch (EOFException e) { System.out.println("EOF:" + e.getMessage());
    } catch (IOException e) { System.out.println("readline:" + e.getMessage());
    } finally {
      try {
        clientSocket.close();
      } catch (IOException e) {/* close failed */
      }
    }
  }
}
