module part_3_top_module (input [3:0] a, input [3:0] b, input [3:0] c, input [3:0] d, input [3:0] e, output [3:0] q);

assign q = (c == 0) ? b : 
            (c == 1) ? e: 
            (c == 2) ? a: 
            (c==3)? d :
            15;

endmodule