(* ocamlopt -O3 -unbox-closures -unsafe -o bench cps.ml *)

(* Normal Ackermann function as per math definition *)
let rec ack1 m n = match m, n with
  | 0, n -> n + 1
  | m, 0 -> ack1 (m-1) 1
  | m, n -> ack1 (m-1) @@ ack1 m (n-1)

(* just a different way with no tuple construction-deconstruction
 * i wonder if that makes a difference in speed/memory
 * spoiler: it doesn't *)
let rec ack2 m n =
  if m = 0 then n + 1
  else 
  if n = 0 then ack2 (m-1) 1
  else
  ack2 (m-1) (ack2 m (n-1))

(* Continuation Passing Style:
 * replace stackframes with thunks
 * look at where an evaluation would be delayed and turn it to a tailcall by
 * moving it inside the continuation.
 *
 *  m, n -> ack (m-1) @@ ack m (n-1)
 *                    ^^^^^^^^^^^^^^ 
 *  m, n -> let rhs = ack m (n-1) in
 *            ack (m-1) rhs <- not tailrec because of the above binding, but
 *                             getting closer...
 *  m, n -> ack m (n-1) (fun rhs ->
 *            ack (m-1) rhs return)
 *
 * This is called CPS. It sacrifices heap and time to save stack
 *)
let[@inline always] id x = x

let rec ack3' m n ret =
  match m, n with
  | 0, n -> ret (n+1)
  | m, 0 -> ack3' (m-1) 1 ret
  | m, n -> (ack3'[@tailcall]) m (n-1)
      (fun cont -> (ack3'[@tailcall]) (m-1) cont ret)

let ack3 m n = ack3' m n id

(* Defunctionalization: an optimization step after CPS that removes the weight
 * of thunks, replacing them with constructors.. Which should retreive some of
 * the lost speed.. I think. Also consider this: you can't send a function. You
 * can't save a function. You can't hash a function. But you can a structure!
 * https://archive.is/I3RaL ||
 * https://blog.sigplan.org/2019/12/30/defunctionalization-everybody-does-it-nobody-talks-about-it/ ||
 * https://stackoverflow.com/a/9323417 (gasche is brilliant)
 *
 * Steps:
 * Get your CPS'd function
 * Collect all the unique instances of continuation
 *   here we have two:
 *        id = (fun x -> x)
 *        (fun n -> ack (m-1) n k)
 *
 * For each of those thunks, create a variant to our datastructure cont that
 *   contains its *free variables*
 *        id has no free vars. ID
 *        the second one has m and k. Ack(m, k) where m: int, k: cont
 *
 * Finally, we create a (mutually recursive) evaluator function that expands
 *   this data and turns it into the desired computation.
 *)

(* notice how this looks a lot like a list -- we're recreating the call stack *)
type cont = Ack of int * cont
          | ID

let rec ack4' m n k =
  match m, n with
  | 0, n -> apply (n+1) k
  | m, 0 -> ack4' (m-1) 1 k
  | m, n -> ack4' m (n-1) (Ack(m-1, k))

and apply x = function
  | ID -> x
  | Ack(m, k) -> ack4' m x k

let ack4 m n = ack4' m n ID




(* Driver code *)
let () =
  let ack = ack4 in
  let n = if Array.length Sys.argv > 1 then int_of_string Sys.argv.(1) else
  (print_endline "Argument not provided. Continuing with Ack(4,1)"; 1) in
  Printf.printf "Ack(4,%d): %d\n" n (ack 4 n)
