class MyQeue:
    def __init__(self):
        self.stack_in = [] #head
        self.stack_out = [] #tail
    def __len__(self):
        return len(self.stack_in) + len(self.stack_out)
    
    def push(self, obj):
        self.stack_in.append(obj)
    
    def pop(self):
        """We must pop the first pushed element. However, we are using lists that follow the LIFO rule.
         So in order to implement the FIFO rule we must reverse the order of elements in one stack and 
          simply pop it in the second one using pop method which removes items from the tail of the stack. """
        if not self.stack_out:
            self.stack_out = self.stack_in[::-1] #reverse the order of the items, like changing head to tail
            self.stack_in = []
        return self.stack_out.pop() #pop items if stack_out is already full
