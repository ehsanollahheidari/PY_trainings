import time

def execution_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        print(f"Execution time of '{func.__name__}': {execution_time:.6f} seconds")
        
        return result
    return wrapper

@execution_timer
def generate_list_from_1_to_n(n):
    return list(range(1, n + 1))

# Get input from user
if __name__ == "__main__":
    try:
        n = int(input("Enter number n: "))
        
        result_list = generate_list_from_1_to_n(n)

        print(f"Generated list: {result_list}")
        
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {e}")