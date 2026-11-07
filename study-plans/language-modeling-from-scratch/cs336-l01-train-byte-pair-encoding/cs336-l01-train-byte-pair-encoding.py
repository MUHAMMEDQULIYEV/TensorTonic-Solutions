from collections import Counter

def merge(seq,pair,vocab_size):
    i=0
    new_list=[]
    while i<len(seq):
        if i<len(seq)-1 and (seq[i], seq[i+1]) == pair:
                new_list.append(vocab_size)
                i+=2
        else:
                new_list.append(seq[i])
                i+=1
    return new_list

def get_stats(ids):
    counts=Counter()
    for seq in ids:
        counts.update(zip(seq, seq[1:]))    
    return counts
        
    
def train_bpe(corpus: list[str], vocab_size: int) -> dict:
    """
    Returns a dictionary of learned vocab entries and ordered merges.
    """
    ids=[]
    vocab=[]
    merges=[]
    token_bytes = {b: [b] for b in range(256)}
    for text in corpus:
        ids.append(list(text.encode()))

    for i in range(256,vocab_size):
        k=get_stats(ids)
        if not k:
            break
        pair = max(k, key=lambda p: (k[p], token_bytes[p[0]], token_bytes[p[1]]))
        
        for j in range(len(ids)):
            ids[j] = merge(ids[j], pair, i)
        a, b = pair
        token_bytes[i] = token_bytes[a] + token_bytes[b]
        merges.append([a, b, i])
        vocab.append([i, token_bytes[i]])
    return {"vocab":vocab,"merges":merges}
        
