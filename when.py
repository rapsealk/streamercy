#!/usr/bin/python3
# -*- coding: utf-8 -*-

def when(value, switch):
    assert("default" in switch)
    if value in switch:
        switch[value]()
    else:
        switch["default"]()


if __name__ == "__main__":
    switch = {
        "ronald": lambda: print("Hi! I'm Ronald Weasely!"),
        "harry": lambda: print("I am Potter."),
        "default": lambda: print("Oh..")
    }
    when("harry", switch)
    when("no..", switch)