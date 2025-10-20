from GabesPythonToolBox.ControllSoftwere.StateMachine.StateManager import StateManager
from GabesPythonToolBox.Utility.Debug import *

#takes data from config manager
SM = StateManager(stateFilePaths=CM.data.states.., defaultStateName=CM.data.defoult)
SM.RequestDefaultState(Teleport=True)

#udeate with delta time

#get rules and inndata to change states? exsternal program just gives inndata rest is from config