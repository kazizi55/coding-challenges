class InitialSolution:
    def isValid(self, s: str) -> bool:
        stack_list = list()

        for char in s:
            match (char):
                case "(" | "{" | "[":
                    stack_list.append(char)
                case ")":
                    if not stack_list or stack_list[-1] != "(":
                        return False
                    stack_list.pop()
                case "}":
                    if not stack_list or stack_list[-1] != "{":
                        return False
                    stack_list.pop()
                case "]":
                    if not stack_list or stack_list[-1] != "[":
                        return False
                    stack_list.pop()
        return not stack_list
