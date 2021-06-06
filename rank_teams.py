def seed_mps(seed_results):
    team_to_scores = [el for el in seed_results if el['turns'] and el['score'] is not None]
    sorted_team_to_scores = sorted(team_to_scores, key=lambda element: (element['score'], -element['turns']))
    for i in range(len(sorted_team_to_scores)):
        if i == 0:
            # last place
            sorted_team_to_scores[i]['mp'] = 0
        elif sorted_team_to_scores[i]['score'] == sorted_team_to_scores[i - 1]['score'] and sorted_team_to_scores[i]['turns'] == sorted_team_to_scores[i - 1]['turns']:
            # tie
            j = i - 1
            sorted_team_to_scores[i]['mp'] = sorted_team_to_scores[j]['mp'] + 1
            while(sorted_team_to_scores[i]['score'] == sorted_team_to_scores[j]['score'] and sorted_team_to_scores[i]['turns'] == sorted_team_to_scores[j]['turns']):
                sorted_team_to_scores[j]['mp'] = sorted_team_to_scores[j]['mp'] + 1
                j -= 1
        else:
            sorted_team_to_scores[i]['mp'] = sorted_team_to_scores[i - 1]['mp'] + 2
    return sorted_team_to_scores
    
def mps(seed_scores):
    teams = {}
    for seed, results in seed_scores.items():
        for team_results in seed_mps(results):
            team = team_results.pop('team')
            teams.setdefault(team, {'team': team, 'seeds': {}})['seeds'][seed] = team_results
    for val in teams.values():
        val['total_mp'] = sum([v['mp'] for v in val['seeds'].values()])
    return sorted(teams.values(), key=lambda element: element['total_mp'], reverse=True)

def pretty_print(ordered_scores):
    for index, i in enumerate(ordered_scores):
        print(f"Rank: {index+1}    |   Team: {i['team']}    |   Total MP: {i['total_mp']}   |   Seed 1 MP: {i['seeds'].get('1', {}).get('mp', 0)}   |   Seed 2 MP: {i['seeds'].get('2', {}).get('mp', 0)}   |   Seed 3 MP: {i['seeds'].get('3', {}).get('mp', 0)}   |   Seed 4 MP: {i['seeds'].get('4', {}).get('mp', 0)}  ")
