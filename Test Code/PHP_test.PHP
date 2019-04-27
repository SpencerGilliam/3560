<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>';
	// Defining a PHP Function
         function helloworld() {
            echo "Hello again world";
         }
         //class declaration example
		class C {
			var $a;
			var $b;
		}
		//returning an object
		function getC(): C {
			 return new C;
		}

		var_dump(getC());

         // Calling a PHP Function 
         helloworld();
 
 
 ?> 

 </body>
</html>