import GabesPythonToolBox.Utility.DeltaTime as DT

def test():
    deltaTime = DT.StartDeltaTime()

    while True:
        print(f"time since last key press {deltaTime()}")
        input("waiting on press")

if __name__ == "__main__":
    test()