package com.iscas.utils;


/**
 * 设定一个数组，其中的元素都是两位数的随机数，计算这个数组的最大值，最小值，总和，平均值
 */


public class MyArray {
    public static void main(String[] args) {
        int[] arr = new int[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int)(Math.random() * (99 - 10 + 1) + 10);
        }
        // get the max value of the arr
        int maxValue = 0;
        for (int i: arr) {
            if (i > maxValue) {
                maxValue = i;
            }
        }
        int minValue = 0;
        for (int j : arr) {
            if (j < minValue) {
                minValue = j;
            }
        }
        int sumValue = 0;
        for (int i : arr) {
            sumValue += i;
        }
        int average = sumValue / arr.length;
    }
}
