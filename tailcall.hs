-- Simple tail-call optimisation does not work in a lazy-evaluated lang like
-- haskell. Laziness can be extrememly efficient but recursive thunks are just
-- as bad if not worse than recursive stack frames:
-- https://stackoverflow.com/questions/13042353/does-haskell-have-tail-recursive-optimization

fac n = fac' n 1 where
	fac' 0 acc = acc
	fac' n acc = fac' (n-1) $! (n*acc)

-- Another way (i think doesn't wotk with hugs):

-- fac2 n = fac' n 1 where
-- 	fac' 0 acc = acc
-- 	fac' n !acc = fac' (n-1) (n*acc)


-- The ! operator enforces strictness for arguments
-- whereas fn' is a strict fn..
-- With GHC you can forego strictness notation if you compile with -O3 or -O2
-- or even -O as it does strictness analysis for you.
