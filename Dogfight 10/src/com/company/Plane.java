package com.company;

import java.util.ArrayList;
import java.util.HashMap;

abstract class Plane {

    Plane(int health, Bullet bullet, int spd) {
        setInitStatus(health, spd);
        _bullet = bullet;
    }

    /** Set the initial status of the plane. */
    void setInitStatus(int health, int spd) {
        _status.put("health", health);
        _status.put("speed", spd);
        _status.put("power up", 0);
        _status.put("impaired", 0);
        maxHealth = health;
    }


    /** Shooting command of the plane. */
    abstract void shoot();

    /** Reduces the plane's health. */
    abstract void reduceHealth();

    /** Current Status of the Plane, including
     * Health, speed, powerups and if the plane
     * is impaired or not. */
    protected HashMap<String, Integer> _status;

    /** The initial maximum health of the plane.
     * For the purpose of health bars and healing. */
    protected int maxHealth;

    /** The bullet the plane is using. */
    protected Bullet _bullet;


}
