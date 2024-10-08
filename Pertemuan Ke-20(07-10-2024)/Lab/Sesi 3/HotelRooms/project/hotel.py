from .room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = self.__find_room_by_number(room_number)
        if room:
            result = room.take_room(people)
            if result is None:  # Jika kamar berhasil diambil, perbarui jumlah tamu
                self.guests += people

    def free_room(self, room_number: int):
        room = self.__find_room_by_number(room_number)
        if room:
            if room.is_taken:  # Pastikan kamar diambil sebelum membebaskannya
                self.guests -= room.guests  # Kurangi tamu sesuai jumlah yang meninggalkan kamar
            result = room.free_room()
            return result  # Memastikan keluaran dikembalikan jika kamar sudah bebas

    def status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(map(str, free_rooms))}\n"
                f"Taken rooms: {', '.join(map(str, taken_rooms))}")

    def __find_room_by_number(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                return room
        return None
