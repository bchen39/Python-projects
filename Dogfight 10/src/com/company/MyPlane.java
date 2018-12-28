package com.company;

import java.awt.event.KeyAdapter;
import java.util.ArrayList;

class MyPlane extends Plane {


    MyPlane(int health, Bullet bullet, int spd, int pwp) {
       super(health, bullet, spd);
        setPowerUp(pwp);
    }

    /** Set the initial number of powerups the
     * player has. */
    void setPowerUp(int num) {
        for (int i = 0; i < 4; i += 1) {
            _numPowerUps.add(num);
        }
    }

    @Override
    void shoot() {

    }

    @Override
    void reduceHealth() {

    }

    /** The number of each powerups left. */
    private ArrayList<Integer> _numPowerUps;
}
