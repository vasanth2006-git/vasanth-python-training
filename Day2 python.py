class Cgpa:
    def __init__(self):
        self.cgpa = []
        self.result = []

    def check_elgiblity(self):
        for i in self.cgpa:
            if i <= 70:
                self.result.append("NA")
            elif i > 70 and i < 86:
                self.result.append("3R")
            elif i > 85 and i < 101 :
                self.result.append("1R")
            else:
                self.result.append("invalid")
        return self.result
            
    def get_input(self):
        no_of_mark = int(input("enter the number of marks"))
        for a in range(no_of_mark):
           mark =int(input("percentage:"))
           self.cgpa.append(mark)
        
    def give_output(self):
        print(self.result)

print("No of rounds for each percantage of marks:")
result = Cgpa()
result.get_input()
result.check_elgiblity()
result.give_output()

output:
No of rounds for each percantage of marks:
enter the number of marks5
percentage:80
percentage:75
percentage:105
percentage:90
percentage:33
['3R', '3R', 'invalid', '1R', 'NA']



