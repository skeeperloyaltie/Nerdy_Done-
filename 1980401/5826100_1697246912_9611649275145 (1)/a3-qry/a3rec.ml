(*===========================================================================*)
(* the following functions are given *)

fun map f [] = []
  | map f (a::l) = (f a) :: (map f l);

fun reduce f init (h::t) = f h (reduce f init t)
  | reduce f init []     = init;

fun accumulate f init (h::t) = accumulate f (f init h) t
  | accumulate f init []     = init;

fun exists test [] = false
  | exists test (a::l) = if (test a) then true else exists test l;

fun forall test [] = true
  | forall test (a::l) = if (test a) then (forall test l) else false;

infix through;
fun m through n = if m>n then [] else m :: ((m+1) through n);

(*===========================================================================*)


fun cuts l = if (l = []) then [[],[]] else (l::(cuts (tl l)));

(*===========================================================================*)




fun map_rec f [] = []
  | map_rec f (a::l) = (f a) :: (map_rec f l);






fun append [] ys = ys
  | append (x::xs) ys = x::(append xs ys);

(*===========================================================================*)




fun replicate x 0 = []
  | replicate x n = x::(replicate x (n-1));

(*===========================================================================*)



fun member x [] = false
  | member x (y::ys) = (x=y) orelse member x ys;



fun prime n =
  let fun prime2 n m = if m>=n then true
                      else if n mod m = 0 then false
                      else prime2 n (m+1)
  in (n>1) andalso prime2 n 2 end;

(*===========================================================================*)





