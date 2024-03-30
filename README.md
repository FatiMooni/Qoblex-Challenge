## Thought Process

The problem at hand is to determine the maximum number of products we can construct based on the availability of different pieces in stock.

let's consider a product P composed of two bundles B1 and B2.
To assemble a complete P, an equal number of pieces from B1 and B2 must be available.
Therefore, the number of possible products is limited by the minimum quantity of pieces available for either B1 or B2.

Similarly, if another product P' requires one (1) piece from B1 and two (2) pieces from B2, then the number of possible products is constrained by the minimum of the available quantity of B1 pieces divided by 1 and the available quantity of B2 pieces divided by 2.

We can generalize this approach using recursion:

For any bundle Bx requiring 'num_req_piece_x' pieces (where 'x' ranges from 1 to 'n'), the maximum number of products (P) we can build is given by:

P = min(B1 / num_req_piece_1, B2 / num_req_piece_2, ......, Bx / num_req_piece_x)

To implement this solution, we represent the product as an N-ary tree, with the root node representing the target product P0.
the subsequent nodes representing different bundles required for assembly. We utilize a Depth First Search (DFS) algorithm to traverse each bundle, recursively calculating the maximum number of products achievable based on available pieces from dependent bundles. Finally, we compare the local output obtained from each bundle level to determine the overall maximum number of products that can be built.

# RUN code

cd qoblex_challenge
python ./bundles.py
