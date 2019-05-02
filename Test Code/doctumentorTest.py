


#1
class funcTests():
#2
        
	def func(self, test):
		print("Hello,", test)
#3


	def func2(self, test):
#4
		print("Goodbye,", test)


def func(test):
	print("reeeeeeeee,", test)

test = funcTests()
func("michael")
test.func("michael")
test.func2("michael")