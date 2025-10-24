from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start brewing {name} chai")
    time.sleep(3)
    print(f"End brewing {name} chai")

if __name__ == "__main__":
    chai_option = [
        Process(target=brew_chai, args=(f"{i+1}th",))
        for i in range(4)
    ]

    # starting all processes

    for p in chai_option:
        p.start()
    
    # wait for all to get excecuted
    for p in chai_option:
        p.join()

    print("Thank you")