from GabesPythonToolBox.Utility.Debug import Debug
#Debug.add_group('LIB', True) #Uncoment for the debug mesages

import GabesPythonToolBox.Utility.DeltaTime as DT

def test():
    deltaTime = DT.StartDeltaTime()
 
    while True:
        Debug.log(f"time since last key press {deltaTime()}", message_type="Info", group="Showcase")
        Debug.log("waiting on press", message_type="Info", group="Showcase") 
        input("")

if __name__ == "__main__":
    test()