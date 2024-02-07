import GPUtil

def check_gpu():
    try:
        # Get the list of available GPUs
        gpus = GPUtil.getGPUs()

        if not gpus:
            print("No GPUs found on the system.")
        else:
            for i, gpu in enumerate(gpus, 1):
                print(f"GPU {i}:")
                print(f"  Name: {gpu.name}")
                print(f"  Driver: {gpu.driver}")
                print(f"  GPU Memory: {gpu.memoryTotal} MB")
                print(f"  GPU Memory Free: {gpu.memoryFree} MB")
                print(f"  GPU Memory Used: {gpu.memoryUsed} MB")
                print(f"  GPU Load: {gpu.load * 100}%")
                print()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_gpu()
