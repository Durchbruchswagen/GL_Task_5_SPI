import serial
import time

COM_PORT = 'COM4' 
BAUD_RATE = 9600
TIMEOUT = 1  

def main():
    print(f"--- Attempting to connect to {COM_PORT} at {BAUD_RATE} baud ---")
    
    try:
        ser = serial.Serial(port=COM_PORT, baudrate=BAUD_RATE, timeout=TIMEOUT)

        ser.reset_input_buffer()
        print("Connected successfully! Press Ctrl+C to stop.\n")
        
        while True:
            if ser.in_waiting > 0:
                raw_line = ser.readline()
                
                try:
                    decoded_line = raw_line.decode('utf-8').strip()
                    
                    if decoded_line:
                        print(decoded_line)
                        
                except UnicodeDecodeError:
                    print(f"Malformed data received: {raw_line}")
                    
            time.sleep(0.01)

    except serial.SerialException as e:
        print(f"\n[Error] Could not open serial port {COM_PORT}.")
        print("Please check your connection and ensure the port isn't open in another program (like Putty).")
        print(f"Details: {e}")
        
    except KeyboardInterrupt:
        print("\nStopping UART script. Goodbye!")
        
    finally:
        # Ensure the port is closed when exiting
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == '__main__':
    main()