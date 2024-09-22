from candidate import CandidateManager
from role import RoleManager
from voter import VoterManager

candidate_manager = CandidateManager()
role_manager = RoleManager()
voter_manager = VoterManager()

#role_manager.create('Presidente', 2, True)
#candidate_manager.create('op0', 10, 'Presidente')
voter_manager.create('Nelio', 32)
#print(voter_manager.find(1))
#voter_manager.update('nelio junior', 32)