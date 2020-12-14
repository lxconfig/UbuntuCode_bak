import Web3 from "web3";
var contract = require("@truffle/contract");
import ecommerce_store_artifacts from "../../build/contracts/EcommerceStore.json";

var EcommerceStore = contract(ecommerce_store_artifacts);
var ipfsAPI = require("ipfs-http-client");
var ipfs = ipfsAPI({
    host: "localhost",
    port: "5001",
    protocol: "http"
});
// window.accounts = [];
// web3.eth.getAccounts().then(function(acc){ window.accounts = acc })

window.App = {
    start: function () {
        var self = this;
        EcommerceStore.setProvider(web3.currentProvider);
        renderStore();
        // 获取上传的图片二进制信息，转换为buffer
        var reader;
        $("#product-image").change(function (event) {
            const file = event.target.files[0];
            reader = new window.FileReader();
            reader.readAsArrayBuffer(file);
        });

        // 获取前端表单中的数据，转换为JSON对象，保存在decodedParams中
        $("#add-item-to-store").submit(function (event) {
            const req = $("#add-item-to-store").serialize();
            let params = JSON.parse('{"' + req.replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}');
            let decodedParams = {}
            Object.keys(params).forEach(function (v) {
                decodedParams[v] = decodeURIComponent(decodeURI(params[v]));
            });
            saveProduct(reader, decodedParams);
            event.preventDefault();
        });

        // 从url中获取商品ID
        if ($("#product-details").length > 0) {
            let productId = new URLSearchParams(window.location.search).get('id');
            $("#revealing, #bidding").hide();
            renderProductDetails(productId);
        }

        // 提供一个出价
        $("#bidding").submit(event => {
            $("#msg").hide();
            let amount = $("#bid-amount").val(); // 实际的出价
            let sendAmount = $("#bid-send-amount").val();  // 保证金
            let secretText = $("#secret-text").val();  // 秘钥
            let productId = $("#product-id").val();
            let sealedBid = web3js.utils.keccak256(web3js.utils.toWei(amount, 'ether').toString() + secretText);  // 出价与秘钥的哈希值
            EcommerceStore.deployed().then(i => {
                i.bid(parseInt(productId), sealedBid, {from: accounts[0], value: web3js.utils.toWei(sendAmount, "ether")}).then(function(res) {
                    $("#msg").html("Your bid has been successfully submitted!");
                    $("#msg").show();
                });
            });
            event.preventDefault();
        });

        // 揭示一个报价
        $("#revealing").submit(event => {
            $("#msg").hide();
            let amount = $("#actual-amount").val();
            let secretText = $("#reveal-secret-text").val();
            let productId = $("#product-id").val();
            EcommerceStore.deployed().then(i => {
                i.revealBid(parseInt(productId), web3js.utils.toWei(amount,  'ether'), secretText, {from: accounts[0]}).then(function(res) {
                    $("#msg").show();
                    $("#msg").html("Your bid has been successfully revealed!");
                });
            });
            event.preventDefault();
        })
    },
};

// 保存产品信息
function saveProduct(reader, decodedParams) {
    let imageId, descId;
    saveImageOnIpfs(reader).then(function (id) {
        imageId = id;
        saveTextBlobOnIpfs(decodedParams["product-description"]).then(function (id) {
            descId = id;
            saveProductToBlockchain(decodedParams, imageId, descId);
        })
    })
};

// 调用ipfs的API，获取图像信息的哈希值
function saveImageOnIpfs(reader) {
    return new Promise(function (resolve, reject) {
        const buffer = Buffer.from(reader.result);
        ipfs.add(buffer)
            .then((response) => {
                console.log(response)
                resolve(response["path"]);
            }).catch((err) => {
                console.log(err)
                reject(err);
            })
    })
}

// 调用ipfs的API，获取描述信息的哈希值
function saveTextBlobOnIpfs(blob) {
    return new Promise(function (resolve, reject) {
        const descBuffer = Buffer.from(blob, 'utf-8');
        ipfs.add(descBuffer)
            .then((response) => {
                console.log(response)
                resolve(response["path"]);
            }).catch((err) => {
                console.error(err)
                reject(err);
            })
    })
}

// 调用智能合约函数，保存产品信息至区块链上
function saveProductToBlockchain(params, imageId, descId) {
    console.log(params);
    let auctionStartTime = Date.parse(params["product-auction-start"]) / 1000;
    let auctionEndTime = auctionStartTime + parseInt(params["product-auction-end"]) * 24 * 60 * 60

    EcommerceStore.deployed().then(function(i) {
        i.addProductToStore(params["product-name"], params["product-category"], imageId, descId, auctionStartTime,
       auctionEndTime, web3js.utils.toWei(params["product-price"], 'ether'), parseInt(params["product-condition"]), {from: accounts[0], gas: 440000}).then(function(f) {
            console.log(f);
            $("#msg").show();
            $("#msg").html("Your product was successfully added to your store!");
        })
    });
};

// 渲染商品详情页面
function renderProductDetails(productId) {
    EcommerceStore.deployed().then(function (i) {
        i.getProduct.call(productId).then(function (p) {
            let content = "";
            // ipfs.cat(p[4]).then(file => {
            //     content = file.toString();
            //     $("#product-desc").append("<div>" + content + "</div>");
            // });
            // ipfs.cat().then()暂时无法使用,只能写死
            $("#product-desc").append("<div>" + "cell phone & smart phone" + "</div>");

            $("#product-image").append("<img src='http://localhost:9001/ipfs/" + p[3] + "' width='250px' />");
            $("#product-price").html(displayPrice(p[7]));
            $("#product-name").html(p[1]);
            $("#product-auction-end").html(displayEndHours(p[6]));
            $("#product-id").val(p[0]);
            let currentTime = getCurrentTimeInSeconds();
            console.log(currentTime < p[6])
            if (currentTime < p[6]) {
                $("#bidding").show();
            } else if (currentTime - (60) < p[6]) {
                console.log("xxxx");
                $("#revealing").show();
            }
        })
    })
}

// 获取当前时间戳
function getCurrentTimeInSeconds() {
    return Math.round(new Date() / 1000);
}

// 将起拍价转换为ether
function displayPrice(amt) {
    return web3js.utils.fromWei(amt, 'ether') + 'ETH';
}

// 显示剩余拍卖时间
function displayEndHours(seconds) {
    let current_time = getCurrentTimeInSeconds()
    let remaining_seconds = seconds - current_time;

    if (remaining_seconds <= 0) {
        return "Auction has ended";
    }

    let days = Math.trunc(remaining_seconds / (24 * 60 * 60));
    remaining_seconds -= days * 24 * 60 * 60;

    let hours = Math.trunc(remaining_seconds / (60 * 60));
    remaining_seconds -= hours * 60 * 60;

    let minutes = Math.trunc(remaining_seconds / 60);
    remaining_seconds -= minutes * 60;

    if (days > 0) {
        return "Auction ends in " + days + " days, " + hours + ", hours, " + minutes + " minutes";
    } else if (hours > 0) {
        return "Auction ends in " + hours + " hours, " + minutes + " minutes ";
    } else if (minutes > 0) {
        return "Auction ends in " + minutes + " minutes ";
    } else {
        return "Auction ends in " + remaining_seconds + " seconds";
    }
}

function renderStore() {
    EcommerceStore.deployed().then(function (i) {
        i.getProduct.call(1).then(function (product) {
            $("#product-list").append(bulidProduct(product));
        });
        i.getProduct.call(2).then(function (product) {
            $("#product-list").append(bulidProduct(product));
        });
    })
}

function bulidProduct(product) {
    let node = $("<div />");
    node.addClass("col-sm-3 text-center col-margin-bottom-1");
    node.append("<a href='product.html?id=" + product[0] + "'><img src='http://localhost:9001/ipfs/" + product[3] + "' width='150px' /></a>")
    node.append("<div>" + product[1] + "</div>");
    node.append("<div>" + product[2] + "</div>");
    node.append("<div>" + product[5] + "</div>");
    node.append("<div>" + product[6] + "</div>");
    node.append("<div>Ether " + product[7] + "</div>");
    return node;
}

window.addEventListener("load", function () {
    // if (typeof Web3 !== undefined) {
    //     window.web3 = new Web3(web3.currentProvider);
    // } else {
    //     window.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
    // }
    // App.start();
    var web3Provider;
    if (window.ethereum) {
        web3Provider = window.ethereum;
        try {
            // 请求用户授权
            window.ethereum.enable();
        } catch (error) {
            console.error("User denied account access");
        }
    } else if (window.web3) {
        web3Provider = window.web3.currentProvider;
    } else {
        web3Provider = new Web3.providers.HttpProvider('http://localhost:8545');
    }
    window.web3js = new Web3(web3Provider);//web3js就是你需要的web3实例
    window.web3js.eth.getAccounts(function (error, result) {
        if (!error)
            window.accounts = result;
            console.log(window.accounts)//授权成功后result能正常获取到账号了
    });
    App.start();
});