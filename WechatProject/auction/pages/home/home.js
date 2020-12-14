// pages/home/home.js

var app = getApp();

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userInfo: null
  },

  /**
   * 生命周期函数--监听页面加载(第一次打开时会执行)
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成（第一次打开时会执行）
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    // 从stora中取值，该值永久保存在本地
    var userInfo = wx.getStorageSync('userInfo');
    this.setData({
      // 从全局的app中取值，缺点在于重启小程序该值就不在了
      // phone: app.globalData.phone
      userInfo: userInfo
    })
  },

  /**
   * 注销登录
   */
  onClickLogout: function() {
    app.delUserInfo();
    this.setData({
      userInfo: null
    })
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