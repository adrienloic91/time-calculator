# Time Calculator

This Python program calculates the new time after adding a duration to a start time.  
It can also calculate the resulting day of the week and how many days later it will be.

---

## 📋 Project Description

The `add_time` function takes three inputs:  
1. `start` (str): The start time in 12-hour format (e.g., `"3:30 PM"`).  
2. `duration` (str): Duration to add in hours and minutes (e.g., `"2:12"`).  
3. `day` (str, optional): Starting day of the week (e.g., `"Monday"`).

It returns a string showing:  
- The new time in 12-hour format with AM/PM.  
- The day of the week if provided.  
- `(next day)` or `(x days later)` if the time passes into the next day(s).

---

## Example Usage

```python
from time_calculator import add_time

# Basic usage
print(add_time("3:30 PM", "2:12"))
# Output: "5:42 PM"

# With next day
print(add_time("2:59 AM", "24:00"))
# Output: "2:59 AM (next day)"

# Large duration
print(add_time("8:16 PM", "466:02", "Tuesday"))

# Output: "6:18 AM, Monday (20 days later)"

