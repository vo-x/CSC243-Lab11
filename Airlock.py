class Airlock:
    def __init__(self, code):
        self.code = code
        self.__sealed = False

    def is_sealed(self):
        return self.__sealed

    def __lock_bolts(self):
        print("Bolts locked.")

    def __unlock_bolts(self):
        print("Bolts unlocked.")

    def seal(self):
        if self.__sealed:
            print("Already sealed.")
        else:
            self.__lock_bolts()
            self.__sealed = True
            print("Airlock sealed.")

    def unseal(self):
        if not self.__sealed:
            print("Already open.")
        else:
            self.__unlock_bolts()
            self.__sealed = False
            print("Airlock open.")

    def __str__(self):
        if self.__sealed:
            return "Airlock " + str(self.code) + ": sealed"
        else:
            return "Airlock " + str(self.code) + ": open"
a = Airlock (" H1 ")
print ( a )
a . seal ()
print ( a . is_sealed () )
a . seal ()
a . unseal ()
print ( a )
a . unseal ()