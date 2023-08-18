import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"Hello, {nombre} from Github Actions!!!")

if __name__ == "__main__":
    main()