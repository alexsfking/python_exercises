'''
### kyu 4 ###
Your task is to implement a function that calculates an election winner from a
list of voter selections using an Instant Runoff Voting algorithm. If you
haven't heard of IRV, here's a basic overview (slightly altered for this kata):

    Each voter selects several candidates in order of preference.
    The votes are tallied from the each voter's first choice.
    If the first-place candidate has more than half the total votes, they win.
    Otherwise, find the candidate who got the least votes and remove them from each
    person's voting list.
    In case of a tie for least, remove all of the tying candidates.
    In case of a complete tie between every candidate, return
    nil(Ruby)/None(Python)/undefined(JS).
    Start over.
    Continue until somebody has more than half the votes; they are the winner.
    Your function will be given a list of voter ballots; each ballot will be a list
    of candidates (symbols) in descending order of preference. You should return the
    symbol corresponding to the winning candidate. See the default test for an
    example!
'''


class Election:
    def __init__(self, voters:list[list[str]]) -> None:
        self.voters: list[list[str]] = voters
        self.tally: dict[str, int] = {}
        self.available_candidates: set[str] = set()
        self.total_votes: int = len(voters)
        self.fifty_percent: int = self.total_votes // 2

    def begin(self) -> str | None:
        self.initial_count()
        winner = self.get_winner()
        if(winner): return winner
        self.eliminate_candidates()
        while len(self.available_candidates) > 0:
            self.count_votes()
            winner = self.get_winner()
            if(winner): return winner
            self.eliminate_candidates()
        return None

    def initial_count(self):
        for voter in self.voters:
            for vote in voter:
                if vote in self.tally: self.tally[vote] += 1
                else: 
                    self.tally[vote] = 1
                    self.available_candidates.add(vote)
                break

    def get_winner(self) -> str | None:
        max_value = max(self.tally.values())
        if max_value > self.fifty_percent:
            max_keys = [key for key, value in self.tally.items() if value == max_value]
            return max(max_keys)
        return None
    
    def eliminate_candidates(self):
        min_value = min(self.tally.values())
        min_keys = [key for key, value in self.tally.items() if value == min_value]
        for candidate in min_keys:
            self.available_candidates.remove(candidate)

    def count_votes(self):
        self.tally = dict()
        for voter in self.voters:
            for vote in voter:
                if vote in self.available_candidates:
                    if vote in self.tally: self.tally[vote] += 1
                    else: self.tally[vote] = 1
                    break

def runoff(voters:list[list[str]]) -> str | None:
    election = Election(voters)
    return election.begin()


tests = []
tests.append([['Daisuke Aramaki', 'Lex Luthor', 'Abelt Dessler', 'Johan Liebert', 'Reinhard von Musel', 'Gihren Zabi'], ['Johan Liebert', 'Reinhard von Musel', 'Gihren Zabi', 'Daisuke Aramaki', 'Lex Luthor', 'Abelt Dessler'], ['Reinhard von Musel', 'Lex Luthor', 'Abelt Dessler', 'Daisuke Aramaki', 'Johan Liebert', 'Gihren Zabi'], ['Abelt Dessler', 'Daisuke Aramaki', 'Gihren Zabi', 'Lex Luthor', 'Johan Liebert', 'Reinhard von Musel'], ['Abelt Dessler', 'Johan Liebert', 'Gihren Zabi', 'Lex Luthor', 'Daisuke Aramaki', 'Reinhard von Musel'], ['Johan Liebert', 'Gihren Zabi', 'Daisuke Aramaki', 'Reinhard von Musel', 'Abelt Dessler', 'Lex Luthor']])
#tests.append([['Drake Luft', 'Reinhard von Musel', 'Johan Liebert', 'Brian J. Mason', 'Daisuke Aramaki', 'Abelt Dessler'], ['Reinhard von Musel', 'Drake Luft', 'Daisuke Aramaki', 'Johan Liebert', 'Abelt Dessler', 'Brian J. Mason'], ['Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Daisuke Aramaki', 'Reinhard von Musel', 'Abelt Dessler'], ['Reinhard von Musel', 'Brian J. Mason', 'Drake Luft', 'Daisuke Aramaki', 'Johan Liebert', 'Abelt Dessler'], ['Daisuke Aramaki', 'Abelt Dessler', 'Drake Luft', 'Reinhard von Musel', 'Johan Liebert', 'Brian J. Mason'], ['Drake Luft', 'Brian J. Mason', 'Reinhard von Musel', 'Johan Liebert', 'Abelt Dessler', 'Daisuke Aramaki']])
for test in tests:
    print(runoff(test))