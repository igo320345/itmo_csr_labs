module part_1_top_module (input a, input b, input c, input d, output q);
assign q = (a | b) & (c | d) ;
endmodule