module part_2_top_module(input clk, 
input shift_ena, input count_ena, input data, 
output reg [3:0] q = 0);

always @(posedge clk) begin
    if (shift_ena) q = q << 1;
    if (count_ena) q -= 1;
    if (data) q[0] <= data;
end
endmodule