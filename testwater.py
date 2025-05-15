# test_water_reminder.py
import pytest
from water_reminder import calculate_water_intake, suggest_reminder_interval

def test_calculate_water_intake():
    assert calculate_water_intake(70, 25) == 2.45
    assert calculate_water_intake(50, 30) == 1.75

def test_suggest_reminder_interval():
    assert suggest_reminder_interval(10) == "Every 3 hours"
    assert suggest_reminder_interval(30) == "Every 2 hours"
    assert suggest_reminder_interval(60) == "Every 1.5 hours"
