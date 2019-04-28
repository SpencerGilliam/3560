package main


//I/O functions
import "ftm"


//Go doesent really have objects but does have structs
type object struct{
	a string
	b string
}


//function declaration
func helloworld() {
    fmt.Println("Hello World!")
}

func main(){
	helloworld()
	hello := object{
		a: "hello"
		b: "world"
	}
}

//also there are structures called interfaces in GO
//appears to be a struct of methods or functions
//example:

//interface
type geometry interface {
    area() float64
    perim() float64
}
//struct type rectangle
type rect struct {
    width, height float64
}
//methods in the interface
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}