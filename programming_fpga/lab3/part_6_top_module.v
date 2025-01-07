module part_6_top_module (input clock, input a, input b, output reg q, output wire state );
reg s;
always @(posedge clock) begin
    if (a==b) s <= a;
end
assign q = s^a^b;
assign state = s;
endmodule