# STEP 1
class Entry:

    def __init__(self, day = 0, description = "default entry", start = 0, end = 23, location = None):
        self.description = description
        if isinstance(day, int) and day >= 0:
            self.__day = day
        if self.is_valid_slot(start):
            self.__start = start
        if self.is_valid_slot(end):
            self.__end = end
        if location is not None:
            self.__location = location

    def __eq__(self, other):
        if not isinstance(other,Entry):
            return False
        return self.get_description() == other.get_description() and self.get_day() == other.get_day() and \
               self.get_start_slot() == other.get_start_slot() and self.get_end_slot() == other.get_end_slot() and\
               self.get_location() == other.get_location()


    def __ne__(self, other):
        # if self.__day == other.__day or self.__start == other.__start or self.__end == other.__end:
        #     return False
        # return True
        return not self == other


    def __str__(self):
        if hasattr(self, '_Entry__location'):
            return str(self.description) + ' on ' + str(self.__day) + ' from ' + str(self.__start) + ' until ' + str(self.__end) + ' at ' + str(self.__location)
        return str(self.description) + ' on ' + str(self.__day) + ' from ' + str(self.__start) + ' until ' + str(self.__end)

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def set_location(self, location):
        if location is None:
            del self.__location
        else:
            self.__location = location

    def get_day(self):
        return self.__day

    def get_start_slot(self):
        return self.__start

    def get_end_slot(self):
        return self.__end

    def get_location(self):
        if not hasattr(self, "_Entry__location"):  # class moet er voor
            return None
        return self.__location

    def is_valid_slot(self, number):
        if number in range(0, 24):
            return True

    def occupies_slot(self, time_slot):
        if time_slot in range(self.__start, self.__end + 1):
            return True
        return False

    def overlaps_with(self, other):
        if self.__day == other.__day:
            for time_1 in range(self.__start, self.__end + 1):
                for time_2 in range(other.__start, other.__end + 1):
                    if time_1 == time_2:
                        return True
            return False


class Agenda:

    def __init__(self):
        self.__entries = list()

    def __str__(self):
        self.__entries.sort(key=lambda x: (x._Entry__day,x._Entry__end))
        string = ""
        for entry in self.__entries:
            string += (str(entry) + '\n')
        return string

    def add_entry(self, new_entry):
        OVERLAP = False
        for entry in self.__entries:
            if new_entry.overlaps_with(entry):
                OVERLAP = True
                return False
        if not OVERLAP:
            self.__entries.append(new_entry)
            return True

    def get_entries_on_day(self, day):
        entries_on_day = list()
        for entry in self.__entries:
            if entry.get_day() == day:
                entries_on_day.append(entry)
        return entries_on_day

    def remove_entry(self, remove_entry):
        for entry in self.__entries:
            if entry == remove_entry:
                self.__entries.remove(remove_entry)


entry = Entry(description="Methodiek van de informatica")
assert entry.get_description() == "Methodiek van de informatica"

#STEP 2
entry = Entry(day=200)
assert entry.get_day() == 200

#STEP 3
meeting = Entry(description="Dinner",day=133,start=18,end=22)
assert meeting.get_description() == "Dinner"
assert meeting.get_day() == 133
assert meeting.get_start_slot() == 18
assert meeting.get_end_slot() == 22

#STEP 4
meeting = Entry(description="Dinner",day=133,start=18,end=22)
for slot in range(0,18):
    assert not meeting.occupies_slot(slot)
for slot in range(18,23):
    assert meeting.occupies_slot(slot)
assert not meeting.occupies_slot(23)
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert not meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=12, end=13)
assert meeting.overlaps_with(meeting2)
meeting2 = Entry(description="Lunch", day=42, start=13, end=14)
assert not meeting.overlaps_with(meeting2)

#STEP 5
agenda = Agenda()
meeting = Entry(description="Dinner",day=133,start=18,end=22)
assert agenda.add_entry(meeting)
assert not agenda.add_entry(meeting)
assert len(agenda._Agenda__entries) == 1

agenda = Agenda()
meeting = Entry(description="Dinner",day=133,start=18,end=22)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
meeting3 = Entry(description="Breakfast", day=41, start=8, end=8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
assert len(agenda.get_entries_on_day(133)) == 1
assert len(agenda.get_entries_on_day(41)) == 2

#STEP 6
meeting = Entry()
meeting2 = Entry()
assert meeting == meeting2
assert not meeting != meeting2
meeting = Entry(description="Study", day=42, start=9, end=12)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
assert meeting != meeting2
assert not meeting == meeting2

#STEP 7
agenda = Agenda()
meeting = Entry(description="Breakfast", day=41, start=8, end=8)
meeting2 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
meeting3 = Entry(description="Lunch", day=41, start=12, end=13)
agenda.remove_entry(meeting3)
assert len(agenda._Agenda__entries) == 1
meeting4 = Entry(description="Dinner",day=133,start=18,end=22)
agenda.remove_entry(meeting4)
assert len(agenda._Agenda__entries) == 1

#STEP 8
meeting = Entry(description = "Dinner", day = 133, start = 18, end = 22)
assert meeting.get_location() == None
meeting.set_location("De Volle Pollepel")
assert meeting.get_location() == "De Volle Pollepel"
meeting.set_location(None)
assert meeting.get_location() == None

#STEP 9
meeting = Entry(description = "Dinner", day = 133, start = 18, end = 22)
assert str(meeting) == "Dinner on 133 from 18 until 22"
meeting.set_location("De Volle Pollepel")
assert str(meeting) == "Dinner on 133 from 18 until 22 at De Volle Pollepel"

# STEP 10
agenda = Agenda()
meeting = Entry(description = "Dinner", day = 133, start = 18, end = 22)
meeting2 = Entry(description = "Lunch", day = 41, start = 12, end = 13)
meeting3 = Entry(description = "Breakfast", day = 41, start = 8, end = 8)
agenda.add_entry(meeting)
agenda.add_entry(meeting2)
agenda.add_entry(meeting3)
assert str(agenda) == "Breakfast on 41 from 8 until 8\nLunch on 41 from 12 until 13\nDinner on 133 from 18 until 22\n"

print("OK.")
