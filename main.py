from candidate import CandidateManager
from role import Role
from voter import Voter

# checar se os dbs existem:


manager = CandidateManager()
manager.load_candidates('./data/candidates.json')
manager.display()
manager.add_vote("Presidente", 45)