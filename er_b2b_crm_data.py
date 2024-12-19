import random
import csv
import datetime
import uuid
import string

# List of common first names
first_names = ["John", "David", "Michael", "Christopher", "Matthew", "James", "Joshua", "Daniel", "Joseph", "William", "Anthony", "Robert", "Brian", "Eric", "Steven", "Kevin", "Timothy", "Charles", "Jeffrey", "George"]

# List of common last names
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Moore", "Jackson", "White", "Lee", "Harris", "Clark"]

companies = [
    "Walmart",
    "Amazon",
    "Apple",
    "UnitedHealth Group",
    "Berkshire Hathaway",
    "CVS Health",
    "ExxonMobil",
    "Johnson & Johnson",
    "McKesson",
    "Cencora",
    "AT&T",
    "Verizon Communications",
    "Ford Motor Company",
    "General Motors",
    "JPMorgan Chase & Co.",
    "Bank of America Corp.",
    "Wells Fargo & Company",
    "United Airlines Holdings Inc.",
    "Delta Air Lines Inc.",
    "American Airlines Group Inc.",
    "Intel Corp.",
    "General Electric Co.",
    "Chevron Corp.",
    "Kroger Co.",
    "Comcast Corp.",
    "PepsiCo Inc.",
    "Anthem Inc.",
    "Caterpillar Inc.",
    "Home Depot Inc.",
    "Target Corp.",
]

# Function to generate a random email address
def generate_random_email(first_name, last_name):
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com"])
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"

# Function to generate a random phone number
def generate_random_phone_number():
    return "555-" + "".join(random.choice("0123456789") for _ in range(7))

# Function to generate a random timestamp within a specified range
def generate_random_timestamp(start_date, end_date):
    seconds_in_range = int((end_date - start_date).total_seconds())
    random_seconds = random.randint(0, seconds_in_range)
    return start_date + datetime.timedelta(seconds=random_seconds)

# Generate USER_ID with an 80% chance of being NULL -- represents anon users
# USER_ID will be 1:1 relationship with email address when not null
def generate_user_id(email, email_user_map):
    if email not in email_user_map:
        user_id = None if random.random() < 0.2 else random.randint(100000000, 999999999)
        email_user_map[email] = user_id
    else:
        user_id = email_user_map[email]
    
    return user_id

# Generate IP Address -- N:1 relationship with Email; 30% reuse rate for IP Address because people can use the same IP Address 
def generate_ip_address(email_address, email_ip_map, reuse_probability=0.3):
    # 30% chance of reusing an IP address, 70% chance of generating a new one
    if email_address in email_ip_map and random.random() < reuse_probability:
        # Reuse an existing IP address
        ip_address = random.choice(email_ip_map[email_address])
    else:
        # Generate a new IP address
        ip_address = f"{random.randint(1, 256)}.{random.randint(1, 256)}.{random.randint(1, 256)}.{random.randint(1, 256)}"
        if email_address not in email_ip_map:
            email_ip_map[email_address] = []
        email_ip_map[email_address].append(ip_address)  # Store the new IP address for future reuse

    return ip_address

def generate_gclid(gclid_length):
    gclid_prefix = "Cj0KCQjwkNiLBhD0ARIsAOwAG_"
    characters = string.ascii_letters + string.digits
    gclid_id = ''.join(random.choice(characters) for i in range(gclid_length))
    gclid = gclid_prefix + gclid_id
    return gclid

def generate_fbclid():
    fbclid_prefix = "fb_"
    fbclid = fbclid_prefix + ''.join(random.choice(string.digits) for i in range(random.randint(8,12))) + "_" + ''.join(random.choice(string.digits) for i in range(random.randint(8,12)))
    return fbclid

# List of US cities
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin"]

# List of industries
industries = ["Technology", "Healthcare", "Finance", "Manufacturing", "Retail", "Education", "Government", "Non-profit"]

# List of department names
departments = ["Sales", "Marketing", "Engineering", "Finance", "Human Resources", "Customer Service", "Operations"]

# Generate data for 10000 records
with open("unresolved_data.csv", "w", newline="") as csvfile:
    fieldnames = [
        "crm_contact_id",
        "user_id",
        "full_name",
        "first_name",
        "last_name",
        "email_address",
        "phone_numbers",
        "city",
        "state",
        "zip_code",
        "country_code",
        "title",
        "company",
        "industry",
        "company_id",
        "company_size",
        "department",
        "lead_source",
        "lead_status",
        "lifecycle_stage",
        "owner",
        "last_contacted",
        "last_activity",
        "ip_address",
        "gclid",
        "fbclid",
        "device_id"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    email_user_map = {}
    email_ip_map = {}

    for i in range(10000):
        crm_contact_id = str(uuid.uuid4())[:10]
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        email_address = generate_random_email(first_name, last_name)
        phone_number = generate_random_phone_number()
        city = random.choice(cities)
        state = random.choice(["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
        zip_code = f"{random.randint(0, 99999):05d}"
        country_code = "US"

        # CEO, CFO, VP of couple of things, intern, entry-level
        title = random.choice(["CEO", "CFO", "CMO", "CRO", "VP of Finance", "VP of Sales", "VP of Revenue",  "Marketing Manager", "Business Development Representative", "Engineering Intern", "Sales Engineer Intern", "Marketing Intern", "Entry-Level Engineer"])
        company = random.choice(companies)
        industry = random.choice(industries)
        company_id = f"{random.randint(0, 99999):05d}"
        company_size = random.randint(1, 10000)
        department = random.choice(departments)
        lead_source = random.choice(['website', 'referral', 'social media', 'demo request', 'SDR outbound'])
        lead_status = random.choice(['sales discovery set', 'qualify', 'validate', 'negotiation'])
        lifecycle_stage = "prospect"
        owner = random.choice(first_names) + random.choice(last_names)
        last_contacted = generate_random_timestamp(datetime.datetime.now() - datetime.timedelta(days=730), datetime.datetime.now())
        last_activity = generate_random_timestamp(datetime.datetime.now() - datetime.timedelta(days=365), datetime.datetime.now())
        ip_address = ip_address = generate_ip_address(email_address, email_ip_map, reuse_probability=0.3)
        user_id = generate_user_id(email_address, email_user_map)
        gclid = generate_gclid(25)
        fbclid = generate_fbclid()
        device_id = str(uuid.uuid4())[:36]

        writer.writerow({
            "crm_contact_id": crm_contact_id,
            "user_id": user_id,
            "full_name": full_name,
            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "phone_numbers": phone_number,
            "city": city,
            "state": state,
            "zip_code": zip_code,
            "country_code": country_code,
            "title": title,
            "company": company,
            "industry": industry,
            "company_id": company_id,
            "company_size": company_size,
            "department": department,
            "lead_source": lead_source,
            "lead_status": lead_status,
            "lifecycle_stage": lifecycle_stage,
            "owner": owner,
            "last_contacted": last_contacted.strftime("%Y-%m-%d %H:%M:%S"),
            "last_activity": last_activity.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip_address,
            "gclid": gclid,
            "fbclid": fbclid,
            "device_id": device_id
        })







