//function declaration with one parameter
function test(Parameter1) {
    document.getElementById("demo").innerHTML = "Hello World!";
    document.getElementById("demo").innerHTML = Parameter1.a + " " + Parameter1.b;
}

//This is the only way I saw about returning a "object"
function returnObject(x,y){
    var object1 ={
        a: x,
        b: y,
        }
    return object1;
}

//object decaration
var object2 = {
    a: "Hello",
    b: "World",
};


test(object2);// test print function call
var obj2 = returnObject("hello","world");

//this is a comment in javascript(same as c++)