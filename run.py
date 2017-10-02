#!/usr/bin/env python3

import multiprocessing
from joblib import Parallel, delayed
from itertools import product

def toad_move(s):
    rs = set()
    for i in range(0, len(s)-1):
        if s[i] == 'T' and s[i+1] == ' ':
            ns = list(s)
            ns[i] = ' '
            ns[i+1] = 'T'
            rs.add(''.join(ns))
    return rs

def toad_hops(s):
    rs = set()
    for i in range(0, len(s)-2):
        if s[i] == 'T' and s[i+1] == 'F' and s[i+2] == ' ':
            ns = list(s)
            ns[i] = ' '
            ns[i+2] = 'T'
            rs.add(''.join(ns))
    return rs

def toad_all(s):
    return toad_move(s).union(toad_hops(s))

def frog_move(s):
    rs = set()
    for i in range(1, len(s)):
        if s[i] == 'F' and s[i-1] == ' ':
            ns = list(s)
            ns[i] = ' '
            ns[i-1] = 'F'
            rs.add(''.join(ns))
    return rs

def frog_hops(s):
    rs = set()
    for i in range(2, len(s)):
        if s[i] == 'F' and s[i-1] == 'T' and s[i-2] == ' ':
            ns = list(s)
            ns[i] = ' '
            ns[i-2] = 'F'
            rs.add(''.join(ns))
    return rs

def frog_all(s):
    return frog_move(s).union(frog_hops(s))

def game_graph(s):
    graph = {}
    q = [(s, 0, 0)]

    while len(q) > 0:
        ss = q.pop()
        if ss in graph:
            continue
        if ss[1] == 0:
            ne = toad_all(ss[0])
            graph[ss] = set()
            for e in ne:
                graph[ss].add((e, 1, ss[2]+1))
                q.append((e, 1, ss[2]+1))
        elif ss[1] == 1:
            ne = frog_all(ss[0])
            graph[ss] = set()
            for e in ne:
                graph[ss].add((e, 0, ss[2]+1))
                q.append((e, 0, ss[2]+1))
    return graph

def graph_query(g, s):
    for k in g:
        if k[0] == s:
            return g[k]
    return None

def graph_find(g, s):
    for k in g:
        if k[0] == s:
            return k
    return None

def graph_parent(g, s):
    for k in g:
        if s in g[k]:
            return k
    return None

def t_not(p):
    if p == 0:
        return 1
    return 0

def winners(g, s):
    assert(graph_find(g, s) != None)
    w = set()
    q = [graph_find(g, s)]
    while len(q) > 0:
        g_e = q.pop()
        rs = g[g_e]
        if len(rs) == 0:
            w.add(t_not(g_e[1]))
        else:
            for r in rs:
                q.append(r)
    return w

def all_winners(g, s):
    assert(graph_find(g, s) != None)
    w = []
    q = [graph_find(g, s)]
    while len(q) > 0:
        g_e = q.pop()
        rs = g[g_e]
        if len(rs) == 0:
            w.append(t_not(g_e[1]))
        else:
            for r in rs:
                q.append(r)
    return [w.count(0), w.count(1)]

def p_w(e):
    s = ''.join(e)
    w = winners(game_graph(s), s)
    if len(w) == 1 and 0 in w:
        return 0
    elif len(w) == 1 and 1 in w:
        return 1
    else:
        return 2

def p_a_w(e):
    s = ''.join(e)
    r = all_winners(game_graph(s), s)
    sm = r[0] + r[1]
    return [r[0]/sm, r[1]/sm]

def p_w_l(l):
    r = []
    for i in range(0, l):
        r.append(['T', 'F', ' '])
    ps = [0, 0, 0]
    results = Parallel(n_jobs=4)(delayed(p_w)(e) for e in product(*r))
    ps[0] = results.count(0)
    ps[1] = results.count(1)
    ps[2] = results.count(2)
    return ps

def p_s_l(l, g):
    r = []
    for i in range(0, l):
        r.append(['T', 'F', ' '])
    ps = [0, 0, 0]
    rs = set()
    for e in product(*r):
        if p_w(e) == g:
            rs.add(''.join(e))
    return rs

def p_win(l):
    r = []
    for i in range(0, l):
        r.append(['T', 'F', ' '])
    ps = [0, 0]
    c = 0
    results = Parallel(n_jobs=4)(delayed(p_a_w)(e) for e in product(*r))
    for r in results:
        c += 1
        ps[0] += r[0]
        ps[1] += r[1]
    return [ps[0]/c, ps[1]/c]

def p_fair(l):
    r = []
    for i in range(0, l):
        r.append(['T', 'F', ' '])
    rs = set()
    for e in product(*r):
        r = p_a_w(e)
        if abs(0.5 - r[0]) < 1E-10:
            rs.add(''.join(e))
    return rs


def p_thrm(l):
    ce = set()
    for i in range(1, 9):
        a = p_s_l(i, 2)
        b = p_s_l(i+1, 2)
        for e in a:
            if (e+"T" not in b) and ("F"+e not in b):
                print("[" + e + "] not in " + str(i+1))
                ce.add(e)
    return ce
