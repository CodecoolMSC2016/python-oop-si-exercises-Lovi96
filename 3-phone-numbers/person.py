class Person():
    _name = None
    _phone_number = None

    def __init__(self, _name, _phone_number):
        self._name = _name
        self._phone_number = _phone_number

    def is_phone_number_matching(self, input_phone_number):
        self.input_phone_number = input_phone_number
        if self._phone_number == input_phone_number:
            return True
        else:
            return False

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(_phone_number):
        number = list(_phone_number)
        for i in number[::-1]:

            if i == "-":
                number.remove(i)
            if i == " ":
                number.remove(i)
        result = "".join(number)
        return result
