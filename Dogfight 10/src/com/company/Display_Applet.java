package com.company;

import javax.swing.JApplet;
import java.awt.*;

public class Display_Applet extends JApplet {
    private Game game = new Game();

    public void init() {
        setLayout(new BorderLayout());
        add(game);
    }

    public void start() {
        game.start();
    }

    public void stop() {
        game.stop();
    }
}
