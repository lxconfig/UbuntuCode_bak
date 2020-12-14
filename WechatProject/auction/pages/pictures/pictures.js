// pages/pictures/pictures.js
Page({

	/**
	 * 页面的初始数据
	 */
	data: {
		path: ["/static/index/default.png", "/static/index/ic_menu_choice_nor.png"]
	},

	UploadPic: function () {
		var that = this;
		wx.chooseImage({
		  count: 9,
		  sizeType: ["original", "compressed"],
		  sourceType: ["album", "camera"],
		  success: function (res) {
			console.log(res);
			// 直接替换原来的图片
			// that.setData({
			// 	path: res.tempFilePaths
			// });
			//  追加图片 用concat合并两个列表，返回一个新的大列表
			that.setData({
				path: that.data.path.concat(res.tempFilePaths)
			});
		  },
		  fail: function (res) {
			  console.log(res);
		  },
		  complete: function (res) {
			  console.log("complete");
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