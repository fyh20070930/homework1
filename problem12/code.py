def isValid(s: str) -> bool:
    stack = []
    # 右括号对应匹配的左括号
    match = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in match:
            # 当前是右括号，栈顶必须是对应的左括号
            if not stack or stack.pop() != match[ch]:
                return False
        else:
            # 左括号，压栈
            stack.append(ch)
    # 遍历完栈必须为空
    return len(stack) == 0

if __name__ == "__main__":
    s1 = "()[]{}"
    s2 = "(]"
    print(f"{s1}: {isValid(s1)}")
    print(f"{s2}: {isValid(s2)}")
