class Calculator:
    def calculate(self, input_list):
        if input_list[2] == '':
            operand, operator = float(input_list[0]), input_list[1]
            match operator:
                case "sqrt":
                    return self.calc_sqrt(operand)
        else:
            left_operand, operator, right_operand = float(input_list[0]), input_list[1], float(input_list[2])
            match operator:
                case "+":
                    return self.calc_sum(left_operand, right_operand)
                case "-":
                    return self.calc_minus(left_operand, right_operand)
                case "/":
                    return self.calc_division(left_operand, right_operand)
                case "*":
                    return self.calc_multiply(left_operand, right_operand)
                case "**":
                    return self.calc_pow(left_operand, right_operand)
                case _:
                    return "Wrong operator"

    def calc_sum(self, a, b):
        return a + b

    def calc_minus(self, a, b):
        return a - b

    def calc_division(self, a, b):
        return a / b

    def calc_multiply(self, a, b):
        return a * b

    def calc_pow(self, a, b):
        return a ** b

    def calc_sqrt(self, a):
        return a ** 0.5
