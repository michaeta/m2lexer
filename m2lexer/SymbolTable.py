#This imports the token class definition from the token.py file
#Since both files are in the same dir then we don't need a path
#if they weren't then you specify the location like:
# from Documents.CS480.token import token 
from tokens.token import Token

class SymbolTable:
    """
    Its the symbol table. It has a dictionary where each token is stored
    """
    
    #a dictionary in python is like a hash table, but it has a lot more features
    def __init__(self):
        self._table = dict()
    
    def __str__(self):
        stable = "----- Symbol Table -----"
        #for loops are easy in python!
        for tid in self._table.keys():
            #the :< left aligns text and :> right aligns it
            #the number of spaces indicates amount of padding
            stable += "\n{0:<5}| {1:<17}".format(tid, self._table[tid])
        return stable
    
    def add_token(self, token):
        #the tid is the key in the hash table / dict and the value is the value
        self._table[token.get_tid()] = token.get_value()
        
    def get_token(self, tid = int):
        #create a token from the symbol table and return it
        token = Token(tid, self._table[tid])
        return token

#a main function is also easy in python!    
#these below are just examples and will be removed
def main():
    derp = Token(1, "int")
    herp = Token(2, "string")
    rate = Token(3, "real")
    pos = Token(4, "float")
    wtf = Token(5, "bool")
    
    table = SymbolTable()
    
    table.add_token(derp)
    table.add_token(herp)
    table.add_token(rate)
    table.add_token(pos)
    table.add_token(wtf)
    
    #inside a print statement python will automatically call the obj's __str__ function,
    #but since I am concatinating a \n on the end I need to type cast it first
    print(str(derp) + "\n")
    #no type casting b/c there are no string operators being applied
    print(table)

#if this python file is being ran directly, like the user clicks on it to run it
#then the main function is called and ran. If it is going to be imported as a module 
#so other python files can use the class definitions then the main function will not be ran
if __name__ == "__main__":
    main()
        