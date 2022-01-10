# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query

from collections import OrderedDict

def solution(S, P, Q):
    results = []
    impact_factors = OrderedDict([(letter,factor+1) for factor, letter in enumerate(['A','C','G','T'])])
    for i,j in zip(P,Q):
        for letter, factor in impact_factors.items():
            if letter in  S[i:j+1]:
                results.append(factor)
                break
            
    return results

