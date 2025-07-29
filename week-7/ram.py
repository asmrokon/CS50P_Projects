import time

def ram_heavy_task(size):
    print(f"Creating a list with {size} million integers...")
    big_list = list(range(size * 1_000_000))
    
    print("Doubling each element in the list...")
    doubled = [x * 2 for x in big_list]
    
    print("Calculating sum of all elements...")
    total = sum(doubled)
    
    print(f"Sum of doubled list: {total}")

if __name__ == "__main__":
    start = time.time()
    ram_heavy_task(2)  # 2 million * 1,000,000 = 2 billion integers (adjust based on your RAM)
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")
