#!/usr/bin/python3
from PatientClasses import *
from Manager import Manager


def main():

    manager = Manager()
    icu_patient = ICUPatient()
    out_patient = Outpatient()
    patient = PatientRecord()

    manager.admit_patient(icu_patient)
    manager.admit_patient(out_patient)
    manager.admit_patient(patient)

    print(manager.__dict__)


if __name__ == "__main__":
    main()
