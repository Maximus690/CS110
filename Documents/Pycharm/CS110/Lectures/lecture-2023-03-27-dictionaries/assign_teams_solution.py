def assign_teams(participants, age_groups):
    """Return a list of (person, team) tuples"""
    teams = []
    for name, age in participants:
        # Find the age group (round down to nearest x3)
        age_group = (age // 3) * 3
        
        # Look up the team name
        if age_group in age_groups:
            your_team = age_groups[age_group]
        else:
            your_team = 'Adult League'
        teams.append((name, your_team))
    return teams


def print_teams(teams):
    for player, team in teams:
        print(f'{player} is on team {team}')


def main(participants, age_groups):
    teams = assign_teams(participants, age_groups)
    print_teams(teams)
    
    
if __name__ == '__main__':
    age_groups = {
        0: 'Team Toddlers',
        3: 'Tiny Troupers',
        6: 'Starting Stars',
        9: 'Mighty Middles',
        12: 'Too Cool',
        15: 'Boundless'
    }

    participants = [
        ('Joe', 14),
        ('Jane', 6),
        ('Johnny', 4),
        ('Jennifer', 20),
        ('Jack', 16),
        ('Janice', 2)
    ]

    main(participants, age_groups)
    
