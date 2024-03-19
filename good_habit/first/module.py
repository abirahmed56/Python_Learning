import time

def connect() ->None:
    print('Connecting to internet')
    time.sleep(3)
    print("You are connectedS")

# always keep function in this condition 
# to avoid repeatation in another script which import this script
if __name__ == '__main__':
    connect()