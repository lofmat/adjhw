class Data:
    def __init__(self):
        self.pet_default_data = {"id": 0,
                                 "category": {"id": 0, "name": "string"},
                                 "name": "doggie",
                                 "photoUrls": ["string"],
                                 "tags": [{"id": 0, "name": "string"}],
                                 "status": "available"}
        self.store_default_data = {"id": 0,
                                   "petId": 0,
                                   "quantity": 0,
                                   "shipDate": "2022-02-17T21:39:13.481+0000",
                                   "status": "placed",
                                   "complete": True}

    def init_data(self, keys_to_replace: dict, data_type: str) -> dict:
        if data_type == 'pet':
            data = self.pet_default_data.copy()
        else:
            data = self.store_default_data.copy()
        for key in keys_to_replace.keys():
            if key in data.keys():
                data[key] = keys_to_replace[key]
        return data

