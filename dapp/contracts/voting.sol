pragma solidity ^0.4.22;

/// 简答投票合约

contract Ballot {
    // Voter结构体标记了某投票人的投票信息
    struct Voter {
        uint weight;  // 投票的权重(可以理解为某投票人可投的票数)
        bool voted;   // 标记某投票人是否已经投票
        address delegate;  // 委托投票人的地址(投票人委托别人来投票)
        uint vote;    // 提案的索引(理解为一个投票的选项，用下标简单表示)
    }
    //  Proposal结构体标记某个提案的具体信息
    struct Proposal {
        bytes32 name;  // 提案名
        uint voteCount;  // 该提案获得的票数
    }
    
    address public chairperson;  // 主席
    
    mapping(address => Voter) public voters;  // 投票人 => 投票信息的映射
    Proposal[] public proposals;  // 提案动态数组
    
    /// 构造函数,传入提案
    constructor(bytes32[] proposalNames) public {
        chairperson = msg.sender;
        voters[chairperson].weight = 1;
        // 初始化提案数组
        for (uint i = 0;i < proposalNames.length; i++) {
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            })
                );
        }
    }
    /// 主席赋予投票权，即将权重置为1
    function giveRightToVote(address voter) public {
        require(msg.sender == chairperson, "Only chairperson can give right to vote.");  // 只有主席能够赋予投票权
        require(!voters[voter].voted, "The voter already voted.");  // 该投票人不能已经投过票
        require(voters[voter].weight == 0);
        voters[voter].weight = 1;
    }
    
    /// 委托投票,即A本身不投票，将其票数委托给B，B将他们两个人的票数一起投出
    function delegate(address to) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "You already voted.");  // 委托人A不能已经投过票
        require(to != msg.sender, "Self-delegation is disallowed.");  // 委托人A不能再委托自己
        while (voters[to].delegate != address(0)) {  // 被委托人B必须是有效的地址
            to = voters[to].delegate;
            require(to != msg.sender, "Found loop in delegation.");  // 防止链式委托调用又委托回自己
        }
        sender.voted = true;   // 认为委托人A已经投票
        sender.delegate = to;  // 委托B投票
        Voter storage delegate_ = voters[to];  // 找到被委托人B的投票信息
        if (delegate_.voted) {
            // 如果B已经投票了, 就将他投的那个提案再加上委托人A的票数
            proposals[delegate_.vote].voteCount += sender.weight;
        } else {
            // 否则，给B加上委托人A的票数
            delegate_.weight += sender.weight;
        }
    }
    
    /// 投票，传入一个提案的索引即可
    function vote(uint proposal) public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted.");
        sender.voted = true;
        sender.vote = proposal;
        proposals[proposal].voteCount += sender.weight;
    }
    
    /// 确定获胜的提案
    function winningProposal() public view returns (uint winningProposal_)
    {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].voteCount > winningVoteCount) {
                winningVoteCount = proposals[p].voteCount;
                winningProposal_ = p;
            }
        }
    }

    /// 确定获胜提案的名字
    function winnerName() public view returns (bytes32 winnerName_)
    {
        winnerName_ = proposals[winningProposal()].name;
    }
}


[
    "0x123456787989967864735736252"
]