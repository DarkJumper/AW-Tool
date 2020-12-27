import yaml
from dataclasses import dataclass


@dataclass
class AW:
    msr: dict
    et: dict
    pls: dict
    faktor: dict


def getDatafromYaml():
    with open('Verrechnung.yaml', 'r') as f:
        data = yaml.load(f)
        AW(
            data["Verrechnung"]["MSR"], data["Verrechnung"]["ET"], data["Verrechnung"]["PLS"],
            data["Verrechnung"]["Mehrung"]
            )


if __name__ == "__main__":
    getDatafromYaml()
