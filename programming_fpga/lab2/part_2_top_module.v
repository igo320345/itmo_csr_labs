module dff (input clock, input [7:0]data, output reg [7:0]q);
always @(posedge clock) begin
    q <= data;
end
endmodule

module part_2_top_module(input clk, input [7:0] d, input [1:0]sel,
output reg [7:0]q);

wire [7:0] o1; 
wire [7:0] o2;
wire [7:0] o3;

dff my_dff_1(.clock(clk), .data(d), .q(o1));
dff my_dff_2(.clock(clk), .data(o1), .q(o2));
dff my_dff_3(.clock(clk), .data(o2), .q(o3));

always @(*) begin
    case (sel)
        2'b00: q = d;
        2'b01: q = o1;
        2'b10: q = o2;
        2'b11: q = o3;
    endcase
end


endmodule