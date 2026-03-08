#!/usr/bin/env python3

print("=== Game Analytics Dashboard ===")

users = [
    {"name": "mtaheri", "score": 4200, "active": True, "location": "k1m02s01"},
    {"name": "ybarut", "score": 3900, "active": True, "location": "k1m03s02"},
    {"name": "aldinc", "score": 3700, "active": True, "location": "k1m05s03"},
    {"name": "miskirik", "score": 9900, "active": False, "location": "SR"},
]

achievements = [
    {"name": "mtaheri", "title": "Bonus Hunter 2"},
    {"name": "mtaheri", "title": "Perfectionist 1"},
    {"name": "ybarut", "title": "Happy 42nd Day!"},
    {"name": "ybarut", "title": "I have no idea what I'm doing"},
    {"name": "aldinc", "title": "I'm reliable !"},
    {"name": "miskirik", "title": "It's a rich man's world 999"},
    {"name": "miskirik", "title": "Campus Hero"},
]

achievements_by_user = {
    user["name"]: [
        achievement["title"]
        for achievement in achievements
        if achievement["name"] == user["name"]
    ]
    for user in users
}

print("\n=== List Comprehension Examples ===")
high_scorers = [user["name"] for user in users if user["score"] > 4000]
scores_doubled = [user["score"] * 2 for user in users]
active_users = [user["name"] for user in users if user["active"]]
long_achievement_names = [
    achievement["title"] for achievement in achievements
    if len(achievement["title"]) > 15]
print("High scorers (>4000):", high_scorers)
print("Scores doubled:", scores_doubled)
print("Active users:", active_users)
print("Long achievement names:", long_achievement_names)

print("\n=== Dict Comprehension Examples ===")
user_scores = {user["name"]: user["score"] for user in users}
score_categories = {
    "high": len([user for user in users if user["score"] > 5000]),
    "medium": len([user for user in users
                   if 3800 <= user["score"] <= 5000]),
    "low": len([user for user in users if user["score"] < 3800])}
achievement_counts = {
    user["name"]: len(achievements_by_user.get(user["name"], []))
    for user in users
}
first_achievement_by_user = {}
for user in users:
    user_name = user["name"]
    titles = achievements_by_user.get(user_name, [])
    if titles:
        first_achievement_by_user[user_name] = titles[0]
print("user scores:", user_scores)
print("Score categories:", score_categories)
print("Achievement counts:", achievement_counts)
print("First achievement by user:", first_achievement_by_user)

print("\n=== Set Comprehension Examples ===")
unique_users = {user["name"] for user in users}
unique_achievements = {achievement["title"] for achievement in achievements}
active_locations = {user["location"] for user in users
                    if user["active"]}
print("Unique users:", unique_users)
print("Unique achievements:", unique_achievements)
print("Active locations:", active_locations)

print("\n=== Combined Analysis ===")
total_users = len(users)
total_unique_achievements = len(unique_achievements)
average_score = sum(user["score"] for user in users) / len(users)
print("Total users:", total_users)
print("Total unique achievements:", total_unique_achievements)
print(f"Average score: {average_score:g}")
top_score = max(user["score"] for user in users)
top_name = next(user["name"] for user in users
                if user["score"] == top_score)
top_achievement_count = len(achievements_by_user.get(top_name, []))
print(
    "Top user:",
    f"{top_name} ({top_score} points, {top_achievement_count} achievements)",
)
