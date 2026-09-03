# Full Dependency Proof

Fix `n`, `omega`, and a field modulus. Use the valid source domains below; impossible calls are zero. The outer order is increasing vertex budget, then increasing evaporation time `t`, then increasing leaf parameter `ell`, with scalar counters at a fixed layer evaluated in increasing outside counter `k`. Within a layer, evaluate families in the order `fh5` blocks, `ft`, `f`, `g1`, `g2`/`gh`/`gt`, `g`, and finally the connected/all-graph extraction. Boundary and zero cases are returned before recursive calls.

## Family domains and edges

Write `s=x+ell`. The accelerated family has `t>=2`, `ell>=1`, `0<=z<=x`, `x+ell<=omega`, and `0<=k<=n-s`. The families `f` and `ft` have `t>=1`, `ell>=1`, `x+ell<=omega`, and `k<=n-s`; `g`, `gt`, and `gh` have `0<=z<=x`, while `g1` and `g2` have no `z` parameter. All counters have `0<=t<=n` and nonnegative counters within the remaining vertex budget.

The recursive edges are:

| Caller | Callees | Decreasing/already-computed measure |
|---|---|---|
| `fh5(t,x,z,ell,k)` | `g1(t-1,r,q)`, `gh(t-1,x+ell,z,j)`, `fh5(t,x+i,z,ell-i,j)` | `t` decreases for boundary families; interior `ell-i < ell`; all `j<=k` are solved as one block |
| `ft(t,x,ell,k)` | `fh5(t,x,x,ell,*)`, `g1(t-1,*)`, `g2(t-1,*)`, `gh(t-1,*)` | same-`ell` block already materialized; every other edge decreases `t` |
| `f(t,x,ell,k)` | `ft(t,x,ell,q)`, `g(t-2,x+ell,x,*)` | family order at same layer; `t-2` otherwise |
| `g1(t,x,k)` | `f(t,x,ell,*)` | family order |
| `g2(t,x,k)` | `g1(t,x,q)`, `g1(t,x,k-q)`, `g2(t,x,k-q)` | `g1` family order; `k-q<k` for `g2` |
| `gh(t,x,z,k)` | `g1(t,u,q)`, `gh(t,x,z,k-q)` | `g1` family order; `k-q<k` |
| `gt(t,x,z,k)` | `g1(t,u,q)`, `gt(t,x,z,k-q)` | `g1` family order; `k-q<k` |
| `g(t,x,z,k)` | `gt(t,x,z,q)`, `g(t-1,x,z,k-q)` | `gt` family order; `t-1` otherwise |
| `all_graphs(n,omega)` | `count_connected(k,omega)`, `all_graphs(n-k,omega)` | `k<n` and `n-k<n` |

The `i=0` term in `fh5` is the only same-state self-reference. The block ODE solves all its `k` coefficients simultaneously; it is not a recursive call. For `0<i<ell`, the target has leaf parameter `ell-i`; for `i=ell`, the target is the boundary `gh`/`g_p` at time `t-1`. Thus no unhandled cycle remains. The base cases at `t=0`, `t=1`, `k=0`, `x=0`, and `x+ell>omega` terminate every edge.

## Cache invariant

At the start of one fixed `(n,p,omega)` execution, the cache and memo tables are cleared. A key `(t,x,z,ell,omega)` determines `K=n-x-ell`, every `G_{r,q}`, every lower-`ell` vector, and the boundary vector. One block call computes and stores the complete vector `F_0,...,F_K`. A later request for any other admissible `k` with the same key performs only a dictionary lookup. The outer execution parameters `(n,p,omega)` scope the cache and are reset between modular runs, so a vector is never reused across incompatible truncation lengths or fields.
