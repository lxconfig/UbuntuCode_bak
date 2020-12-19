package com.iscas.utils;

public class TemplateTest {
    public static void main(String[] args) {
        Template template = new SubTemplate();
        template.spendTime();
    }

}


abstract class Template {
    public void spendTime() {
        // 计算某段代码花费的时间
        long start = System.currentTimeMillis();
        this.code();
        long end = System.currentTimeMillis();
        System.out.println("花费时间: " + (end - start));
    }
    public abstract void code();
}


class SubTemplate extends Template {
    @Override
    public void code() {
        // 求1000以内的质数
        for (int i = 2; i < 1000; i++) {
            boolean Flag = true;
            for (int j = 2; j < Math.sqrt(i); j++) {
                if (i  % j == 0) {
                    Flag = false;
                    break;
                }
            }
            if (Flag) {
                System.out.println(i);
            }
        }
    }
}