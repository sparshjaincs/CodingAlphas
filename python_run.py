def Solution(variables_input):
	class CodingAlphas:
	    def __init__(self):
	        self.data = ""
	        
	    def get_String(self,data):
	        self.data = data
	        
	    def print_String(self):
	        print(self.data)
	        
	    def frequency(self):
	        print(len(self.data))
	        
	c1 = CodingAlphas()
	c1.get_String("Hello Tausif")
	c1.print_String()
	c1.frequency()
	

Solution(['                     ', '                '])
