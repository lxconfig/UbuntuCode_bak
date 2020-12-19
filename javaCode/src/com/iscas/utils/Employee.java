package com.iscas.utils;

/**
 * 定义一个抽象类及抽象方法
 */

public abstract class Employee {
    private String name;
    private int id;
    private double salary;

    public Employee() {}
    public Employee(String name, int id, double salary) {
        this.name = name;
        this.id = id;
        this.salary = salary;
    }

    // 定义抽象方法work
    public abstract void work();
}


class Manager extends Employee {

    // 必须重写抽象方法
    @Override
    public void work() {
        System.out.println("manager: 打工人!");
    }
}


