#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
        self._name = name
        self._job = job
        if len(name) > 25:
            self._name = "Name must be string between 1 and 25 characters."
        
        if job not in APPROVED_JOBS:
            self._job = "Job must be in the list of approved jobs."

    def get_name(self):
        return self._name

    def get_job(self):
        return self._job

jack = Person("jack","ITC")