import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['cricket_management']

players_collection = db['players']
teams_collection = db['teams']
matches_collection = db['matches']

# Streamlit app
st.title("Cricket Management System")

# Navigation menu
menu = ["Home", "Add Player", "Add Team", "Add Match", "View Players", "View Teams", "View Matches"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Cricket Management System")
    st.write("This system helps manage teams, players, and match details.")

# Add Player
elif choice == "Add Player":
    st.subheader("Add a New Player")
    player_name = st.text_input("Player Name")
    age = st.number_input("Age", min_value=10, max_value=60)
    team = st.text_input("Team")
    role = st.selectbox("Role", ["Batsman", "Bowler", "All-Rounder", "Wicketkeeper"])
    matches = st.number_input("Matches Played", min_value=0)
    runs = st.number_input("Total Runs", min_value=0)
    wickets = st.number_input("Total Wickets", min_value=0)

    if st.button("Add Player"):
        if player_name and team:
            players_collection.insert_one({
                "name": player_name,
                "age": age,
                "team": team,
                "role": role,
                "matches": matches,
                "runs": runs,
                "wickets": wickets
            })
            st.success(f"Player {player_name} added successfully!")
        else:
            st.error("Please fill all the fields")

# Add Team
elif choice == "Add Team":
    st.subheader("Add a New Team")
    team_name = st.text_input("Team Name")
    captain = st.text_input("Captain Name")
    coach = st.text_input("Coach Name")

    if st.button("Add Team"):
        if team_name and captain and coach:
            teams_collection.insert_one({
                "team_name": team_name,
                "captain": captain,
                "coach": coach
            })
            st.success(f"Team {team_name} added successfully!")
        else:
            st.error("Please fill all the fields")

# Add Match
elif choice == "Add Match":
    st.subheader("Add a New Match")
    match_id = st.text_input("Match ID")
    team1 = st.text_input("Team 1")
    team2 = st.text_input("Team 2")
    date = st.date_input("Date")
    venue = st.text_input("Venue")
    team1_score = st.number_input("Team 1 Score", min_value=0)
    team2_score = st.number_input("Team 2 Score", min_value=0)
    result = st.text_input("Result")

    if st.button("Add Match"):
        if match_id and team1 and team2:
            matches_collection.insert_one({
                "match_id": match_id,
                "team1": team1,
                "team2": team2,
                "date": date.strftime('%Y-%m-%d'),
                "venue": venue,
                "team1_score": team1_score,
                "team2_score": team2_score,
                "result": result
            })
            st.success(f"Match {match_id} added successfully!")
        else:
            st.error("Please fill all the fields")

# View Players
elif choice == "View Players":
    st.subheader("Players List")
    players = players_collection.find()
    for player in players:
        st.write(f"Name: {player['name']}, Age: {player['age']}, Team: {player['team']}, "
                 f"Role: {player['role']}, Matches: {player['matches']}, Runs: {player['runs']}, "
                 f"Wickets: {player['wickets']}")

# View Teams
elif choice == "View Teams":
    st.subheader("Teams List")
    teams = teams_collection.find()
    for team in teams:
        st.write(f"Team: {team['team_name']}, Captain: {team['captain']}, Coach: {team['coach']}")

# View Matches
elif choice == "View Matches":
    st.subheader("Matches List")
    matches = matches_collection.find()
    for match in matches:
        st.write(f"Match ID: {match['match_id']}, {match['team1']} vs {match['team2']}, "
                 f"Date: {match['date']}, Venue: {match['venue']}, "
                 f"Result: {match['result']}")

