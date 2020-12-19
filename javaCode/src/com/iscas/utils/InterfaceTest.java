package com.iscas.utils;

public class InterfaceTest {
}



interface Flyable {
    // 默认定义的都是全局变量 public static final
    int ID = 1;
    // 默认定义的都是抽象方法 public abstract void
    void fly();
}

interface Attack {
    void attack();
}

class Bird implements Flyable {
    // 要么实现定义的抽象方法，要么定义为抽象类
    @Override
    public void fly() {

    }
}

class Bullet implements Attack, Flyable {
    // 多实现接口，必须把抽象方法都实现
    @Override
    public void fly() {

    }

    @Override
    public void attack() {

    }
}