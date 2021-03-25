(* Variadic functions challenge:
 * https://blog.janestreet.com/variable-argument-functions/
 * ehh.. technically type-indexed lol *)

module Challenge_1 = struct
type _ n =
  | A: ('a n -> 'a) n
  | Z: int n

let a = A
let z = Z

let f x =
  let rec aux: type a. int -> a n -> a =
    fun i ->
    function Z -> i
           | A -> aux (succ i)
  in aux 0 x

let () =
  assert (f z = 0);
  assert (f a z = 1);
  assert (f a a z = 2);
  assert (f a a a z = 3);
end

module Challenge_2 = struct
type _ n =
  | A: int -> ('a n -> 'a) n
  | Z: int n

let a = fun x -> A x
let z = Z

let f x =
  let rec aux: type a. int -> a n -> a =
    fun i ->
    function Z -> i
           | A n -> aux (i+n)
  in aux 0 x
  
let () =
  assert (f z = 0);
  assert (f (a 1) (a 2) (a 3) z = 6);
end

module Challenge_3 = struct
type _ n =
  | A: (int -> 'a n -> 'a) n
  | Z: int n

let a = A
let z = Z

let f x =
  let rec aux: type a. int -> a n -> a =
    fun i ->
    function Z -> i
           | A -> fun n -> aux (i+n)
  in aux 0 x
  
let () =
  assert (f z = 0);
  assert (f a 1 a 2 a 3 z = 1 + 2 + 3);
end

