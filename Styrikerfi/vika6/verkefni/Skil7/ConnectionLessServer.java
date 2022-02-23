//package ch3Processes.connectionLessSocket;
import java.net.*;
import java.io.*;

public class ConnectionLessServer {
  public static void main(String args[]) {
    DatagramSocket aSocket = null;
    
    try {
      aSocket = new DatagramSocket(6789); // create socket at agreed port
      byte[] buffer = new byte[1000];
      int count = 1;
      while (true) {
        System.out.println("Listening to requests!");
        DatagramPacket request = new DatagramPacket(buffer, buffer.length);
        String skilabod = String.valueOf(count);
        skilabod = skilabod + "    ";
        buffer = skilabod.getBytes();
        aSocket.receive(request);
        DatagramPacket reply = new DatagramPacket(buffer, request.getLength(), request.getAddress(), request.getPort());
        count++;
        System.out.println("Sending message to client: " + skilabod);
        aSocket.send(reply);
      }
    } catch (SocketException e) {
      System.out.println("Socket: " + e.getMessage());
    } catch (IOException e) {
      System.out.println("IO: " + e.getMessage());
    } finally {
      if (aSocket != null)
        System.out.println("Closing socket!");
        aSocket.close();
    }
  }
}