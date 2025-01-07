`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_2_tb;

	reg clk = 0;
    reg shift_ena = 0;
    reg count_ena = 0;
    reg data;
    reg [3:0] q;

    always #5 clk += 1;

	part_2_top_module top0
	(
		.clk(clk),
        .shift_ena(shift_ena),
        .count_ena(count_ena),
        .data(data),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_2_tb);	
		# 15 shift_ena <= 1; data <= 1;
        # 10 data <= 0;
        # 20 data <= 1;
        # 10 shift_ena <= 0; data <= 1'bX;
        # 20 count_ena <= 1;
        # 30 count_ena <= 0;
		# 20 $finish();
	end

	initial begin
		$monitor("t=%-4d: clk = %d, shift_ena = %d, count_ena = %d, data = %d, q = %d", $time, clk, shift_ena, count_ena, data, q);
	end
endmodule