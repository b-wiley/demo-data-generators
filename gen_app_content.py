import random
import string
import csv

def generate_unique_content_id(used_ids):
  """Generates a unique content ID"""
  while True:
    content_id = random.randint(500, 1000)  # Adjust max ID range as needed
    if content_id not in used_ids:
      return content_id

def generate_data(num_rows):
  """Generates a DataFrame with 100 rows of content data"""
  data = []
  used_ids = set()
  for _ in range(num_rows):
    content_id = generate_unique_content_id(used_ids)
    used_ids.add(content_id)
    content_time = random.choice([20, 40, 60, 80, 100, 120])
    content_tags = random.choice(["beginner", "intermediate", "advanced"])
    content_category = random.choice(["Strength Training", "Cardio", "Yoga", "Pilates", "Barre"])
    data.append({
      "content_id": content_id,
      "content_time": content_time,
      "content_tags": content_tags,
      "content_category": content_category
    })
  return data

# Generate and save data
data = generate_data(500)

with open("centr_app_content_data.csv", "w", newline="") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())  # Use fieldnames from first event
  writer.writeheader()
  writer.writerows(data)

print("Data generation and export complete!")
