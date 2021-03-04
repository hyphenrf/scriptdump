(*
   Haskell's applicative solution for palindromic lists goes like this:
   palindrome = (==) <*> reverse
   in which <*> :: ([a] -> [a] -> Bool) -> ([a] -> [a]) -> [a] -> Bool

   or the more general type:
      (a -> b -> c) -> (a -> b) -> a -> c

   This type is possible thanks to Haskell's type-instance Applicative ((->) r)
   in which arrows are treated as constructors. We'll have to make our own here
   probably...

   this file's job is to find a way in ocaml to equate
      (a -> b -> c) -> (a -> b) -> a -> c
   to
      Applicative p => p (x -> y) -> p x -> p y
*)

module type Applicative = sig
  type 'x t
  val pure    : 'a -> 'a t
  val ( <*> ) : ('a -> 'b) t -> 'a t -> 'b t
  (*
  val liftA2  : ('a -> 'b -> 'c) -> 'a t -> 'b t -> 'c t
  val ( *> )  : 'a t -> 'b t -> 'b t
  val ( <* )  : 'a t -> 'b t -> 'a t
  *)
end

(*
   first let's try and morph the arrows in the second form to mimic the first form

   (a -> (b -> c)) -> (a -> b) -> (a -> c)
   x t = (a -> x)
   (b -> c) t -> b t -> c t                  (* looks correct *)

   so what we need is a type function that takes x t and returns (a -> x) t
   but how do we express this in ocaml? where would x t = (a -> x) fit?

   comes second, ocaml's type system wrestling...
*)

module Arrow (M: sig type r end)
= struct
  type r = M.r
  type 'x t = T:(r -> 'x) -> 'x t
  let pure x = T (fun _ -> x)
  let (<*>) = fun (T( f: r -> ('a -> 'b) ))
                  (T( g: r -> 'a         )) ->
    T(fun (x: r) -> f x (g x))
end

let palindrome (type a) (xs: a list) =
  let module AppArrow = Arrow (struct type r = a list end) in
  (* let module AppArrow: Applicative with type 'x t = 'x AppArrow.t = AppArrow in *)
  (* look I made it work and the sigs match but can't convince the type checker it implements Applicative. *)
  let open   AppArrow in
  let (=) = T (=) in
  let rev = T List.rev in
      (=) <*> rev |> fun (T f) -> f xs

let () = ()
  ; Printf.printf "%b\n" (palindrome ['m';'o';'m'])
  ; Printf.printf "%b\n" (palindrome [1;2;3])
  ; Printf.printf "%b\n" (palindrome [1])
  ; Printf.printf "%b\n" (palindrome [])

