// pages/login/loogin.js
Page({

	/**
	 * 页面的初始数据
	 */
	data: {
		username: "",
		path: "/static/index/default.png",
		localPath: "获取用户位置",
		dataList: [1, 2, 3, 4, 5],
		dataDict: {
			name: "张三",
			age: 18
		}
	},
	fetchInfo: function () {
		// wx.openSetting({});
		var that = this;
		wx.getUserInfo({
		  success: function (res) {
			  console.log(res);
			that.setData({
				username: res.userInfo.nickName,
				path: res.userInfo.avatarUrl
			});
		  },
		  fail: function (res) {
			  console.log(res);
		  }
		});
	},
	getLocalPath: function () {
		var that = this;
		wx.chooseLocation({
		  success: function (res) {
			  console.log(res);
			that.setData({
				localPath: res.address,
			})
		  },
		  fail: function (res) {
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