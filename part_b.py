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
        
def is_operand(string) -> bool:
    return string in "+-/*%"

def is_balanced_paranthesis(expression: str):
    stack = Stack()
    alnum = ""
    for i in expression: 
        if i in "([{":
            stack.push(i)
        elif i == ")":
            if stack.pop() != "(":
                return False
        elif i == "]":
            if stack.pop() != "[":
                return False
        elif i == "}":
            if stack.pop() != "{":
                return False
        elif is_operand(i):
            stack.push(i)
        elif i.isalnum():
            alnum += i
            if len(alnum) > 1:
                popped_val = stack.pop()
                if not is_operand(popped_val):
                    return False
                alnum = ""
     
    return True

if __name__ == "__main__":
    expression:  str = input("Enter expression: ")
    if is_balanced_paranthesis(expression):
        print("Expression is Correct")
    else:
        print("Expression is Incorrect")
    
