name = "DDD"
count = 1

def another():
    color = "Blue"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color 
        color = "f"
        print(name)
        print(color)
    
    greeting("Dave")

another()