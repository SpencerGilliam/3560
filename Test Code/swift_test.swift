//function declaration
func HelloWorld(){
print("hello world")

}

//class/object declaration
class classExample {
	var a: String
	var b: String
	
	init(a: String, b: Int){
		self.a = a
		self.b = b
	}
	
	func print(){
		print(self.a)
		print(self.b)
	}
}

//call function of classExample
var x = classExample(a: "hello", b: "World")
//calling print from class
classExample.print()
//calling print function
HelloWorld()

//will come back to this and add returning object when I find out more about
//swift and how to do it or if it is possible
//this is a comment in swift (same as c/c++)