module add16 (input cin, input [15:0] a, input [15:0] b, output [15:0] sum, output cout);
  wire [16:0] c;	
  assign c[0] = cin;	
  assign cout = c[16];	

  assign sum[15:0] = (a[15:0] ^ b[15:0]) ^ c[15:0];
  assign c[16:1]   = (a[15:0] & b[15:0]) | 
                     (a[15:0] ^ b[15:0]) & c[15:0];
endmodule

module part_5_top_module (input [31:0] a, input [31:0] b, input sub, output [31:0] sum);

wire cout;
wire [15:0] sum1;
wire [15:0] sum2;

reg [31:0] new_b;

assign new_b = sub ? ~b : b;

add16 add16_1(.cin(sub), .cout(cout), .a(a[15:0]), .b(b[15:0]), .sum(sum1));
add16 add16_2(.cin(cout), .a(a[31:16]), .b(b[31:16]), .sum(sum2));

assign sum[15:0] = sum1;
assign sum[31:16] = sum2;

endmodule