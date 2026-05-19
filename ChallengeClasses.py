#!/usr/bin/python3
"""" This file contains 4 classes for the challenge"""


class PatientRecord:
    """"SuperClass"""
    pass


class ICUPatient(PatientRecord):
    pass


class Outpatient(PatientRecord):
    pass


class Manager:
    """Clinic Manager, admits patients, checks medical metrics"""

    def __init__(self):
        """New manager is born, list of patients is empty"""
        self.patients = []
        print("Manager created")

    def admit_patient(self, patient=PatientRecord):
        """Adds the patient to the list"""
        self.patients.append(PatientRecord)
        print("Patient admited")
