package GUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Server_GUI {
    public static void main(String[] args) {
        new ManagerLogin();
    }
}

class ManagerLogin extends JFrame implements ActionListener, KeyListener {
    // 로그인 창
    public ManagerLogin() {

    }
    public void actionPerformed(ActionEvent e) {
        // 접속 버튼을 누르면 작동이 됩니다.
    }

    public void keyPressed(KeyEvent e) {

    }

    public void keyTyped(KeyEvent e) { // 불필요
    }
    public void keyReleased(KeyEvent e) { // 불필요

    }
}

class Server_ChatGUI extends JFrame implements ActionListener, KeyListener {
    // 서버용 채팅창

    public Server_ChatGUI(int port) {

    }

    public void actionPerformed(ActionEvent e) { // 전송 버튼을 누르고, 입력값이 1이상일때만 전송되도록 합니다.

    }

    public void keyPressed(KeyEvent e) {

    }

    public void AppendMessage(String Massage) {

    }

    public void keyTyped(KeyEvent e) {

    }

    public void keyReleased(KeyEvent e) {

    }


}