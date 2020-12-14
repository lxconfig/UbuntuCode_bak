


def isVaild(s: str) -> bool:
    """判断括号是否匹配 ()[]{}"""
    # 用栈来做
    stack = []
    brackets_map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for i in s:
        if i not in brackets_map:
            # 遇到左括号，就入栈
            stack.append(i)
        elif not stack or brackets_map[i] != stack.pop():
            # 如果不是左括号，并且栈不为空，或字典元素不等于栈顶元素，说明不合法
            return False
    return not stack   # 可能有一对括号匹配，但还剩一个括号的情况，如："{[]"


if __name__ == "__main__":
    print(isVaild("]{}"))