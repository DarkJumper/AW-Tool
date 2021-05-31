from abc import abstractproperty


class AW:

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

    @property
    def services(self):
        return list(self.all_services.keys())

    @property
    def increase(self):
        return self.lf["Mehrung"]

    @abstractproperty
    def position(self):
        pass

    @abstractproperty
    def bez1(self):
        pass

    @abstractproperty
    def bez2(self):
        pass

    @abstractproperty
    def note(self):
        pass

    @abstractproperty
    def service_spec(self):
        pass

    @abstractproperty
    def service_price(self):
        pass

    @abstractproperty
    def table_header(self):
        pass


class ET(AW):

    @property
    def position(self):
        return list(self.all_services["ET"].keys())

    @property
    def bez1(self):
        return None

    @bez1.setter
    def bez1(self, detail_bez):
        self.detail_bez1 = ""

    @property
    def bez2(self):
        return None

    @bez2.setter
    def bez2(self, detail_bez):
        self.detail_bez2 = ""

    @property
    def note(self):
        try:
            if self.all_services["ET"][self.pose]["bemerkung"] != None:
                return self.all_services["ET"][self.pose]["bemerkung"]
            else:
                return None
        except KeyError:
            return None

    @note.setter
    def note(self, pose):
        self.pose = pose

    @property
    def service_spec(self):
        if self.spec == "" or self.spec == "---":
            return None
        all_indexes = list(self.all_services["ET"][self.spec].keys())
        all_indexes.remove("bemerkung")
        return all_indexes

    @service_spec.setter
    def service_spec(self, spec):
        self.spec = spec

    @property
    def service_price(self):
        return self.all_services["ET"][self.spec][self.prices]

    @service_price.setter
    def service_price(self, price):
        self.prices = price

    @property
    def table_header(self):
        return list(self.all_header["ET"].split(','))

    @property
    def effortprice(self):
        return float(self.lf["ET"][self.price])

    @effortprice.setter
    def effortprice(self, price):
        self.price = price


class PLS(AW):

    @property
    def position(self):
        return list(self.all_services["PLS"].keys())

    @property
    def bez1(self):
        return list(self.all_services["PLS"][self.detail_bez1].keys())

    @bez1.setter
    def bez1(self, detail_bez):
        self.detail_bez1 = detail_bez

    @property
    def bez2(self):
        return None

    @bez2.setter
    def bez2(self, detail_bez):
        self.detail_bez2 = ""

    @property
    def note(self):
        try:
            if self.all_services["PLS"][self.detail_bez1][self.pose]["bemerkung"] != None:
                return self.all_services["PLS"][self.detail_bez1][self.pose]["bemerkung"]
            else:
                return None
        except KeyError:
            return None

    @note.setter
    def note(self, pose):
        self.pose = pose

    @property
    def service_spec(self):
        if self.detail_bez1 == "" or self.spec == "" or self.spec == "---":
            return None
        all_indexes = list(self.all_services["PLS"][self.detail_bez1][self.spec].keys())
        all_indexes.remove("bemerkung")
        return all_indexes

    @service_spec.setter
    def service_spec(self, spec):
        self.spec = spec

    @property
    def service_price(self):
        print(self.spec)
        print(self.prices)
        return self.all_services["PLS"][self.detail_bez1][self.spec][self.prices]

    @service_price.setter
    def service_price(self, price):
        self.prices = price

    @property
    def table_header(self):
        return list(self.all_header["PLS"].split(','))

    @property
    def effortprice(self):
        return float(self.lf["PLS"]["programmierung"])

    @effortprice.setter
    def effortprice(self, price):
        self.price = price


class MSR(AW):

    @property
    def position(self):
        return list(self.all_services["MSR"].keys())

    @property
    def bez1(self):
        bez_text = list(self.all_services["MSR"][self.detail_bez1].keys())
        if (1 in bez_text):
            return list(self.all_services["MSR"][self.detail_bez1][bez_text[0]].keys())
        return bez_text

    @bez1.setter
    def bez1(self, detail_bez):
        self.detail_bez1 = detail_bez

    @property
    def bez2(self):
        bez_text = list(self.all_services["MSR"][self.detail_bez2].keys())
        if (2 in bez_text):
            return list(self.all_services["MSR"][self.detail_bez2][bez_text[1]].keys())
        else:
            return None

    @bez2.setter
    def bez2(self, detail_bez):
        self.detail_bez2 = detail_bez

    @property
    def note(self):
        return None

    @note.setter
    def note(self, pose):
        self.pose = pose

    @property
    def service_spec(self):
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

    @service_spec.setter
    def service_spec(self, spec):
        self.spec = spec

    @property
    def service_price(self):
        if (self.spec in list(self.all_services["MSR"][self.detail_bez1])):
            return self.all_services["MSR"][self.detail_bez1][self.spec][self.prices]
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez1][1])):
            return self.all_services["MSR"][self.detail_bez1][1][self.spec][self.prices]
        elif (self.spec in list(self.all_services["MSR"][self.detail_bez2][2])):
            return self.all_services["MSR"][self.detail_bez2][2][self.spec][self.prices]
        else:
            return None

    @service_price.setter
    def service_price(self, price):
        self.prices = price

    @property
    def table_header(self):
        return self.all_header["MSR"].split(',')

    @property
    def effortprice(self):
        return float(self.lf["MSR"][self.price])

    @effortprice.setter
    def effortprice(self, price):
        self.price = price