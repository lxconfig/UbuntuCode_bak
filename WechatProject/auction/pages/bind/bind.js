// pages/bind/bind.js
Page({

	/**
	 * 页面的初始数据
	 */
	data: {
		message: "消息1",
		name: "张三",
		username: "",
		path: "/static/index/default.png"
	},
	edit: function () {
		// 获取数据
		console.log(this.data.message);
		// 修改数据（仅修改后端）
		this.data.message = "消息2";
		// 前后端都修改
		this.setData({
			message: "消息3",
			name: "李四"
		});
	},
	GetUserInfo: function () {
		var that = this;
		wx.getUserInfo({
		  success: function (res) {
			  console.log("success", res);
			  // 这里用this指的是getUserInfo函数而不是全局的这个字典
			  // 可以在外部先获取到this
			  that.setData({
				  username: res.userInfo.nickName,
				  path: res.userInfo.avatarUrl
			  });
		  },
		  fail: function (res) {
			console.log("fail", res);
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