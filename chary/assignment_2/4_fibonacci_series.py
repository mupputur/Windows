# Write a program print the  Fibonacci series  till 100


def fibonacci_series(last_value):
    y=[0,1]
    for i in range(2,last_value):
        if y[-1]<last_value/1.5:
            y.append(y[i-2]+y[i-1])
        else:
            break
    return y

print("The Fibonacci series till 100 is:")
output_list = fibonacci_series(100)
print(output_list)

