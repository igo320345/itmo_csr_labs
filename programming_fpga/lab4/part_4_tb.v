`timescale 1ns/100ps // 1 ns time unit, 100 ps resolution

module part_4_tb;

	reg clk = 1;
    reg reset = 1;
    reg data = 0;
    reg [3:0] count;
    wire counting;
    wire done;
    reg ack;

    reg [8*5:0] state ;
    reg [3:0] delay;
    reg [20:0] c;


    always #5 clk += 1;

	part_4_top_module top0
	(
		.clk(clk),
        .reset(reset),
        .data(data),
        .count(count),
        .counting(counting),
        .done(done),
        .ack(ack),
        .state(state),
        .delay(delay),
        .c(c)
	);

	initial begin
		$dumpfile("wave.vcd");	
		$dumpvars(0, part_4_tb);	
		# 10 reset <= 0; data <= 1;
        # 10 data <= 0;
        # 20 data <= 1;
        # 20 data <= 0;
        # 10 data <= 1;
        # 10 data <= 0;
        # 30 data <= 1;
        # 10 data <= 1'bx;
        
		# 25000 ack <= 1;
        # 10 ack <= 0;
        # 50 $finish();
	end

	initial begin
		$monitor("t=%-4d: clk = %d, reset = %d, data = %d, count = %d, counting = %d, done = %d, ack = %d", $time, clk, reset, data, count, counting, done, ack);
	end
endmodule