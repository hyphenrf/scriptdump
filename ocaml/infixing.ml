(* Binary operators that emulate Haskell's backtick infixing 
 *
 * Things to note:
 *   - OCaml's operator fixity and precedence is defined by the first 
 *     (or first few) characters of the operator.
 *   - (<...) defines an operator of low (same as comparison) precedence
 *   - (%...) defines an operator of high (same as division) precedence
 *   - We try to preserve aesthetic symmetry.
 *   - Thus, <%fn%> seems like a verbose but adequate solution. *)

let (<%) = (|>)
let (%>) = Fun.flip

let sub = Int.sub

let _ =
  (* expected evaluation order: *)
  assert (3 <%sub%> 1 = ((|>) 3 ((Fun.flip sub) 1)));
  assert (3 <%sub%> 1 = 2)

(* This doesn't need to be the case though, as one doesn't need to use
 * `Fun.flip` to get the desired effect: *)
let ( /* ) = (|>)
let ( */ ) = (@@)

let _ =
  assert (3 /*sub*/ 1 = 2)
