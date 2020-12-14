EcommerceStore = artifacts.require("./EcommerceStore.sol");
module.exports = function() {
    amt_1 = web3.utils.toWei("1", "ether");
    current_time = Math.round(new Date() / 1000);
    // 增加商品
    EcommerceStore.deployed().then(function (i) {i.addProductToStore('iphone 5', 'Cell Phones & Accessories', 'QmPmv1Wc5Yn1798jzPPFbXLZyp7w73MTCK7qCsvvDNKHYX', 'Qmdat555krbVsBXYnRuDPC7HFZ47RPno12ekintFzCdM4m', current_time, current_time + 200, amt_1, 0).then(function (f) {console.log(f)})});
    EcommerceStore.deployed().then(function (i) {i.addProductToStore('iphone 5C', 'Cell Phones & Accessories', 'QmRW52ShbaALSrAEJcw8aVZXPx86A4zYnjroa4L3AuzUPX', 'QmPEtJ1dUReVHJf7TeZNs5ZLiQyNBQraegiCQ7npGdyTaw', current_time, current_time + 1200, (2*amt_1).toString(), 1).then(function (f) {console.log(f)})});
    EcommerceStore.deployed().then(function (i) {i.addProductToStore('iphone 6', 'Cell Phones & Accessories', 'QmZ3cNfJrvgxdvH4qCRRGN14aSh9ffyQYKjFbrfU2bvJPg', 'QmWt2adzgtNLd7WhueyLETogjj2zLaU7uD77EZd1Y57DT1', current_time, current_time + 400, (3*amt_1).toString(), 0).then(function (f) {console.log(f)})});
    EcommerceStore.deployed().then(function (i) {i.addProductToStore('iphone 7', 'Cell Phones & Accessories', 'QmULU8xzCAj7BqCniNgETbcD29eWWSKE2yHR2cXyyuug5o', 'QmQx84SwuzguD28mLbsiop1mzRbbMxpMUGFLrxiuW8cg8D', current_time, current_time + 300, amt_1, 1).then(function (f) {console.log(f)})});
    EcommerceStore.deployed().then(function (i) {i.addProductToStore('iphone X', 'Cell Phones & Accessories', 'QmdnAED7Gtiuwfd7FMRUsMD4DjdbKvLjokdvrYB4HzJTyR', 'QmT1RHaJBVarohgZ6pJVWkaXRr7NoTPLcBKWtVSXwqSU6Z', current_time, current_time + 100, (3*amt_1).toString(), 1).then(function (f) {console.log(f)})});
    EcommerceStore.deployed().then(function(i) {i.productIndex.call().then(function(f){console.log(f)})});
}





// // 通过异步的方式拿到所有的账号信息
// web3.eth.getAccounts().then(function (acc) {accounts = acc});

// // 获取商品信息
// EcommerceStore.deployed().then(function (i) {i.getProduct.call(5).then(function (f) {console.log(f)})});

// // A出价的哈希值
// sealedBid = web3.utils.sha3((2 * amt_1) + "secret1").toString();

// // A竞价
// EcommerceStore.deployed().then(function (i) {i.bid(5, sealedBid, {value: 3 * amt_1,from: accounts[0]}).then(function (f) {console.log(f)})});

// // B出价的哈希
// sealedBid = web3.utils.sha3((3 * amt_1) + "secret2").toString();

// // B竞价
// EcommerceStore.deployed().then(function (i) {i.bid(5, sealedBid, {value: 4 * amt_1,from: accounts[1]}).then(function (f) {console.log(f)})});

// // A揭示竞价
// EcommerceStore.deployed().then(function (i) {i.revealBid(5, (2 * amt_1).toString(), 'secret1', {from: accounts[0]}).then(function (f) {console.log(f)})});

// // B揭示竞价
// EcommerceStore.deployed().then(function (i) {i.revealBid(5, (3 * amt_1).toString(), 'secret2', {from: accounts[1]}).then(function (f) {console.log(f)})});

// // 查询商品1的竞拍获胜者信息
// EcommerceStore.deployed().then(function (i) {i.highestBidderInfo.call(5).then(function (f) {console.log(f)})});