from collections import defaultdict as dd
import subprocess

def printOnce():
    class v:hasPrinted = False
    def p(*messages):
        if not v.hasPrinted: print(*messages)
        v.hasPrinted = True
    return p

### READ DATA 
class sent: 
    eS,fS=[],[]
    def __init__(self,eS,fS):
        self.eS=["*"]+eS.split()
        self.fS=fS.split()
        self.l = len(self.eS)-1
        self.m = len(self.fS)

def readTrain():return readFile("corpus")
def readDev():return readFile("dev")
def readFile(name):
    with open(f"lib/{name}.en")as eF:
        with open(f"lib/{name}.es")as fF:
            return [sent(eS,fS) for eS,fS in zip(eF,fF)]

def outputPred(model, pred):
    with open(f"lib/dev{model}.out","w") as f:
        for sI,eI,fI in pred:
            f.write(f"{sI} {eI} {fI}\n")

def evalModel(model):
    exp = 1 == model and ".42" or ".45"
    print("#############################")
    print(f"# IBM Model {model}: {exp} Expected #")
    print("#############################")
    subprocess.run(f"python lib/eval_alignment.py lib/dev.key lib/dev{model}.out",shell=True)

def outputTParams(t:dict):
    with open(f"lib/tParams.out","w") as f:
        for key1 in t:
            for key2 in t[key1]:
                f.write(f"{key1} {key2} {t[key1][key2]}\n")

def recoverTParams():
    t = dd(lambda:dd(int))
    with open(f"lib/tParams.out") as f:
        for line in f:
            key1, key2, value = line.split()
            t[key1][key2] = float(value)
    return t