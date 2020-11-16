type letter = Uchar.t

type haraka = [ `Fatha | `Damma | `Kasra ]
type tanwen = [ `Tanwen of haraka ]
type shadda = [ `Shadda of [ haraka | `Sukoon ] ]

type abjad = C of letter
           | V of letter * [ haraka | tanwen | shadda | `Sukoon ]



let aux: [> haraka ] -> string = function
    | `Fatha -> "fatha"
    | `Damma -> "damma"
    | `Kasra -> "kasra"
    | _ -> assert false

let tashkeel: abjad -> string = function
    | C _ -> ""
    | V(_, x) -> begin
        match x with
        | `Sukoon -> "sukoon"
        | `Tanwen a -> "tanween "^ aux a
        | `Shadda a -> begin 
            match a with `Sukoon -> "shadda" 
                | _ -> aux a ^" mashdooda"
        end
        | har -> aux har
    end


let print = print_endline
let () = V(Uchar.of_int 0x62d, `Shadda`Fatha) |> tashkeel |> print;
         C(Uchar.of_int 0x62d)                |> tashkeel |> print;
