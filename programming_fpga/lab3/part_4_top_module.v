module part_4_top_module (input clock, input a, output reg p = 0, output reg q = 0);

always @ (*) begin
    if (clock & (p != 0)) p= 0;
    if (clock & a)
		p = p + 1;
    if(!clock &(p != q))
    q = p;
end

endmodule