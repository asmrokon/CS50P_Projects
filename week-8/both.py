import threading
import time

def cpu_stress(duration_sec):
    print("CPU stress thread started")
    end_time = time.time() + duration_sec
    while time.time() < end_time:
        # Heavy math to keep CPU busy
        x = 0
        for i in range(10**7):
            x += i * i

def ram_stress(size_mb, duration_sec):
    print(f"Allocating approximately {size_mb} MB of RAM...")
    try:
        count = size_mb * 1024 * 1024 // 28  # Approximate int size in bytes
        big_list = [i for i in range(count)]
        print("RAM allocated, now modifying data to keep it busy...")
        
        # Modify the list to keep CPU + RAM busy
        for i in range(0, count, 100000):
            big_list[i] = big_list[i] * 2

        print(f"Holding allocated RAM for {duration_sec} seconds...")
        time.sleep(duration_sec)

    except MemoryError:
        print("MemoryError: Unable to allocate requested RAM!")
    finally:
        del big_list
        print("RAM stress finished, memory freed.")

if __name__ == "__main__":
    duration = 120  # Run stress for 60 seconds
    ram_size = 3900  # Try allocating ~3.5 GB RAM (adjust if too high)

    # Start CPU stress threads (adjust thread count for your CPU cores)
    threads = []
    for _ in range(4):  # If your CPU has 4 cores, else adjust
        t = threading.Thread(target=cpu_stress, args=(duration,))
        t.start()
        threads.append(t)

    # Run RAM stress in main thread
    ram_stress(ram_size, duration)

    # Wait for CPU threads to finish
    for t in threads:
        t.join()

    print("Stress test complete. Your laptop should have been very slow!")
