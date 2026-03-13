# program demonsatrating method (self) and class (counter)

class counter():
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    

if __name__ == "__main__":
    counter = counter() # Object

    # Use 
    counter.increment()
    counter.increment()
    counter.increment()
    counter.increment()
    counter.increment()

    # Print display current output
    # without print even calling counter will not display the output
    print(counter.count) 

    counter.reset()
    print(counter.count) # Reset the counter

    counter.increment()
    counter.increment()
    print(counter.count) # Up to date count

    