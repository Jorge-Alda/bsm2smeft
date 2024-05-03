from wilson import Wilson

def combine_Wilson(w1: Wilson, w2: Wilson) -> Wilson:
    '''
    Combines two Wilson objects into one defined at the lowes energy scale.
    '''
    if w1.wc.scale < w2.wc.scale:
        w1run = w1.wc
        scale = w1.wc.scale
        w2run = w2.match_run(scale = scale, eft='SMEFT', basis='Warsaw')
    elif w1.wc.scale > w2.wc.scale:
        w2run = w2.wc
        scale = w2.wc.scale
        w1run = w1.match_run(scale = scale, eft='SMEFT', basis='Warsaw')
    else:
        w1run = w1.wc
        w2run = w2.wc
        scale = w2.wc.scale
    coeffs = {c: 0 for c in w1run.values.keys() | w2run.values.keys()}
    for w in [w1run, w2run]:
        for k, v in w.values.items():
            if isinstance(v, float):
                coeffs[k] += w.values[k]
            else:
                coeffs[k] += w.values[k]['Re'] + 1j*w.values[k]['Im']
    return Wilson(coeffs, scale=scale, eft='SMEFT', basis='Warsaw')