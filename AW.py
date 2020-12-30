from dataclasses import dataclass


@dataclass
class AW:
    msr: dict
    et: dict
    pls: dict
    faktor: dict
    lf: dict

    def getMSRfaktor(self, *args):
        try:
            if args[0] == "vor Ort":
                if self.msr[args[0]][args[1]][args[3]] == "None":
                    return None
                else:
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
                            if self.msr[args[0]][1][firstkey][args[3]] == "None" or self.msr[args[0]][2][secondkey][
                                args[3]] == "None":
                                return None
                            else:
                                return self.msr[args[0]][1][firstkey][args[3]] + self.msr[args[0]][2][secondkey][args[3]
                                                                                                                 ]
                else:
                    if self.msr[args[0]][1][firstkey][args[3]] == "None":
                        return None
                    else:
                        return self.msr[args[0]][1][firstkey][args[3]]
            elif args[0] == "weitere":
                return self.msr[args[0]][args[1]][args[3]]
        except KeyError:
            return None

    def getETfaktor(self, *args):
        try:
            if self.et[int(args[0])][args[1]] == "None":
                return None
            else:
                return self.et[int(args[0])][args[1]]
        except KeyError:
            return None

    def getPLSfaktor(self, *args):
        try:
            if self.pls[args[0]][args[1]]["programmierung"] == "None":
                return None
            else:
                return self.pls[args[0]][args[1]]["programmierung"]
        except KeyError:
            return None

    def getETinfo(self, *args):
        return self.et[int(args[0])]["info"]

    def getETbemerkung(self, *args):
        return self.et[int(args[0])]["bemerkung"]

    def getPLSinfo(self, *args):
        return self.pls[args[0]][args[1]]["info"]

    def getMSRkeys(self):
        return list(self.msr.keys())

    def getETkeys(self):
        return self.et.keys()

    def getPLSkeys(self):
        return list(self.pls.keys())

    def getFaktorkeys(self):
        return self.faktor

    def getMSRposition(self, *args):
        if args[0] == "vor Ort" or args[0] == "weitere":
            return list(self.msr[args[0]].keys()), None
        elif args[0] == "Leitstand":
            return list(self.msr[args[0]][1].keys()), list(self.msr[args[0]][2].keys())
        else:
            return None, None

    def getPLSposition(self, *args):
        return list(self.pls[args[0]].keys())

    def getMSRlf(self, *args):
        if self.lf["MSR"][args[0]] == "None":
            return None
        else:
            return self.lf["MSR"][args[0]]

    def getETlf(self, *args):
        if self.lf["ET"][args[0]] == "None":
            return None
        else:
            return self.lf["ET"][args[0]]

    def getPLSlf(self):
        if self.lf["PLS"]["programmierung"] == "None":
            return None
        else:
            return self.lf["PLS"]["programmierung"]