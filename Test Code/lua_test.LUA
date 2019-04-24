--example of single line comment style in LUA
--[[ example of comment block in LUA --]]

--************************************************************
--example of a function for max of two numbers
--************************************************************
function max(num1, num2)

   if (num1 > num2) then
      result = num1;
   else
      result = num2;
   end

   return result; 
end


--calling function
print("The maximum of the two numbers is ",max(10,4))


--************************************************************
--example code for classes/objects in lua and returning an object
--************************************************************

-- Meta class
Rectangle = {area = 0, length = 0, breadth = 0}

-- Derived class method new
--uses function keyword and returns 'o' which is an object
function Rectangle:new (o,length,breadth)
   o = o or {}
   setmetatable(o, self)
   self.__index = self
   self.length = length or 0
   self.breadth = breadth or 0
   self.area = length*breadth;
   return o
end

-- Derived class method printArea

function Rectangle:printArea ()
   print("The area of Rectangle is ",self.area)
end