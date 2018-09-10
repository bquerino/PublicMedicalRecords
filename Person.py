class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name
        self.calendar = Calendar()

    def is_available(self, slot):
        return self.calendar.is_available(slot)

    def make_appointment(self, slot, record):
        self.calendar.add_entry(slot, record)

    def get_public_record(self):
        return {
            'name': self.full_name,
            'booking_class': self.__class__.__name__
        }

class Patient(Person):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name)
        self.id = id
        self.patient_id = self.first_name[:1] + self.last_name + id


class Doctor(Person):
    def __init__(self, first_name, last_name, speciality):
        super().__init__(first_name, last_name)
        self.speciality = speciality

    def get_public_record(self):
        record = super(Doctor, self).get_public_record()
        record['specialty'] = self.speciality
        return record
    
    def schedule(doctor, patient, slot):
        if not doctor.is_available(slot):
            print ('Cannot schedule, doctor is not available:', doctor)
            return
        if not patient.is_available(slot):
            print ('Cannot schedule, patient is not available:', patient)
            return
        
        doctor.make_appointment(slot, patient.get_public_record())
        patient.make_appointment(slot, doctor.get_public_record())

class Calendar(object):
    def __init__(self):
        self.entries = {}

    def is_available(self, slot):
        return slot not in self.entries

    def add_entry(self, slot, record):
        if not self.is_available(slot):
            raise DoubleBookingException
        self.entries[slot] = record

    def __str__(self):
        return str(self.entries)


class DoubleBookingException(Exception):
    pass