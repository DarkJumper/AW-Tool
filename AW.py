from dataclasses import dataclass


@dataclass
class AW:
    msr: dict
    et: dict
    pls: dict
    faktor: dict

    def getMSRfaktor(self, *args):
        if args[0] == "vor Ort":
            return self.msr[args[0]][args[1]][args[3]]
        elif args[0] == "Leitstand":
            firstkey = self.msr[args[0]][1].keys()
            for i in firstkey:
                if args[1][0] in i:
                    firstkey = i
                    break
            if len(args[2]) > 0:
                secondkey = self.msr[args[0]][2].keys()
                for i in secondkey:
                    if args[2] in i and len(args[2]) > 0:
                        secondkey = i
                        return self.msr[args[0]][1][firstkey][args[3]] + self.msr[args[0]][2][secondkey][args[3]]
            else:
                return self.msr[args[0]][1][firstkey][args[3]]
        elif args[0] == "weitere":
            return self.msr[args[0]][args[1]][args[3]]

    def getETfaktor(self, *args):
        return self.et[int(args[0])][args[1]]

    def getPLSfaktor(self, *args):
        return self.pls[args[0]][args[1]]["AW"]

    def getETinfo(self, *args):
        return self.et[int(args[0])]["info"]

    def getETbemerkung(self, *args):
        return self.et[int(args[0])]["bemerkung"]

    def getPLSinfo(self, *args):
        return self.pls[args[0]][args[1]]["info"]

    def getMSRkeys(self):
        return self.msr.keys()

    def getETkeys(self):
        return self.et.keys()

    def getPLSkeys(self):
        return self.pls.keys()

    def getFaktorkeys(self):
        return self.faktor.keys()

    def getMSRfunktion(self, *args):
        return self.msr[args[0]].keys()
