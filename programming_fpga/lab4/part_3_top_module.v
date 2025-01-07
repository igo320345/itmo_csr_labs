module part_3_top_module (input clk, input reset,
 input data, output start_shifting = 0);

reg [3:0] d;
always @(posedge clk) begin
    if (d == 4'b1101) start_shifting <= 1;
    if (reset) start_shifting <= 0;
    d[0] <= data;
    d = d << 1;
end
endmodule