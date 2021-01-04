import xlsxwriter
import datetime


class createExcel:

    def __init__(self, Name) -> None:
        self.current_row = 0
        self.last_colmn = 0
        self.maxlen = []
        # Create an new Excel file and new Excel Worksheet
        self.workbook = xlsxwriter.Workbook(Name + '.xlsx', {'constant_memory': True})
        self.worksheet = self.workbook.add_worksheet(Name)

    # Einfügen eines Bilds
    def image(self, place, imagefile):
        self.worksheet.insert_image(place, imagefile)

    def set_width(self):
        for row in range(self.current_row):
            for colmn in range(self.last_colmn):
                print(self.maxlen[colmn])
                self.worksheet.set_column(row, colmn, self.maxlen[colmn] * 1.1)

    # Zeilen Länge ermitteln
    def get_width(self, data):
        for row in data:
            if self.maxlen == []:
                for element in row:
                    self.maxlen.append(len(str(element)))
            else:
                for element in range(len(row)):
                    if self.maxlen[element] < len(str(row[element])):
                        self.maxlen[element] = len(str(row[element]))

    # Beschreiben ab letztegenutzte Zeile diese wird intern gelesen
    # Durch start column kann festgelegt werden ab wo beschrieben wird
    def writeString(self, start_column, data):
        for row in data:
            self.worksheet.write_row(self.current_row, start_column, row)
            self.current_row += 1
            if len(row) >= self.last_colmn:
                self.last_colmn = len(row)

    def file_properties(self, Name):
        self.workbook.set_properties(
            {
                'title': 'AW-Berechnung',
                'subject': '',
                'author': Name,
                'manager': '',
                'company': 'Kiel Engineering GmbH',
                'category': '',
                'keywords': '',
                'created': datetime.date(2018, 1, 1),
                'comments': ''
                }
            )

    def close(self):
        # Datei Schließen
        self.workbook.close()
