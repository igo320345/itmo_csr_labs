`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_1_tb;

	wire q;
    reg a, b, c, d;

    reg [3:0] in = 0;
    always #5 in += 1;

	part_1_top_module top0
	(
		.a(in[3]),
        .b(in[2]),
        .c(in[1]),
        .d(in[0]),
        .q(q)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_1_tb);	
		// # 5 in = 0;
		// # 10 in = 0;
		// # 15 in = 0;
		#90 $finish();
	end

	initial begin
		$monitor("t=%-4d: a = %d, b = %d, c = %d, d = %d, q = %d", $time, in[3], in[2], in[1], in[0], q);
	end
endmodule