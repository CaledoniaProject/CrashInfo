# Load base config file
from dxConfig import dxConfig;
# Add CrashInfo group if it doesn't exist.
dxCrashInfoConfig = dxConfig.get("CrashInfo", {});
# Add default values where no values have been supplied:
for (sName, xValue) in {
  "bOutputIO": False,           # Output cdb i/o while debugging application
  "uMaxAddressOffset": 0xFFF,   # How far from an address can a pointer be offset and still be considered to point to it?
  "uMaxFunctionOffset": 0xFFF,  # How far from a function symbol can a pointer be offset and still be cosidered to point to it?
  "uMaxStackFramesCount": 20,   # How many stack frames are retreived for analysis?
  "uStackHashFramesCount": 3,   # How many stack frames are hashed for the crash id?
  "asSymbolCachePaths": [],     # Where are symbols cached?
  "bOutputFirstChanceExceptions": False, # Are first chance exceptions detected and output?
  "bOutputCommandLine": False,  # Is the cbd.exe command line printed before execution?
}.items():
  if sName not in dxCrashInfoConfig:
    dxCrashInfoConfig[sName] = xValue;
