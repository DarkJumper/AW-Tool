import yaml

from abc import abstractmethod


class AW:

    def __init__(self) -> None:
        self.prices = str()
        self.result_spec = list()
        self.result_pose = str()
        self.result_price = str()
        self.result_bez1 = list()
        self.result_bez2 = list()
        self.set_increace = int()
        self.result_effort = float()
        file = 'Verrechnung.yaml'
        with open(file, 'r') as f:
            self.data = yaml.load(f)
            self._area = strategy(self.data)

    def __call__(self):
        print("test")

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area(self.data)

    @property
    def services(self):
        return self._area.services()

    @property
    def increase(self):
        return self._area.increase()

    @property
    def name(self):
        return self._area.name()

    @property
    def position(self):
        return self._area.position()

    @property
    def bez1(self):
        return self.result_bez1

    @bez1.setter
    def bez1(self, detail_bez):
        self.result_bez1 = self._area.bez1(detail_bez)

    @property
    def bez2(self):
        return self.result_bez2

    @bez2.setter
    def bez2(self, detail_bez):
        self.result_bez2 = self._area.bez2(detail_bez)

    @property
    def note(self):
        return self.result_pose

    @note.setter
    def note(self, pose):
        self.result_pose = self._area.note(pose)

    @property
    def service_spec(self):
        return self.result_spec

    @service_spec.setter
    def service_spec(self, spec):
        self.result_spec = self._area.service_spec(spec)

    @property
    def service_price(self):
        return self.result_price

    @service_price.setter
    def service_price(self, price):
        self.result_price = self._area.service_price(price)

    @property
    def effortprice(self):
        return self.result_effort

    @effortprice.setter
    def effortprice(self, price):
        self.result_effort = self._area.effortprice(price)

    @property
    def table_header(self):
        return self._area.table_header()

    @property
    def increase(self):
        all_faktors = self._area.increase()
        kleinste = list(all_faktors)[0]
        if self.set_increace < kleinste:
            faktor = all_faktors[int(kleinste)]["faktor"]
            return faktor
        else:
            for faktor in reversed(all_faktors):
                if self.set_increace >= int(faktor):
                    faktor = all_faktors[int(faktor)]["faktor"]
                    return faktor

    @increase.setter
    def increase(self, inc):
        self.set_increace = inc


class strategy:

    def __init__(self, data):
        self.prices = str()
        self.spec = str()
        self.pose = str()
        self.price = str()
        self.detail_bez1 = str()
        self.detail_bez2 = str()
        self.all_services = data['Leistungen']
        self.lf = data['LeistungsFaktor']
        self.all_header = data["Header"]

    def services(self):
        return list(self.all_services.keys())

    def increase(self):
        return self.lf["Mehrung"]

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def position(self):
        pass

    @abstractmethod
    def bez1(self, detail_bez):
        pass

    @abstractmethod
    def bez2(self, detail_bez):
        pass

    @abstractmethod
    def note(self, pose):
        pass

    @abstractmethod
    def service_spec(self, spec):
        pass

    @abstractmethod
    def service_price(self, price):
        pass

    @abstractmethod
    def table_header(self):
        pass


class ET(strategy):

    def name(self):
        return "ET"

    def position(self):
        return list(self.all_services["ET"].keys())

    def bez1(self, detail_bez):
        return None

    def bez2(self, detail_bez):
        return None

    def note(self, pose):
        self.pose = pose
        try:
            if self.all_services["ET"][self.pose]["bemerkung"] != None:
                return self.all_services["ET"][self.pose]["bemerkung"]
            else:
                return None
        except KeyError:
            return None

    def service_spec(self, spec):
        self.spec = spec
        if self.spec == "" or self.spec == "---":
            return None
        all_indexes = list(self.all_services["ET"][self.spec].keys())
        all_indexes.remove("bemerkung")
        return all_indexes

    def service_price(self, price):
        self.price = price
        return self.all_services["ET"][self.spec][self.price]

    def table_header(self):
        return list(self.all_header["ET"].split(','))

    def effortprice(self, price):
        self.prices = price
        return float(self.lf["ET"][self.prices])


class PLS(strategy):

    def name(self):
        return "PLS"

    def position(self):
        return list(self.all_services["PLS"].keys())

    def bez1(self, detail_bez):
        self.detail_bez1 = detail_bez
        return list(self.all_services["PLS"][self.detail_bez1].keys())

    def bez2(self, detail_bez):
        return None

    def note(self, pose):
        self.pose = pose
        try:
            if self.all_services["PLS"][self.detail_bez1][self.pose]["bemerkung"] != None:
                return self.all_services["PLS"][self.detail_bez1][self.pose]["bemerkung"]
            else:
                return None
        except KeyError:
            return None

    def service_spec(self, spec):
        self.spec = spec
        if self.detail_bez1 == "" or self.spec == "" or self.spec == "---":
            return None
        all_indexes = list(self.all_services["PLS"][self.detail_bez1][self.spec].keys())
        all_indexes.remove("bemerkung")
        return all_indexes

    def service_price(self, price):
        self.price = price
        return self.all_services["PLS"][self.detail_bez1][self.spec]["programmierung"]

    def table_header(self):
        return list(self.all_header["PLS"].split(','))

    def effortprice(self, price):
        self.prices = price
        return float(self.lf["PLS"]["programmierung"])


class MSR(strategy):

    def name(self):
        return "MSR"

    def position(self):
        return list(self.all_services["MSR"].keys())

    def bez1(self, detail_bez):
        self.detail_bez1 = detail_bez
        bez_text = list(self.all_services["MSR"][self.detail_bez1].keys())
        if (1 in bez_text):
            return list(self.all_services["MSR"][self.detail_bez1][bez_text[0]].keys())
        return bez_text

    def bez2(self, detail_bez):
        self.detail_bez2 = detail_bez
        bez_text = list(self.all_services["MSR"][self.detail_bez2].keys())
        if (2 in bez_text):
            return list(self.all_services["MSR"][self.detail_bez2][bez_text[1]].keys())
        else:
            return None

    def note(self, pose):
        self.pose = pose
        return None

    def service_spec(self, spec):
        self.spec = spec
        if self.detail_bez1 == "" or self.spec == "" or self.spec == "---":
            return None
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez1])):
            return list(self.all_services["MSR"][self.detail_bez1][self.spec].keys())
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez1][1])):
            return list(self.all_services["MSR"][self.detail_bez1][1][self.spec].keys())
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez2][2])):
            return list(self.all_services["MSR"][self.detail_bez2][2][self.spec].keys())
        else:
            return None

    def service_price(self, price):
        self.price = price
        if (self.spec in list(self.all_services["MSR"][self.detail_bez1])):
            return self.all_services["MSR"][self.detail_bez1][self.spec][self.prices]
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez1][1])):
            return self.all_services["MSR"][self.detail_bez1][1][self.spec][self.prices]
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez2][2])):
            return self.all_services["MSR"][self.detail_bez2][2][self.spec][self.prices]
        else:
            return None

    def table_header(self):
        return self.all_header["MSR"].split(',')

    def effortprice(self, price):
        self.prices = price
        return float(self.lf["MSR"][self.prices])
