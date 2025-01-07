`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_6_tb;
    reg clock = 1, a, b;
    wire q, state;

    always #5 clock += 1;

	part_6_top_module top0
	(
		.clock(clock),
        .a(a),
        .b(b),
        .q(q),
        .state(state)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_6_tb);
        # 15 a <= 0; b <= 0;
        # 25 b <= 1;
        # 10 a <= 1; b <= 0;
        # 10 b <= 1;
        # 10 a <= 0; b <= 0;
        # 10 a <= 1; b <= 1;
        # 30 b <= 0;
        # 10 a <= 0; b <= 1;
        # 10 b <= 0;
  
		#20 $finish();
	end

	initial begin
		$monitor("t=%-4d: clock =  %d, a = %d, b = %d, q = %d, state = %d", $time, clock, a, b, q, state);
	end
endmodule