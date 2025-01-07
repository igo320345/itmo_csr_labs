module dff (input clock, input data, output reg q);
always @(posedge clock) begin
    q <= data;
end
endmodule

module part_1_top_module (
    input clk, input d,
    output q);
wire o1, o2;
dff my_dff_1(.clock(clk), .data(d), .q(o1));
dff my_dff_2(.clock(clk), .data(o1), .q(o2));
dff my_dff_3(.clock(clk), .data(o2), .q(q));

endmodule