# %%
def segLengths(S1: float, S2: float, L: float, divCoeff = 2):
    """
    Returns a list of segmenth lengths that fit a space of length L. The first segment will have the smallest length (but bigger than S1), while the last segment will have the biggest length of the list (but smaller than S2). 

    Parameters
    ----------
    S1 : float
        Length of the left segment.

    S2 : float
        Length of the right segment. 

    L : float
        Length of the segment to be filled. 

    Returns 
    ----------
    segments : list 
        List contians the lengths of the segments from left to right, whose total lengths add up to L. 

    Other parameters
    ----------
    divCoeff : float, optional
        Coefficient used to divide S1 by, in case the algorithm does not find a suitable number of segments.
    
    Notes
    ----------
    The number of segments must be smaller than uppBound for the algorithm to work. Otherwise, alpha is negative and the lengths of the segments will all be smaller than S1 and S2. 

    The number of segments must be bigger than lowbound for the algorithm to work. Otherwise, the biggest segment will have a length larger than the largest of S1 and S2. We choose numSeg as the ceiling of lowBound to make sure this condition is met. 

    The algorithm always 

    Raises
    ----------
    valueError
        Both elements lengths should be positive numbers 
    """
    from math import ceil 

    sLow = min(S1, S2)
    sHigh = max(S1, S2)
    if sLow <= 0 or sHigh <= 0:
        raise ValueError('Verify that the elements lengths are positive.')
    
    uppBound = L/sLow #Upper bound on the number of segments
    lowBound = (2*L - sHigh + sLow)/(sHigh+sLow) #Lower bound on the number of segments
    numSeg = max(1, ceil(lowBound)) #Initial guess for the number of segments, must be at least 1 for the algorithm to functi
    segments = []

    if numSeg > uppBound:
        # In this case, the algorithm is restarted with a smaller sLow
        # The new sLow value is determined by divCoeff, typically divCoeff=2
        segments = segLengths(sLow/divCoeff, sHigh, L)
    else:
        if sHigh == sLow:
            alpha = 0
        else:
            alpha = (2*(L-numSeg*sLow))/(numSeg*(numSeg+1)*(sHigh-sLow))
        for i in range(1,numSeg+1):
            l = alpha*i 
            lSeg = (sHigh - sLow)*l + sLow 
            segments.append(lSeg)
    if sLow == S2: #If S2<S1, then the order of the element lengths needs to be reversed
        segments = list(reversed(segments))
    return segments
# %%
