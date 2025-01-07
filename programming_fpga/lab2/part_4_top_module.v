module add16 (input cin, input [15:0] a, input [15:0] b, output [15:0] sum, output cout);
  wire [16:0] c;	
  assign c[0] = cin;	
  assign cout = c[16];	

  assign sum[15:0] = (a[15:0] ^ b[15:0]) ^ c[15:0];
  assign c[16:1]   = (a[15:0] & b[15:0]) | 
                     (a[15:0] ^ b[15:0]) & c[15:0];
endmodule



module part_4_top_module (input [31:0] a, input [31:0] b, output reg [31:0] sum);

reg cout;
reg [15:0] sum1;
reg [15:0] sum2;
reg [15:0] sum3;

add16 add16_1(.cin(0), .cout(cout), .a(a[15:0]), .b(b[15:0]), .sum(sum1));
add16 add16_2(.cin(0), .a(a[31:16]), .b(b[31:16]), .sum(sum2));
add16 add16_3(.cin(1), .a(a[31:16]), .b(b[31:16]), .sum(sum3));

always @(*) begin
    if (!cout) begin
        sum[15:0] = sum1;
        sum[31:16] = sum2;
    end
    else begin
        sum[15:0] = sum1;
        sum[31:16] = sum3;
    end
end

endmodule