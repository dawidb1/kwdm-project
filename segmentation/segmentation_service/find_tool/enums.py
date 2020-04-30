from enum import Enum


class Level(Enum):
    PATIENT = "Patient"
    INSTANCE = "Instance"
    STUDY = "Study"


class Modality(Enum):
    FLAIR = "FLAIR"
    T1 = "T1"
    T2 = "T2"
    T2CE = "T2CE"
