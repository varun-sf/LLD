# LLD
1- created a parking system, only one system can exist at a time(Used singleton pattern).
2- Once a parking system is created, it creates a PARKING LOT, inside PARKING LOT we can add PARKING LEVEL, and each level has list of PARKING SPOT.
3- Each PARKING SPOT stores Account, and Account class stores licence number.
4- Vehicle class is inherited to different products like car, motorcycle etc. And this products are mentioned in enum class VEHICLE TYPE.