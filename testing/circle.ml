let w = 50
let h = 25
let r = 16

let ( =~ ) a b = abs(a-b) < 12

let draw_line y a x b =
  if y*y =~ r*r - x*x
  then print_char '*'
  else print_char ' '

let rec draw = function
  | _, b when b = h -> ()
  | a, b when a = w -> 
      print_char '\n'; 
      draw (0, b+1)
  | a, b -> 
      let x, y = a-w/2, 2*(b-h/2) in
      draw_line y 1 x 0;
      draw (a+1, b)

let () = draw (0, 0)
