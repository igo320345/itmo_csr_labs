`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_3_tb;

	reg clk = 1;
    reg reset = 1;
    reg data = 0;
    wire start_shifting;

    always #5 clk += 1;

	part_3_top_module top0
	(
		.clk(clk),
        .reset(reset),
        .data(data),
        .start_shifting(start_shifting)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_3_tb);	
		# 10 reset <= 0;
        # 5 data <= 1;
        # 10 data <= 0;
        # 10 data <= 1;
		# 50 data <= 0;
		# 10 data <= 1;
		# 20 data <= 0;
		# 20 data <= 1; reset <= 1;
        
		# 20 $finish();
	end

	initial begin
		$monitor("t=%-4d: clk = %d, reset = %d, data = %d, start_shifting = %d", $time, clk, reset, data, start_shifting);
	end
endmodule