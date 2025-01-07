module part_1_top_module (input clk, input reset, output reg [9:0] q = 0);
always @(posedge clk) begin
    q += 1;
    if (q > 999) q <= 0;
    if (reset) q = 0;
    
end    
endmodule