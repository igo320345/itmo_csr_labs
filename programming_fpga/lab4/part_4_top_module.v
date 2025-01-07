module part_4_top_module (input clk, input reset,
 input data, input ack, output reg [3:0] count, output counting = 0, output done = 0, output reg [8*5:0] state = "S", output reg [3:0] delay = 0, output reg [20:0] c = 0);

always @(posedge clk) begin
    case (state)
        "S" : begin
            if (data == 1) state <= "S1";
        end
        "S1" : begin
            if (data == 0) state <= "S";
            if (data == 1) state <= "S11";
        end
        "S11" : begin
            if (data == 0) state <= "S110";
        end
        "S110" : begin
            if (data == 0) state <= "S";
            if (data == 1) state <= "B0";
        end
        "B0" : begin
            delay[0] <= data;
            delay = delay << 1;
            state <= "B1";
        end
        "B1" : begin
            delay[0] <= data;
            delay = delay << 1;
            state <= "B2";
        end
        "B2": begin
            delay[0] <= data;
            delay = delay << 1;
            state <= "B3";
        end
        "B3": begin
            delay[0] <= data;
            delay = delay << 1;
            state <= "Count";
            counting <= 1;
            count = 1;
        end
        "Count": begin
            count += 1;
            c += 1;
            if (c == (delay + 1) * 1000) begin
                count = 4'bxxxx;
                state <= "Wait";
                counting <= 0;
                done <= 1;
            end
        end
        "Wait": begin
            if (ack) begin
                c <= 0;
                done <= 0;
                state <= "S";
            end
        end
    endcase
    
    if (reset) begin
        c <= 0;
        counting <= 0;
        done <= 0;
        state <= "S";
        count = 4'bxxxx;
    end
end
endmodule