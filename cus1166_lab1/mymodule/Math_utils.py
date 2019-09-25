def Average(roster):
    total = 0
    for x in roster:
        total += x.GetGrade()
    return total/len(roster)
    
