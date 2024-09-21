import json

class Candidate:
    def __init__(self, name, number, role, votes):
        self.name = name
        self.number = number
        self.role = role
        self.votes = votes

class CandidateManager:
    def __init__(self):
        self.candidates = []

    def load_candidates(self, database):
        with open(database, 'r') as file:
            data = json.load(file)
            for item in data['candidates']:
                candidate = Candidate(item['name'], item['number'], item["role"], item["votes"])
                self.candidates.append(candidate)
    
    def display(self):
        for candidate in self.candidates:
            print(f'{candidate.name} - {candidate.number}')
    
    def add_vote(self, role, number):
        for candidate in self.candidates:
            if candidate.role == role and candidate.number == number:
                candidate.votes += 1
                self.save_candidates('./data/database.json')

    def save_candidates(self, database):
        data = {'candidates': []}
        for candidate in self.candidates:
            data['candidates'].append({
                'name': candidate.name,
                'number': candidate.number,
                'role': candidate.role,
                'votes': candidate.votes
            })
        with open(database, 'w') as file:
            json.dump(data, file, indent=4)
    
    def create_candidate(self, name, number, role):
        new_candidate = Candidate(name, number, role, 0)
        self.candidates.append(new_candidate)
        self.save_candidates('./data/database.json')