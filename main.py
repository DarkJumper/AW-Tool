import yaml

if __name__ == "__main__":
    with open('Verrechnung.yaml', 'r') as f:
        data = yaml.load(f)
        print("HALLO?!")
"""         print("__________vorOrt__________")
        print(data["Verrechnung"]["MSR"]["vor Ort"])
        print("__________leitstand__________")
        print("__________erster Kenn________")
        print(data["Verrechnung"]["MSR"]["Leitstand"][1])
        print("__________zweiter Kenn________")
        print(data["Verrechnung"]["MSR"]["Leitstand"][2])
        print("__________Weitere________")
        print(data["Verrechnung"]["MSR"]["weitere"])
        print("__________ET________")
        print(data["Verrechnung"]["ET"])
        print("__________PLS________")
        print(data["Verrechnung"]["PLS"])
        print("__________mehrung________")
        print(data["Verrechnung"]["Mehrung"]) """