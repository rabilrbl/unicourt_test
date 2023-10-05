class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, elem):
        return self.stack.append(elem)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return ""
        
    

def is_balanced_paranthesis(expression: str):
    stack = Stack()
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.pop() != "(":
                return False
        elif i == "[":
            stack.push(i)
        elif i == "]":
            if stack.pop() != "[":
                return False
        elif i == "{":
            stack.push(i)
        elif i == "}":
            if stack.pop() != "{":
                return False
    return True

if __name__ == "__main__":
    expression:  str = input("Enter expression: ")
    if is_balanced_paranthesis(expression):
        print("Expression is Correct")
    else:
        print("Expression is Incorrect")
    
