package com.company;

import java.awt.*;
import java.awt.image.BufferStrategy;

public class Game extends Canvas implements Runnable {


    /** Width and height of the game board. */
    public static final int WIDTH = 800, HEIGHT = WIDTH / 12 * 9;

    /** Difficulty of the game. Damage, health etc.
     * change according to this number.*/
    public int difficulty;

    /** The FPS of the game. */
    public int FPS;

    /** The thread of the game. */
    private Thread thread;

    /** Determine if the game is running. */
    private boolean running = false;

    /** Game class initialization. */
    public Game() {
        new Window(WIDTH, HEIGHT, "Dogfight 10", this);
    }

    /** Start the game. */
    public synchronized void start() {
        if (running) {
            return;
        }
        thread = new Thread(this);
        thread.start();
        running = true;
        run();
    }

    public synchronized void stop() {
        if (!running) {
            return;
        }
        try {
            thread.join();
            running = false;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        long timer = System.currentTimeMillis();
        long lastLoopTime = System.nanoTime();
        final int TARGET_FPS = 60;
        final long OPTIMAL_TIME = 1000000000 / TARGET_FPS;
        int frames = 0;



        while (running) {
            long now = System.nanoTime();
            long updateLength = now - lastLoopTime;
            lastLoopTime = now;
            double delta = updateLength / ((double) OPTIMAL_TIME);

            while (delta >= 1) {
                tick();
                delta--;
            }
            if (running) {
                render();
            }
            frames++;

            if (System.currentTimeMillis() - timer > 1000) {
                timer += 1000;
                FPS = frames;
                System.out.println("FPS: "+ FPS);
                frames = 0;
            }

            try {
                thread.sleep(((lastLoopTime - System.nanoTime()) + OPTIMAL_TIME) / 1000);
            } catch (Exception e) {

            }
            System.out.println("Somebody once told me the world is gonna roll me I aint the sharpest tool in the shed.");
            System.out.println("Hey now youre an all star.");
        }
    }

    private void tick() {

    }

    private void render() {
        BufferStrategy bs = this.getBufferStrategy();
        if (bs == null) {
            this.createBufferStrategy(3);
            return;
        }

        Graphics g = bs.getDrawGraphics();

        g.setColor(Color.GRAY);
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.dispose();
        bs.show();
    }

    public static void main(String[] args) {
        new Game();
    }
}
