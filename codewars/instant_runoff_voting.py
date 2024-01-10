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


def runoff(voters:list[list[str]]) -> str | None:
    tally = dict()
    initial = '019384489283489234759238174412434534534zx@d6344'
    available_candidates = set(initial)
    eliminated_candidates = set()
    total_votes = len(voters)
    fifty_percent = (total_votes // 2)
    winning_candidate = False
    while not winning_candidate and len(available_candidates) > 0:
        available_candidates.discard(initial)
        for voter in voters:
            for i, vote in enumerate(voter):
                if vote not in eliminated_candidates:
                    if vote in tally: tally[vote] += 1
                    else: 
                        tally[vote] = 1
                        available_candidates.add(vote)
                    break
        print(f'available candidates = {available_candidates}')
        print(f'tally.values() = {tally.values()}')
        max_value = max(tally.values())
        if max_value > fifty_percent:
            max_keys = [key for key, value in tally.items() if value == max_value]
            print(f'max keys = {max_keys}')
            return max(max_keys)
        
        min_value = min(tally.values())
        min_keys = [key for key, value in tally.items() if value == min_value]
        for candidate in min_keys:
            eliminated_candidates.add(candidate)
            del(tally[candidate])
            available_candidates.remove(candidate)
    return None