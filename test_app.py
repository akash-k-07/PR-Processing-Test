import logging

def hello_world():
    print("Hello, World!")
    print("hi welcome")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("This is a test log for the hello_world function.")
    hello_world()
