// pages/telephone/telephone.js
Page({

	/**
	 * 页面的初始数据
	 */
	data: {
		phone: "",
		code: ""
	},
	bindPhone: function (e) {
		// console.log(e);
		this.setData({
			phone: e.detail.value
		})
	},
	bindCode: function (e) {
		// console.log(e);
		this.setData({
			code: e.detail.value
		})
	},
	/**
	 * 向后端发请求，获取短信验证码
	 */
	Message: function () {
		// 手机号长度限制
		if (this.data.phone.length < 11 ) {
			wx.showToast({
			  title:  '手机号格式错误',
			  icon: "none"
			})
		return ;
		};
		// 手机号格式限制
		var reg = /^1([3|4|5|6|7|8|9])\d{9}$/;
		if (!reg.test(this.data.phone)) {
			wx.showToast({
				title:  '手机号格式错误',
				icon: "none"
			  })
			  return;
		};
		// 否则可以发请求给后端
		wx.request({
			url: 'http://127.0.0.1:8000/api/message/',
			data: {
				phone: this.data.phone,
			},
			method: "GET",
			dataType: "json",
			success: function (res) {
				console.log(res);
			},
		})
	},

	/**
	 * 请求登录
	 */
	login: function () {
		// 先做手机号和验证码的校验
		if (this.data.phone.length < 11) {
			wx.showToast({
			  title: '手机号格式错误',
			  icon: "none"
			});
			return;
		};
		if (this.data.code.length < 4) {
			wx.showToast({
			  title: '验证码格式错误',
			  icon: "none"
			});
			return;
		};
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
			},
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