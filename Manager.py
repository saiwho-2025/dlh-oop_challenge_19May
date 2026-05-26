#!/usr/bin/python3
"""" This file contains the Manager Class"""

from PatientClasses import *
import json


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

    def generate_nurse_dashboard(self):
        """returns a JSON dashboard """
        dashboard = {
            "patients": [patient.__dict__ for patient in self.patients]
        }
        return json.dumps(dashboard)
