
class Token(object):
    """
    A token object, holds the id and the token's value.
    """
    
    #this is the constructor method, it returns the token object
    #tid MUST have a value sent in or it will fail
    #if a value is not passed for value parameter then None will be used
    def __init__(self, tid, value = None):
        self._tid = tid
        self._value = value
    
    #this defines how to display the object as a string
    #if this is not implemented then the mem address will be displayed
    def __str__(self):
        # {0} is how you tell python to display a var/obj
        #inside format() is where you declare the vars/objs to display
        stoken = "tid  : {0}\n".format(self._tid) + "value: {0}".format(self._value)
        return stoken
    
    def get_tid(self):
        return self._tid
    
    def get_value(self):
        return self._value


