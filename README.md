## Thought Process

the problem is straight forward , we want to count total number of products we can build based on number of different pieces avaialable in stock

let's imagine a product P that is composed out of 2 pieces ( bundles ) B1 and B2, to be able to build a complete model of product P , B1 and B2 pieces need to be available equally, hence :

1. number of possible products = min ( number of pieces B1, number of pieces B2)

similaraly , if we had product P' that is built out of one bundle B1 and 2 pieces of B2 then : 2. number of possible products = min ( (number of pieces B1) / 1,(number of pieces B2) / 2)

from 1 and 2, by recurrission :

P = min (Bx / num_req_piece_x)
Bx : Bundle
num_req_piece_x : number of required pieces ( 1 ... m)
x = (1 ... n)

in order to achieve this solution, we gonna represent the product by N-ary tree where root is the P0 or item we aim to build and nodes are different bundles that are used to achieve that. to calculate the total number of bikes to build, I propose a solution based on DFS algorithm (Depth First Search).

for each bundle, we go in depth and count how many pieces we can build based on children (dependent bundles) then we use the local output and compare it with same level bundles to calculate the maximum
