

//every thing in java is written in classes
public class HelloWorld{
	public static void main(String[] args){
		System.out.println("Hello World");
	}
}

//class / object declaration
public class classExample{
	private String s;
	private String s2;

	//function returning an object
	public classExample returnObj(){
	classExample obj = new classExample;
	obj.s = this.s
	obj.s2 = this.s2;
	return obj;
	}
	//function declaration
	public void setObj(String s, String s2){
		this.s = s;
		this.s2 = s2;
	}

}
//declaring obj
classExample hello = new classExample();
hello.setstring("Hello", "World");

classExample2 helloWorld = hello.returnObj;

