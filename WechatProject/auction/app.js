App({

globalData: {
	userInfo: null
},
initUserInfo: function(res, localInfo) {
	var info = {
		token: res.token,
		phone: res.phone,
		nickName: localInfo.nickName,
		avatarUrl: localInfo.avatarUrl
	}
	// 在全局位置中记录用户已经登录
	this.globalData.userInfo = info
	// 在storage中记录用户已经登录
	wx.setStorageSync('userInfo', info);
},
  /**
   * 注销登录
   */
delUserInfo: function() {
	this.globalData.userInfo = null;  // 全局变量中删掉信息
	wx.removeStorageSync('userInfo');  // storage中删掉信息
},
  /**
   * 当小程序初始化完成时，会触发 onLaunch（全局只触发一次）
   */
  onLaunch: function () {
	var userInfo = wx.getStorageSync('userInfo');
	if (userInfo) {
		this.globalData.userInfo = userInfo;
	}
  },

  /**
   * 当小程序启动，或从后台进入前台显示，会触发 onShow
   */
  onShow: function (options) {
	
  },

  /**
   * 当小程序从前台进入后台，会触发 onHide
   */
  onHide: function () {
	
  },

  /**
   * 当小程序发生脚本错误，或者 api 调用失败时，会触发 onError 并带上错误信息
   */
  onError: function (msg) {
	
  }
})
