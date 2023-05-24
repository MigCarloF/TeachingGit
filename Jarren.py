def add(x, y):
    sum = x + y
    return sum

def multiply(x, y):
    product = x * y
    return product

def subtract(x, y):
    diff = x - y
    return diff

def square_function(x):
    square = multiply(x, x)
    return square

def main():
    sum = add(2, 4)
    product = multiply(4, 4)
    diff = subtract(8, 4)
    square = square_function(4)
    print(sum)
    print(product)
    print(diff)
    print(square)

if(__name__ == "__main__"):
    main()