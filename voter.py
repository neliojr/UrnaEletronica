import json

class Voter:
    def __init__(self, voter_id, name, section, voted):
        self.voter_id = voter_id
        self.name = name
        self.section = section
        self.voted = voted

class VoterManager:
    def __init__(self):
        self.voters = []
        self.database = './data/voters.json'
        self.load()

    # carregar eleitores para a RAM.
    def load(self):
        try:
            with open(self.database, 'r') as file:
                data = json.load(file)

                for item in data['voters']:
                    voter = Voter(item['voter_id'], item['name'], item["section"], item["voted"])
                    self.voters.append(voter)
        except: # criando arquio JSON caso não exista.
            data = {
                "voters": []
            }

            with open(self.database, 'w') as file:
                json.dump(data, file, indent=4)
    
    # salvar eleitores na database.
    def save(self):
        data = {'voters': []}

        for voter in self.voters:
            data['voters'].append({
                'voter_id': voter.voter_id,
                'name': voter.name,
                'section': voter.section,
                'voted': voter.voted
            })

        with open(self.database, 'w') as file:
            json.dump(data, file, indent=4)
    
    # exibir eleitores.
    def display(self):
        return [
            {
                'voter_id': voter.voter_id,
                'name': voter.name,
                'section': voter.section,
                'voted': voter.voted
            }
            for voter in self.voters
        ]
    
    # criar eleitor.
    def create(self, voter_id, name, section):
        for voter in self.voters:
            if voter.voter_id == voter_id:
                return 'voter_id already registered'
            
        new_voter = Voter(voter_id, name, section, False)
        self.voters.append(new_voter)
        self.save()
    
    # remover eleitor.
    def remove(self, voter_id):
        self.voters = [
            voter for voter in self.voters
            if not (voter.voter_id == voter_id)
        ]
        self.save()