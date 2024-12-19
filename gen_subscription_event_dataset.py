import random
from datetime import datetime, timedelta

def generate_subscription_event_id(used_ids):
  """Generates a unique subscription event ID"""
  while True:
    event_id = random.randint(1000000, 2000000)  # Adjust max ID range as needed
    if event_id not in used_ids:
      return event_id


def generate_event_timestamp():
  """Generates a random event timestamp within the last 3 years in ISO 8601 format"""
  base_date = datetime.now() - timedelta(days=3*365)  # Adjust time range to 3 years
  random_delta = timedelta(days=random.randint(0, 3*365))
  event_timestamp = base_date + random_delta
  return event_timestamp.isoformat(timespec='milliseconds') + '+0000'  # Add milliseconds and offset

def generate_event_type():
  """Selects a random event type"""
  event_types = ["Subscription Purchase", "Subscription Cancelled", "Subscription Started"]
  return random.choice(event_types)

def generate_data(used_event_ids):
  """Generates a single row of data"""
  event_id = generate_subscription_event_id(used_event_ids)
  used_event_ids.add(event_id)
  member_id = random.randint(9000, 20000)
  event_timestamp = generate_event_timestamp()
  event_type = generate_event_type()
  return event_id, member_id, event_timestamp, event_type

# Generate 1000 rows of data
data = []
used_event_ids = set()
for _ in range(81230):
  data.append(generate_data(used_event_ids))

# Print or save data (optional)
# for row in data:
#   print(row)

# Save the data to a CSV file (optional)
import csv
with open("centr_subscription_events.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["subscription_event_id", "member_id", "event_timestamp", "event_type"])
  writer.writerows(data)

print("Dataset generation complete!")
