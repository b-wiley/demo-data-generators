import random
import string
from datetime import datetime, timedelta
import csv

workout_names = [
    "Full Body Strength Blast",
    "Lower Body Strength & Conditioning",
    "Upper Body Pump",
    "Core & Cardio Circuit",
    "High-Intensity Interval Training (HIIT)",
    "Yoga Flow for Flexibility",
    "Pilates for Core Strength",
    "Barre for Muscle Tone",
    "Beginner Strength Training",
    "Advanced Strength Training",
    "Metabolic Conditioning Workout",
    "Tabata Intervals",
    "Jump Rope Cardio Blast",
    "Stair Climbing Workout",
    "Animal Flow Movement Training",
    "Kickboxing Cardio",
    "Spinning Class",
    "Step Aerobics",
    "Bodyweight Strength Workout",
    "Dumbbell Strength Training",
    "Kettlebell Workout",
    "Medicine Ball Circuit",
    "Suspension Training Workout",
    "Resistance Band Workout",
    "Plyometric Workout for Power",
    "Mobility & Flexibility Routine",
    "Active Stretching & Recovery",
    "Yoga for Beginners",
    "Vinyasa Yoga Flow",
    "Yin Yoga for Stress Relief",
    "Restorative Yoga",
    "Prenatal Yoga",
    "Postnatal Yoga",
    "Pilates Mat Workout",
    "Reformer Pilates",
    "Barre for Glutes & Legs",
    "Barre for Arms & Core",
    "Bootcamp Workout",
    "Circuit Training",
    "Sports Conditioning Workout",
    "Injury Prevention Workout",
    "Functional Fitness Training",
    "Mind-Body Workout",
    "Dance Fitness Class",
    "Zumba",
    "Cardio Kickboxing",
    "Booty Sculpt Workout",
    "Abs & Core Workout",
    "Arm Workout",
    "Back & Shoulder Workout",
    "Chest & Tricep Workout",
    "Leg & Glute Workout",
    "Full Body Stretch & Cool Down"
]




def generate_workout_event_id(used_ids):
    """Generates a unique workout event ID"""
    while True:
        event_id = random.randint(1000000, 2000000)  # Adjust max ID range as needed
        if event_id not in used_ids:
            return event_id

def generate_workout_event_timestamp():
    """Generates a random workout event timestamp within the last 30 days in ISO 8601 format"""
    base_date = datetime.now() - timedelta(days=30)
    random_delta = timedelta(days=random.randint(0, 30))
    event_timestamp = base_date + random_delta
    return event_timestamp.isoformat(timespec='milliseconds') + '+0000'  # Add milliseconds and offset

def generate_workout_event(used_event_ids):
    """Generates a dictionary representing a workout event with unique ID"""
    event_id = generate_workout_event_id(used_event_ids)
    used_event_ids.add(event_id)
    member_id = random.randint(9000, 20000)  # Replace with your member ID generation logic
    event_type = random.choice(["content_workout_started", "content_workout_completed"])
    timestamp = generate_workout_event_timestamp()
    content_id = random.randint(500, 1000)  # Replace with your content ID generation logic
    coached_or_self_guided = random.choice(["coached", "self guided"])
    workout_name = random.choice(workout_names)
    workout_target = random.choice(["Glutes", "Biceps", "Quads", "Triceps", "Core", "Chest"])
    workout_style = random.choice(["Boxing", "Strength Training", "Yoga"])

    return {
        "workout_event_id": event_id,
        "member_id": member_id,
        "event_name": event_type,
        "timestamp": timestamp,
        "content_id": content_id,
        "workout_coached_or_self_guided": coached_or_self_guided,
        "workout_name": workout_name,
        "workout_target": workout_target,
        "workout_style": workout_style
    }

def generate_dataset(num_events):
    """Generates a list of workout event dictionaries"""
    dataset = []
    used_event_ids = set()
    for _ in range(num_events):
        dataset.append(generate_workout_event(used_event_ids))
    return dataset

# Generate 1000 workout events
data = generate_dataset(61200)

# Save the data to a CSV file
with open("centr_app_workout_events.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())  # Use fieldnames from first event
    writer.writeheader()
    writer.writerows(data)

print("Dataset generation and export complete!")
