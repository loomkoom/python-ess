def seq_sum(seq):
    """
    Returns the sum of the elements of a given sequence.
    """
    i = 0
    partial_sum = 0
    while i < len(seq):
        # INVARIANT: partial_sum is equal to the sum of the elements in seq[:i]
        assert partial_sum == sum(seq[:i])
        partial_sum += seq[i]
        i += 1
    return partial_sum


assert seq_sum([1, 5, -1]) == 5
assert seq_sum([]) == 0
assert seq_sum([10]) == 10
## CORRECTNESS

# BASE CASE
# Given: i = 0; partial_sum = 0
# To prove: partialsum = seq[:i]

# 0=0
# 0 is de som van de eerste 0 elementen

# INDUCTION STEP
# assume partialsum0 = seq[:i0]
# Given:
# To prove: partialsum = seq[:i]

# partialsum0 + seq[i] = seq[:i0+1]
# seq[:i0] + seq[i] = seq[:i0+1]
# seq[:i0] + seq[i] = seq[:i0] + seq[i]


# EPILOGUE
# Given: ...
# To prove: ...


### CORRECTNESS
'''
##BASE CASE
    # Given:
      i == 0
      partial_sum == 0
    # To prove: 
      partial_sum is equal to the sum of the elements in seq[:i]
    # Proof:
      i==0 
      => the sum of seq[:i] should be equal to the elements in seq[:0].
      0 elements in seq[:0] 
      => sum(seq[:0]) == 0 == partial_sum == 0
      is satisfied in a trivial way

## INDUCTION STEP
      Let's denote the invariant with the following assertion:
      partial_sum == Σ(0, i), where Σ(0,i) = seq[0] + seq[0+1] + ... + seq[i-1]
    # Given: 
      The given invariant is satisfied at the beginning of the loop body,
      i.e.: partial_sum0 == Σ(0, i0)
      0 denotes that this is the value at the beginning of the body
    # To prove: 
      The given invariant is satisfied at the end of the loop body,
      i.e. partial_sum == Σ(0, i)
    # Proof:
       i = i0 + 1
       partial_sum == partial_sum0 + seq[i0]
       partial_sum == partial_sum0 + seq[i0]
       partial_sum ==  Σ(0, i0 + 1 )
       partial_sum ==   Σ(0, i )

## Epilogue
    # Given:
      partial_sum == Σ(0, i )
      i == len(k)
    # To prove:
      partial_sum == Σ(0, len(k) )
    # Proof:
      partial_sum == Σ(0, i )
      <=> partial_sum == Σ(0, len(k) )      # i == len(k) is given by the ending loop condition
'''