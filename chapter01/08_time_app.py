# Constants
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

# Prompt
total_seconds = int(input("Enter the number of seconds: "))

# Calculations
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

minutes = total_seconds // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

print(f"{total_seconds} seconds it equal to")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds_remaining} seconds")

# 105310 second is equal to
# 1 days, 5 hours, 1755 minutes, 10 seconds