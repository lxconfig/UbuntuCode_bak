// pages/profile/profile.js

// 获取公共的app
var app = getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    phone: "18370850448",
    code: ""
  },
  /**
   * 手机号的双向绑定
   */
  bindPhoneInput: function (e) {
    // console.log(e.detail.value);
    this.setData({
      phone: e.detail.value
    });
  },
  /**
   * 验证码的双向绑定
   */
  bindCodeInput: function (e) {
    this.setData({
      code: e.detail.value
    });
  },
  /**
   * 获取验证码
   */
  onClickCheckCode: function () {
    // 验证手机号格式
    if (this.data.phone.length != 11) {
      wx.showToast({
        title: '手机号格式错误',
        icon: "none"
      });
      return;
    };
    var reg = /^1[3456789]\d{9}$/;
    if (!reg.test(this.data.phone)) {
      wx.showToast({
        title: '手机号格式错误',
        icon: "none"
      });
      return;
    };
    // 验证通过后，再发送请求给后端
    wx.request({
      url: 'http://127.0.0.1:8000/api/message/',
      data: {
        phone: this.data.phone
      },
      dataType: "json",
      method: "GET",
      success: function (res) {
        console.log(res);
      }
    });
  },
  /**
   * 登录或注册
   */
  onClickSubmit: function (e) {
    // e是包含用户信息的结果集
    console.log(e);
    // 给后端发送请求，类似ajax
    wx.request({
      url: 'http://127.0.0.1:8000/api/login/',
      data: {
        phone: this.data.phone,
        code: this.data.code
      },
      method: "POST",
      dataType: "json",
      success: function (res) {
        console.log(res);
        if (res.data.status) {
          app.initUserInfo(res.data.data, e.detail.userInfo);
          // 登录/注册成功返回上一页
          wx.navigateBack({});
        } else {
          wx.showToast({
            title: '登录失败',
            icon: "none"
          })
        }
      },
      fail: function(res) {
        console.log(res);
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})