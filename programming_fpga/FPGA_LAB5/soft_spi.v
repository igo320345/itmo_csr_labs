module soft_spi (
    input clk,         // System clock
    output reg data = 0,   // Data output
    output reg ss = 1,     // Slave select output
     output clk_out, // SPI clock output
     output IO_voltage
);
    

     Gowin_rPLL my_rpll(
         .clkout(clkout), //output clkout
         .lock(lock), //output lock
         .clkoutd(clkoutd), //output clkoutd
         .clkin(clk) //input clkin
    );

    led blinking_led(.clk(clk), .IO_voltage(IO_voltage));

    reg [4:0] d = 0;
    reg [31:0] showing_number = 1_000_000; // 2^27 = 134.217.728 , because max number is "9999.9999" ~ 10^8 ~ 2^27 is enough
    parameter COUNT_SEC = 50000; // // 50.000 Hz now for 1-second increment
    reg [15:0] count_sec = 0;    // Counter for 1-second timing
    reg [4:0] bit_index = 0;
    wire [15:0] bcd;
    

   wire [3:0] bcd0;
   wire [3:0] bcd1;
   wire [3:0] bcd2;
   wire [3:0] bcd3;
   wire [3:0] bcd4;
   wire [3:0] bcd5;
   wire [3:0] bcd6;
   wire [3:0] bcd7;
   wire [3:0] bcd8;
   wire [3:0] bcd9;
   
   reg  RST;
   reg  en = 1; 
   wire  fin; 
   wire  busy;
    
    
   bin2bcd bcd_converter(.bin(showing_number), 
                        .RST(RST), 
                        .CLK(clk), 
                        .en(en), 
                        .busy(busy), 
                        .fin(fin), 
                        .bcd0(bcd0), .bcd1(bcd1), .bcd2(bcd2), 
                        .bcd3(bcd3), .bcd4(bcd4), .bcd5(bcd5), 
                        .bcd6(bcd6), .bcd7(bcd7), .bcd8(bcd8), .bcd9(bcd9));   
   
    assign clk_out = ~clkoutd;

    reg [15:0] spi_data [7:0];     // 8 digits, each 16-bit SPI data
    reg [3:0] digit_index = 0;     // Current digit being sent

    reg [4:0] spi_bit_index = 0;   // Current bit in SPI frame

    // LUT for Seven-Segment Patterns
    reg [7:0] segment_lut [9:0]; // for 0-9
    initial begin
        segment_lut[0] = 8'b1111_1100; // 0
        segment_lut[1] = 8'b0110_0000; // 1
        segment_lut[2] = 8'b1101_1010; // 2
        segment_lut[3] = 8'b1111_0010; // 3
        segment_lut[4] = 8'b0110_0110; // 4
        segment_lut[5] = 8'b1011_0110; // 5
        segment_lut[6] = 8'b1011_1110; // 6
        segment_lut[7] = 8'b1110_0000; // 7
        segment_lut[8] = 8'b1111_1110; // 8
        segment_lut[9] = 8'b1111_0110; // 9
    end
    
    always @(posedge clkoutd) begin
            if (~lock) begin 
                RST <= 0; 
            end 
            else begin 
                RST <= 1; 
            end            
        end
 
    always @(negedge clkoutd) begin


        count_sec <= count_sec + 1'b1;
        if (count_sec >= COUNT_SEC) begin
            count_sec <= 0;
            showing_number <= showing_number + 1'b1;
            en <= 1;
        end 

        ss<=1;
        data <= spi_data[digit_index][spi_bit_index]; 
                spi_bit_index <= spi_bit_index + 1'b1;
                if (spi_bit_index == 16) begin
                    spi_bit_index <= 0;
                    ss <= 0;
                    digit_index <= digit_index + 1'b1;
                    if (digit_index == 8) begin
                        digit_index <= 0;
                    end
                end

        if (fin) begin        
            spi_data[0][15:8] <= 8'b1111_1110;  // Digit 1
            spi_data[0][7:0] <= segment_lut[bcd0];  // Digit 1

            spi_data[1][15:8] <= 8'b1111_1101;  // Digit 2
            spi_data[1][7:0] <= segment_lut[bcd1];  // Digit 2

            spi_data[2][15:8] <= 8'b1111_1011;  // Digit 3
            spi_data[2][7:0] <= segment_lut[bcd2];  // Digit 4

            spi_data[3][15:8] <= 8'b1111_0111;  // Digit 4
            spi_data[3][7:0] <= segment_lut[bcd3];  // Digit 4

            spi_data[4][15:8] <= 8'b1110_1111;  // Digit 5
            spi_data[4][7:0] <= segment_lut[bcd4];  // Digit 5

            spi_data[5][15:8] <= 8'b1101_1111;  // Digit 6
            spi_data[5][7:0] <= segment_lut[bcd5];  // Digit 6

            spi_data[6][15:8] <= 8'b1011_1111;  // Digit 7
            spi_data[6][7:0] <= segment_lut[bcd6];  // Digit 7

            spi_data[7][15:8] <= 8'b0111_1111;  // Digit 8
            spi_data[7][7:0] <= segment_lut[bcd7];  // Digit 8
            en <=0;
       end
    end
endmodule