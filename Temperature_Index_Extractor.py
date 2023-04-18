class Temperature_Index_Extractor:
    def __init__(self, header_row):
        self.header_row = header_row
    def get_max_temperature_index(self):
        for index, colum_hearder in enumerate(self.header_row):
            if colum_hearder == 'TMAX':
                return int(index)

    def get_min_temperature_index(self):
        for index, colum_hearder in enumerate(self.header_row):
            if colum_hearder == 'TMIN':
                return int(index)