pragma solidity ^0.5.0;

contract EcommerceStore {
    // 电商合约，存储用户即用户对应商品的信息
    // 这里把用户理解为商店，其商店的商品就是他要拍卖的物品
    // 0x1245 => {1 => "商品信息"}
    enum ProductStatus { Open, Sold, Unsold }
    enum ProductCondition { New, Used }
    uint public productIndex;  // 商品计数器
    mapping (uint => address) productIdInStore;  // 记录商品索引属于哪个商店(用户)
    mapping (address => mapping(uint => Product)) stores; // 记录一个用户的商店中的所有商品

    // 记录商品详细信息
    struct Product {
        uint id;
        string name;
        string category;
        string imageLink;
        string descLink;
        uint auctionStartTime;
        uint auctionEndTime;
        uint startPrice;
        address payable highestBidder;
        uint highestBid;
        uint secondHighestBid;
        uint totalBids;
        ProductStatus status;
        ProductCondition condition;
        // 这里的bytes32是每次出价经过sha3加密后得到的哈希值
        mapping (address => mapping (bytes32 => Bid)) bids;
    }

    struct Bid {
        address bidder;
        uint productId;
        uint value;  // 不是实际的出价，而是出价者实际发送的ETH数量(保证金)
        bool revealed;
    }

    constructor () public {
        productIndex = 0;
    }

    // 上传一个商品信息，保存到区块链
    function addProductToStore(
        string memory _name, string memory _category, string memory _imageLink, string memory _descLink, uint _auctionStartTime, 
        uint _auctionEndTime, uint _startPrice, uint _productCondition
    ) public {
        require(_auctionStartTime < _auctionEndTime, "auction start time should be lower than auction end time.");
        productIndex += 1;
        Product memory product = Product(productIndex, _name, _category, _imageLink, _descLink, _auctionStartTime,
        _auctionEndTime, _startPrice, address(0), 0, 0, 0, ProductStatus.Open, ProductCondition(_productCondition));
        stores[msg.sender][productIndex] = product;
        productIdInStore[productIndex] = msg.sender;
    }

    // 根据商品id获取商品详细信息
    function getProduct(uint _productIndex) view public returns (uint, string memory, string memory, string memory, string memory, uint, uint, uint, ProductStatus, ProductCondition) {
        Product memory product = stores[productIdInStore[_productIndex]][_productIndex];
        return (product.id, product.name, product.category, product.imageLink, product.descLink, product.auctionStartTime, 
        product.auctionEndTime, product.startPrice, product.status, product.condition);
    }

    // 出价函数，需要商品id，真正出价的哈希值(bytes32的值)作为参数
    function bid(uint _productId, bytes32 _bid) payable public returns (bool) {
        Product storage product = stores[productIdInStore[_productId]][_productId];
        require(now >= product.auctionStartTime, "current time should be larger than auction start time.");
        require(now <= product.auctionEndTime, "current time should be slower than auction end time.");
        require(msg.value > product.startPrice, "value should be larger than product start price.");
        // 防止用户对同一个商品出同一个报价
        require(product.bids[msg.sender][_bid].bidder == address(0), "bider should be null");
        product.bids[msg.sender][_bid] = Bid(msg.sender, _productId, msg.value, false);
        product.totalBids += 1;
        return true;
    }

    // 揭示报价，需要商品id，真正的出价，秘钥作为参数
    function revealBid(uint _productId, string memory _amount, string memory _secret) public {
        Product storage product = stores[productIdInStore[_productId]][_productId];
        require(now > product.auctionEndTime, "auction should be ended.");
        /* 
        由于sha3函数已经被移除，所以只能用keccak256，且该函数只能接受bytes类型的参数
        solidity不支持string拼接，所以用abi.encodePacked(s1, s2)来拼接
        */
        bytes memory b = bytes(abi.encodePacked(_amount, _secret));
        // 得到真正出价的哈希值
        bytes32 sealedBid = keccak256(b);
        Bid memory bidInfo = product.bids[msg.sender][sealedBid];
        require(bidInfo.bidder != address(0));
        require(bidInfo.revealed == false);
        uint refund;  // 没有竞拍成功的人应该退回的钱
        uint amount = stringToUint(_amount);
        if (bidInfo.value < amount) {
            // 判断是否是合理出价，即保证金 < 真正的出价，认为是无效的
            refund = bidInfo.value;
        } else {
            if (product.highestBidder == address(0)) {
                // 该商品还没有最高出价
                product.highestBidder = msg.sender;
                product.highestBid = amount;
                product.secondHighestBid = product.startPrice;
                refund = bidInfo.value - amount;
            } else {
                if (amount > product.highestBid) {
                    // 已经有最高报价，但是出价比当前最高报价还高
                    // 先把当前最高报价退回
                    product.secondHighestBid = product.highestBid;
                    product.highestBidder.transfer(product.highestBid);
                    product.highestBidder = msg.sender;
                    product.highestBid = amount;
                    refund = bidInfo.value - amount;
                } else if (amount > product.secondHighestBid) {
                    // 比第二价高，则记录下来，然后退回所有钱(最高价才能赢得竞拍！)
                    product.secondHighestBid = amount;
                    refund = bidInfo.value;
                } else {
                    refund = bidInfo.value;
                }
            }
        }
        product.bids[msg.sender][sealedBid].revealed = true;
        if (refund > 0) {
            msg.sender.transfer(refund);
        }
    }

    // string 转 uint
    function stringToUint(string memory s) private pure returns(uint) {
        bytes memory b = bytes(s);
        uint result = 0;
        for (uint i = 0; i < b.length; i++) {
            if (uint(uint8(b[i])) >= 48 && uint(uint8(b[i])) <= 57) {
                result = result * 10 + (uint(uint8(b[i])) - 48);
            }
        }
        return result;
    }

    function highestBidderInfo(uint _productId) public view returns(address, uint, uint) {
        Product memory product = stores[productIdInStore[_productId]][_productId];
        return (product.highestBidder, product.highestBid, product.secondHighestBid);
    }

    function totalBids(uint _productId) public view returns(uint) {
        Product memory product = stores[productIdInStore[_productId]][_productId];
        return product.totalBids;
    }

    
}