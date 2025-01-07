`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_1_tb;

	reg clk = 0;
    reg reset = 0;
    reg [9:0] q;
    always #5 clk += 1;

	part_1_top_module top0
	(
		.clk(clk),
        .reset(reset),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_1_tb);	
		# 85 reset <= 1;
        # 10 reset <= 0;
		# 20 $finish();
	end

	initial begin
		$monitor("t=%-4d: clk = %d, reset = %d, q = %d", $time, clk, reset, q);
	end
endmodule