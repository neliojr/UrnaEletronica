from candidate import CandidateManager
from role import RoleManager
from voter import VoterManager

candidate_manager = CandidateManager()
role_manager = RoleManager()
voter_manager = VoterManager()

print(candidate_manager.add_vote(961307, 'Presidente', 22))