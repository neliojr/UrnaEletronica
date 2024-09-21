from candidate import CandidateManager
from role import Role
from voter import Voter

# checar se o db existe:


manager = CandidateManager()
manager.load_candidates('./data/database.json')
manager.display()
manager.add_vote("Presidente", 45)