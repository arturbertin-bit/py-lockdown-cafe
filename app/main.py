import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(NotVaccinatedError)
    pass

class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor don't have vaccine")
        if visitor["vaccine"]["expiration_date"] < datetime.date:
            raise OutdatedVaccineError("Outdated Vaccine")
