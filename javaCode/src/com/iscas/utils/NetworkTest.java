package com.iscas.utils;

/**
 * 接口的使用：代理模式
 */

public class NetworkTest {
    public static void main(String[] args) {
        Server server = new Server();
        ProxyServer proxyServer = new ProxyServer(server);
        proxyServer.check();
    }
}

interface Network {
    void browse();
}

// 被代理类
class Server implements Network {

    @Override
    public void browse() {
        System.out.println("服务器开始工作....");
    }
}

// 代理类
class ProxyServer implements Network {
    private Network work;
    public ProxyServer(Network work) {
        this.work = work;
    }
    public void check() {
        System.out.println("工作前的检查....");
        this.browse();
    }
    @Override
    public void browse() {
        System.out.println("代理服务器开始工作....");
    }
}