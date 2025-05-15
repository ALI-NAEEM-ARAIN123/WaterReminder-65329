# water_reminder.py

def calculate_water_intake(weight, age):
    return round((weight * 35) / 1000, 2)  # 35ml per kg

def suggest_reminder_interval(age):
    if age < 18:
        return "Every 3 hours"
    elif age < 50:
        return "Every 2 hours"
    else:
        return "Every 1.5 hours"

def suggest_water_temperature(age):
    if age < 18:
        return "Cool"
    elif age < 50:
        return "Room temperature"
    else:
        return "Lukewarm"

def get_user_input():
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age: "))

        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")

        water_intake = calculate_water_intake(weight, age)
        reminder = suggest_reminder_interval(age)
        temperature = suggest_water_temperature(age)

        print(f"\nRecommended Daily Water Intake: {water_intake} liters")
        print(f"Reminder Frequency: {reminder}")
        print(f"Recommended Water Temperature: {temperature}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the app
get_user_input()
