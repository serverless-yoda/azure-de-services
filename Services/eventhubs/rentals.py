class Rental:
    def __init__(self, rentalid, status, pickuploc, dropoffloc, pickupdate, dropoffdate, country, ts):
        self.rentalid = rentalid
        self.status = status
        self.pickuploc = pickuploc
        self.dropoffloc = dropoffloc
        self.pickupdate = pickupdate
        self.dropoffdate = dropoffdate
        self.country = country
        self.ts = ts
        self.table_folder = 'landing/rental'

