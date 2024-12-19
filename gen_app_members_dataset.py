import random
import string

#---------------------------------------------------------------------------------------------------------------------------
# Dummy Data Values

common_first_names = [
  "Olivia", "Emma", "Amelia", "Sophia", "Isabella", "Ava", "Mia", "Evelyn", "Charlotte", "Abigail",
  "Noah", "Liam", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Mason", "Ethan",
  "Sophia", "Avery", "Isla", "Charlotte", "Harper", "Amelia", "Evelyn", "Aaliyah", "Mia", "Scarlett",
  "Lucas", "Jackson", "Aiden", "Mason", "Ethan", "Logan", "David", "Elijah", "James", "Alexander",
  "Emily", "Avery", "Isla", "Sophia", "Charlotte", "Harper", "Amelia", "Evelyn", "Abigail", "Mia",
  "Michael", "Aiden", "William", "Logan", "James", "Benjamin", "Mason", "Elijah", "Alexander", "Jackson",
  "Ashley", "Madison", "Elizabeth", "Sarah", "Emily", "Victoria", "Samantha", "Lauren", "Kaitlyn", "Hannah",
  "Daniel", "Matthew", "Joshua", "Andrew", "Joseph", "David", "Anthony", "Christopher", "John", "Dylan",
  "Elizabeth", "Chloe", "Sophia", "Isabella", "Avery", "Evelyn", "Emilia", "Charlotte", "Harper", "Abigail",
  "Christopher", "Jacob", "William", "Benjamin", "Elijah", "Alexander", "Mason", "Ethan", "James", "Logan"
]

common_last_names = [
  "Smith", "Johnson", "Williams", "Brown", "Jones",
  "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
  "Moore", "Anderson", "Taylor", "Thomas", "Evans",
  "Hall", "Martin", "Lewis", "Clark", "Robinson",
  "Walker", "Young", "Allen", "Scott", "Hernandez"
]

us_cities = [
  "New York City", "Los Angeles", "Chicago", "Houston", "Phoenix",
  "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
  "Jacksonville", "Columbus", "Indianapolis", "Fort Worth", "Charlotte",
  "Detroit", "El Paso", "Memphis", "Seattle", "Denver",
  "Boston", "Washington D.C.", "Miami", "Nashville", "Atlanta",
  "Baltimore", "Oklahoma City", "Milwaukee", "Las Vegas", "Albuquerque",
  "Tucson", "Fresno", "Austin", "Sacramento", "Long Beach",
  "Kansas City", "Mesa", "Virginia Beach", "Omaha", "Cleveland",
  "Colorado Springs", "Raleigh", "Louisville", "Newark", "Buffalo",
  "Philadelphia", "Portland", "Oklahoma City", "Indianapolis", "Jacksonville",
  "San Antonio", "Tulsa", "Austin", "Memphis", "Baltimore",
  "Albuquerque", "Mesa", "Omaha", "Wichita", "Nashville",
  "Norfolk", "Seattle", "Milwaukee", "Columbus", "El Paso",
  "Miami", "Fort Worth", "Charlotte", "Detroit", "Denver",
  "Las Vegas", "Cleveland", "Newark", "Orlando", "Kansas City",
  "Chicago", "Phoenix", "San Diego", "San Jose", "Jacksonville"
]

us_state_abbreviations = [
  "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]


#---------------------------------------------------------------------------------------------------------------------------

def generate_name():
  """Generates a random first and last name"""
  first_name = random.choice(common_first_names)
  last_name = random.choice(common_last_names)
  return first_name, last_name

def generate_email(first_name, last_name):
  """Generates a random email address based on first and last name"""
  domain = ["exampleemail.com", "demoemail.com", "fakeemail.com"]
  return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domain)}"

def generate_unique_user_id(used_ids):
  """Generates a unique user ID, checking against existing ones"""
  while True:
    user_id = random.randint(9000, 20000)
    if user_id not in used_ids:
      return user_id

def generate_data():
  """Generates a single row of data"""
  member_ids = set()  # Keeps track of used IDs
  member_id = generate_unique_user_id(member_ids)
  member_ids.add(member_id)  # Add generated ID to used set
  first_name, last_name = generate_name()
  full_name = f"{first_name} {last_name}"
  email_address = generate_email(first_name, last_name)
  is_member = random.choice([True, False])
  zip_code = random.randint(10000, 99999)
  city = random.choice(us_cities)
  state = random.choice(us_state_abbreviations)
  return member_id, first_name, last_name, full_name, email_address, is_member, zip_code, city, state

# Generate 1000 rows of data
data = []
for _ in range(11000):
  data.append(generate_data())

# Print the data (optional)
#for row in data:
#  print(row)

# Save the data to a CSV file (optional)
import csv
with open("app_members.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["member_id", "first_name", "last_name", "full_name", "email_address", "is_member", "zip_code", "city", "state"])
  writer.writerows(data)

print("Dataset generation complete!")













