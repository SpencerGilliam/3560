using System;
namespace funcex1
{
    //class def
    class Test
    {
        private string string;
        //function in c#
        public void SayHello()
        {
            Console.WriteLine("Hello");
        }
        //object return in c#
        public Test objectReturn()
        {
            Test obj = new Test();
            obj.string = "hello world";
            return obj;
        }
    }

    //driver program
    class Program
    {
        static void Main(string[] args)
        {
            var t = new Test();
            var t2 = new Test();
            t.SayHello();
            t2 = t.objectReturn();
            Console.ReadKey();
        }
    }
}